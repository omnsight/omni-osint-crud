from unittest.mock import patch

import jwt
from fastapi.testclient import TestClient
from omni_python_library import init_omni_library
from omni_python_library.models.osint import WebsiteMainData
from omni_python_library.utils.config import UserRole

from omni_osint_crud.main import app


class TestWebsite:
    client: TestClient
    no_roles_client: TestClient

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

    def test_website_crud_cycle(self):
        # 1. Create Website
        create_data = WebsiteMainData(title="Test Website", url="http://test.com")
        response = self.client.post("/website", json=create_data.model_dump())
        assert response.status_code == 200
        created_website = response.json()
        website_id = created_website["_id"]
        assert website_id
        assert created_website["title"] == "Test Website"

        # 2. Read Website
        response = self.client.get(f"/website/{website_id}")
        assert response.status_code == 200
        assert response.json() == created_website

        # 3. Update Website
        update_data = WebsiteMainData(title="Test Website Updated", url="http://test-updated.com")
        response = self.client.put(f"/website/{website_id}", json=update_data.model_dump())
        assert response.status_code == 200
        updated_website = response.json()
        assert updated_website["title"] == "Test Website Updated"

        # 4. Delete Website
        response = self.client.delete(f"/entity/{website_id}")
        assert response.status_code == 200

        # 5. Verify Deletion
        response = self.client.get(f"/website/{website_id}")
        assert response.status_code == 404

    ######################################################################################################
    # Test Creates
    ######################################################################################################

    def test_create_website_permission_denied(self):
        create_data = WebsiteMainData(title="Test Website", url="http://test.com")
        response = self.no_roles_client.post("/website", json=create_data.model_dump())
        assert response.status_code == 403

    @patch("omni_osint_crud.routers.create.dal.create_website")
    def test_create_website_internal_error(self, mock_create_website):
        mock_create_website.side_effect = Exception("DB error")
        create_data = WebsiteMainData(title="Test Website", url="http://test.com")
        response = self.client.post("/website", json=create_data.model_dump())
        assert response.status_code == 500

    ######################################################################################################
    # Test Reads
    ######################################################################################################

    def test_read_website_not_found(self):
        response = self.client.get("/website/non-existent-id")
        assert response.status_code == 404

    def test_read_website_not_found_bad_id(self):
        response = self.client.get("/website/bad_collection/bad_key")
        assert response.status_code == 404

    def test_read_website_permission_denied(self):
        create_data = WebsiteMainData(title="Test Website", url="http://test.com")
        response = self.client.post("/website", json=create_data.model_dump())
        assert response.status_code == 200
        created_website = response.json()
        website_id = created_website["_id"]

        response = self.no_roles_client.get(f"/website/{website_id}")
        assert response.status_code == 403

    @patch("omni_osint_crud.routers.read.dal.get_website")
    def test_read_website_internal_error(self, mock_get_website_by_id):
        mock_get_website_by_id.side_effect = Exception("DB error")
        response = self.client.get("/website/some-id")
        assert response.status_code == 500

    ######################################################################################################
    # Test Updates
    ######################################################################################################

    # Test update_website

    def test_update_website_not_found(self):
        update_data = WebsiteMainData(title="Jane Doe", url="http://jane.com")
        response = self.client.put("/website/non-existent-id", json=update_data.model_dump())
        assert response.status_code == 404

    def test_update_website_permission_denied(self):
        create_data = WebsiteMainData(title="Test Website", url="http://test.com")
        response = self.client.post("/website", json=create_data.model_dump())
        assert response.status_code == 200
        created_website = response.json()
        website_id = created_website["_id"]

        update_data = WebsiteMainData(title="Test Website Updated", url="http://test-updated.com")
        response = self.no_roles_client.put(f"/website/{website_id}", json=update_data.model_dump())
        assert response.status_code == 403

    @patch("omni_osint_crud.routers.update.dal.update_website")
    def test_update_website_internal_error(self, mock_update_website):
        mock_update_website.side_effect = Exception("DB error")
        update_data = WebsiteMainData(title="Test Website Updated", url="http://test-updated.com")
        response = self.client.put("/website/some-id", json=update_data.model_dump())
        assert response.status_code == 500

    # Test update_website_permissions

    def test_update_website_permissions_not_found(self):
        update_data = {"owner": "new-owner"}
        response = self.client.put("/website/non-existent-id/permissions", json=update_data)
        assert response.status_code == 404

    def test_update_website_permissions_permission_denied(self):
        # 1. Create a website with the admin client
        create_data = WebsiteMainData(title="Test Website", url="http://example.com")
        response = self.client.post("/website", json=create_data.model_dump())
        assert response.status_code == 200
        created_website = response.json()
        website_id = created_website["_id"]

        # 2. Grant the user_client read access
        permission_data = {"read": ["test-user-id-789"]}
        response = self.client.put(f"/website/{website_id}/permissions", json=permission_data)
        assert response.status_code == 200

        # 3. Attempt to update permissions with the user_client (non-owner)
        update_data = {"owner": "new-owner"}
        response = self.user_client.put(f"/website/{website_id}/permissions", json=update_data)
        assert response.status_code == 403

    @patch("omni_osint_crud.routers.update.dal.update_website")
    def test_update_website_permissions_internal_error(self, mock_update_website):
        mock_update_website.side_effect = Exception("DB error")
        update_data = {"owner": "new-owner"}
        response = self.client.put("/website/some-id/permissions", json=update_data)
        assert response.status_code == 500

    ######################################################################################################
    # Test Deletes
    ######################################################################################################

    def test_delete_website_not_found(self):
        response = self.client.delete("/entity/non-existent-id")
        assert response.status_code == 404

    def test_delete_website_permission_denied(self):
        create_data = WebsiteMainData(title="Test Website", url="http://test.com")
        response = self.client.post("/website", json=create_data.model_dump())
        assert response.status_code == 200
        created_website = response.json()
        website_id = created_website["_id"]

        response = self.no_roles_client.delete(f"/entity/{website_id}")
        assert response.status_code == 403

    @patch("omni_osint_crud.routers.delete.dal.delete_entity")
    def test_delete_website_internal_error(self, mock_delete_entity):
        mock_delete_entity.side_effect = Exception("DB error")
        response = self.client.delete("/entity/some-id")
        assert response.status_code == 500
