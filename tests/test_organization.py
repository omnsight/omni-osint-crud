from unittest.mock import patch

import jwt
from fastapi.testclient import TestClient
from omni_python_library import init_omni_library
from omni_python_library.models.osint import OrganizationMainData
from omni_python_library.utils.config import UserRole

from omni_osint_crud.main import app


class TestOrganization:
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

    def test_organization_crud_cycle(self):
        # 1. Create Organization
        create_data = OrganizationMainData(name="Test Corp")
        response = self.client.post("/create/organization", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        created_organization = response.json()
        organization_id = created_organization["_id"]
        assert organization_id
        assert created_organization["name"] == "Test Corp"

        # 2. Read Organization
        response = self.client.get(f"/read/organization/{organization_id}")
        assert response.status_code == 200
        assert response.json() == created_organization

        # 3. Update Organization
        update_data = OrganizationMainData(name="Test Corp Updated")
        response = self.client.put(
            f"/update/organization/{organization_id}", json=update_data.model_dump(exclude_unset=True)
        )
        assert response.status_code == 200
        updated_organization = response.json()
        assert updated_organization["name"] == "Test Corp Updated"

        # 4. Delete Organization
        response = self.client.delete(f"/delete/entity/{organization_id}")
        assert response.status_code == 200

        # 5. Verify Deletion
        response = self.client.get(f"/read/organization/{organization_id}")
        assert response.status_code == 404

    def test_create_organization_permission_denied(self):
        create_data = OrganizationMainData(name="Test Corp")
        response = self.no_roles_client.post("/create/organization", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 403

    def test_read_organization_not_found(self):
        response = self.client.get("/read/organization/non-existent-id")
        assert response.status_code == 404

    def test_read_organization_bad_id(self):
        response = self.client.get("/read/organization/bad_collection/bad_key")
        assert response.status_code == 404

    def test_update_organization_permission_denied(self):
        create_data = OrganizationMainData(name="Test Corp")
        response = self.client.post("/create/organization", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        created_organization = response.json()
        organization_id = created_organization["_id"]

        update_data = OrganizationMainData(name="Jane Doe")
        response = self.no_roles_client.put(
            f"/update/organization/{organization_id}", json=update_data.model_dump(exclude_unset=True)
        )
        assert response.status_code == 403

    def test_update_organization_not_found(self):
        update_data = OrganizationMainData(name="Jane Doe")
        response = self.client.put(
            "/update/organization/non-existent-id", json=update_data.model_dump(exclude_unset=True)
        )
        assert response.status_code == 404

    def test_delete_organization_permission_denied(self):
        create_data = OrganizationMainData(name="Test Corp")
        response = self.client.post("/create/organization", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        created_organization = response.json()
        organization_id = created_organization["_id"]

        response = self.no_roles_client.delete(f"/delete/entity/{organization_id}")
        assert response.status_code == 403

    def test_delete_organization_not_found(self):
        response = self.client.delete("/delete/entity/non-existent-id")
        assert response.status_code == 404

    @patch("omni_osint_crud.routers.create.dal.create_organization")
    def test_create_organization_internal_error(self, mock_create_organization):
        mock_create_organization.side_effect = Exception("DB error")
        create_data = OrganizationMainData(name="Test Corp")
        response = self.client.post("/create/organization", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 500

    @patch("omni_osint_crud.routers.read.dal.get_organization")
    def test_read_organization_internal_error(self, mock_read_organization):
        mock_read_organization.side_effect = Exception("DB error")
        response = self.client.get("/read/organization/some-id")
        assert response.status_code == 500

    @patch("omni_osint_crud.routers.update.dal.update_organization")
    def test_update_organization_internal_error(self, mock_update_organization):
        mock_update_organization.side_effect = Exception("DB error")
        update_data = OrganizationMainData(name="Jane Doe")
        response = self.client.put("/update/organization/some-id", json=update_data.model_dump(exclude_unset=True))
        assert response.status_code == 500

    @patch("omni_osint_crud.routers.delete.dal.delete_entity")
    def test_delete_organization_internal_error(self, mock_delete_entity):
        mock_delete_entity.side_effect = Exception("DB error")
        response = self.client.delete("/delete/entity/some-id")
        assert response.status_code == 500

    def test_update_organization_permissions_not_found(self):
        update_data = {"owner": "new-owner"}
        response = self.client.put("/update/organization/non-existent-id/permissions", json=update_data)
        assert response.status_code == 404

    def test_update_organization_permissions_permission_denied(self):
        # 1. Create an organization with the admin client
        create_data = OrganizationMainData(name="Test Organization")
        response = self.client.post("/create/organization", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        created_organization = response.json()
        organization_id = created_organization["_id"]

        # 2. Grant the user_client read access
        permission_data = {"read": ["test-user-id-789"]}
        response = self.client.put(f"/update/organization/{organization_id}/permissions", json=permission_data)
        assert response.status_code == 200

        # 3. Attempt to update permissions with the user_client (non-owner)
        update_data = {"owner": "new-owner"}
        response = self.user_client.put(f"/update/organization/{organization_id}/permissions", json=update_data)
        assert response.status_code == 403

    @patch("omni_osint_crud.routers.update.dal.update_organization")
    def test_update_organization_permissions_internal_error(self, mock_update_organization):
        mock_update_organization.side_effect = Exception("DB error")
        update_data = {"owner": "new-owner"}
        response = self.client.put("/update/organization/some-id/permissions", json=update_data)
        assert response.status_code == 500
