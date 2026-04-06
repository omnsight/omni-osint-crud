from unittest.mock import patch

import jwt
from fastapi.testclient import TestClient
from omni_python_library import init_omni_library
from omni_python_library.models import (
    OsintViewMainData,
    PersonMainData,
)
from omni_python_library.utils.config.user import UserRole

from omni_osint_crud.main import app


class TestView:
    client: TestClient
    no_roles_client: TestClient
    user_client: TestClient

    @classmethod
    def setup_class(cls):
        init_omni_library()
        # Client with admin roles
        payload = {"sub": "test-user-id-123", "roles": [UserRole.ADMIN]}
        token = jwt.encode(payload, key=None, algorithm="none")
        cls.client = TestClient(app)
        cls.client.headers = {"Authorization": f"Bearer {token}"}

        # Client with no roles
        no_roles_payload = {"sub": "test-user-id-456", "roles": []}
        no_roles_token = jwt.encode(no_roles_payload, key=None, algorithm="none")
        cls.no_roles_client = TestClient(app)
        cls.no_roles_client.headers = {"Authorization": f"Bearer {no_roles_token}"}

        # Client with a user role but not admin
        user_payload = {"sub": "test-user-id-789", "roles": [UserRole.USER]}
        user_token = jwt.encode(user_payload, key=None, algorithm="none")
        cls.user_client = TestClient(app)
        cls.user_client.headers = {"Authorization": f"Bearer {user_token}"}

    ######################################################################################################
    # Overall Flow
    ######################################################################################################

    def test_view_crud_cycle(self):
        # Create View
        create_data = OsintViewMainData(
            name="Test View",
            description="A test view",
            analysis=[
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "Hello world!",
                        }
                    ],
                }
            ],
        )
        response = self.client.post("/views", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        created_view = response.json()
        view_id = created_view["_id"]
        assert view_id
        assert created_view["name"] == "Test View"

        # Read View
        response = self.client.get(f"/views/{view_id}")
        assert response.status_code == 200
        assert response.json() == created_view
        assert len(response.json()["analysis"]) == 1

        # Update View
        update_data = OsintViewMainData(name="Test View Updated")
        response = self.client.put(f"/views/{view_id}", json=update_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        updated_view = response.json()
        assert updated_view["name"] == "Test View Updated"
        assert len(response.json()["analysis"]) == 1

        # Connect entity to view
        person_data = PersonMainData(name="John Doe")
        response = self.client.post("/persons", json=person_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        person_id = response.json()["_id"]

        response = self.client.post(f"/views/{view_id}/entities", json={"entity_id": person_id})
        assert response.status_code == 200

        # Get view entities
        response = self.client.get(f"/views/{view_id}/entities")
        assert response.status_code == 200

        # Query Views
        response = self.client.get(f"/views?text=Test")
        assert response.status_code == 200
        assert len(response.json()["views"]) > 0

        # Delete View
        response = self.client.delete(f"/views/{view_id}")
        assert response.status_code == 200

        # Verify Deletion
        response = self.client.get(f"/views/{view_id}")
        assert response.status_code == 404

    ######################################################################################################
    # Test Creates
    ######################################################################################################

    # Test create_view

    def test_create_view_missing_name(self):
        create_data = OsintViewMainData(description="A test view", analysis=[])
        response = self.client.post("/views", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 400

    def test_create_view_missing_description(self):
        create_data = OsintViewMainData(name="Test View", analysis=[])
        response = self.client.post("/views", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 400

    def test_create_view_missing_analysis(self):
        create_data = OsintViewMainData(name="Test View", description="A test view")
        response = self.client.post("/views", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 400

    def test_create_view_permission_denied(self):
        create_data = OsintViewMainData(name="Test View", description="A test view", analysis=[])
        response = self.no_roles_client.post("/views", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 403

    @patch("omni_osint_crud.routers.create.view_dal.create_view")
    def test_create_view_internal_error(self, mock_create_view):
        mock_create_view.side_effect = Exception("DB error")
        create_data = OsintViewMainData(name="Test View", description="A test view", analysis=[])
        response = self.client.post("/views", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 500

    ######################################################################################################
    # Test Reads
    ######################################################################################################

    # Test get_view

    def test_read_view_not_found(self):
        response = self.client.get("/views/bad_collection/bad_key")
        assert response.status_code == 404

    def test_read_view_permission_denied(self):
        create_data = OsintViewMainData(name="Test View", description="A test view", analysis=[])
        response = self.client.post("/views", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        view_id = response.json()["_id"]

        response = self.no_roles_client.get(f"/views/{view_id}")
        assert response.status_code == 403

    @patch("omni_osint_crud.routers.read.view_dal.get_view")
    def test_read_view_internal_error(self, mock_read_view):
        mock_read_view.side_effect = Exception("DB error")
        response = self.client.get("/views/view/some-id")
        assert response.status_code == 500

    # Test get_view_entities

    def test_get_view_entities_not_found(self):
        response = self.client.get("/views/view/non-existent-id/entities")
        assert response.status_code == 404

    def test_get_view_entities_no_permission(self):
        create_data = OsintViewMainData(name="Test View", description="A test view", analysis=[])
        response = self.client.post("/views", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        view_id = response.json()["_id"]

        person_data = PersonMainData(name="John Doe")
        response = self.client.post("/persons", json=person_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        person_id = response.json()["_id"]

        response = self.client.post(f"/views/{view_id}/entities", json={"entity_id": person_id})
        assert response.status_code == 200

        response = self.no_roles_client.get(f"/views/{view_id}/entities")
        assert response.status_code == 403

    @patch("omni_osint_crud.routers.read.view_dal.get_entities")
    def test_get_view_entities_internal_error(self, mock_get_entities):
        mock_get_entities.side_effect = Exception("DB error")
        response = self.client.get("/views/bad-collection/bad-key/entities")
        assert response.status_code == 500

    # Test query_views

    @patch("omni_osint_crud.routers.read.view_dal.query_views")
    def test_query_views_internal_error(self, mock_query_views):
        mock_query_views.side_effect = Exception("DB error")
        response = self.client.get("/views?text=Test")
        assert response.status_code == 500

    ######################################################################################################
    # Test Updates
    ######################################################################################################

    # Test update_view

    def test_update_view_not_found(self):
        update_data = OsintViewMainData(name="Test View Updated")
        response = self.client.put("/views/bad_collection/bad_key", json=update_data.model_dump(exclude_unset=True))
        assert response.status_code == 404

    def test_update_view_permission_denied(self):
        create_data = OsintViewMainData(name="Test View", description="A test view", analysis=[])
        response = self.client.post("/views", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        created_view = response.json()
        view_id = created_view["_id"]

        update_data = OsintViewMainData(name="Test View Updated")
        response = self.no_roles_client.put(f"/views/{view_id}", json=update_data.model_dump(exclude_unset=True))
        assert response.status_code == 403

    @patch("omni_osint_crud.routers.update.view_dal.update_view")
    def test_update_view_internal_error(self, mock_update_view):
        mock_update_view.side_effect = Exception("DB error")
        update_data = OsintViewMainData(name="Test View Updated")
        response = self.client.put("/views/view/some-id", json=update_data.model_dump(exclude_unset=True))
        assert response.status_code == 500

    # Test update_view_permissions

    def test_update_view_permissions_not_found(self):
        update_data = {"owner": "new-owner"}
        response = self.client.put("/views/view/non-existent-id/permissions", json=update_data)
        assert response.status_code == 404

    def test_update_view_permissions_permission_denied(self):
        # 1. Create a view with the admin client
        create_data = OsintViewMainData(name="Test View", description="A test view", analysis=[])
        response = self.client.post("/views", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        created_view = response.json()
        view_id = created_view["_id"]

        # 2. Grant the user_client read access
        permission_data = {"read": ["test-user-id-789"]}
        response = self.client.put(f"/views/{view_id}/permissions", json=permission_data)
        assert response.status_code == 200

        # 3. Attempt to update permissions with the user_client (non-owner)
        update_data = {"owner": "new-owner"}
        response = self.user_client.put(f"/views/{view_id}/permissions", json=update_data)
        assert response.status_code == 403

    @patch("omni_osint_crud.routers.update.view_dal.update_view")
    def test_update_view_permissions_internal_error(self, mock_update_view):
        mock_update_view.side_effect = Exception("DB error")
        update_data = {"owner": "new-owner"}
        response = self.client.put("/views/view/some-id/permissions", json=update_data)
        assert response.status_code == 500

    # Test connect_entity_to_view

    def test_connect_entity_to_view_not_found(self):
        response = self.client.post("/views/view/non-existent-id/entities", json={"entity_id": "person/123"})
        assert response.status_code == 404

    def test_connect_entity_to_view_permission_denied(self):
        create_data = OsintViewMainData(name="Test View", description="A test view", analysis=[])
        response = self.client.post("/views", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        view_id = response.json()["_id"]

        person_data = PersonMainData(name="John Doe")
        response = self.client.post("/persons", json=person_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        person_id = response.json()["_id"]

        response = self.no_roles_client.post(f"/views/{view_id}/entities", json={"entity_id": person_id})
        assert response.status_code == 403

    @patch("omni_osint_crud.routers.update.view_dal.connect_entity_to_view")
    def test_connect_entity_to_view_internal_error(self, mock_connect_entity_to_view):
        mock_connect_entity_to_view.side_effect = Exception("DB error")
        response = self.client.post("/views/view/some-id/entities", json={"entity_id": "person/123"})
        assert response.status_code == 500

    ######################################################################################################
    # Test Deletes
    ######################################################################################################

    # Test delete_view

    def test_delete_view_not_found(self):
        response = self.client.delete("/views/bad_collection/bad_key")
        assert response.status_code == 404

    def test_delete_view_permission_denied(self):
        create_data = OsintViewMainData(name="Test View", description="A test view", analysis=[])
        response = self.client.post("/views", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        created_view = response.json()
        view_id = created_view["_id"]

        response = self.no_roles_client.delete(f"/views/{view_id}")
        assert response.status_code == 403

    @patch("omni_osint_crud.routers.delete.view_dal.delete_view")
    def test_delete_view_internal_error(self, mock_delete_view):
        mock_delete_view.side_effect = Exception("DB error")
        response = self.client.delete("/views/view/some-id")
        assert response.status_code == 500
