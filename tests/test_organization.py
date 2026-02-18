
import jwt
from fastapi.testclient import TestClient

from omni_python_library import init_omni_library
from omni_python_library.models.osint import OrganizationMainData
from omni_python_library.utils.user import UserRole
from omni_osint_crud.main import app


class TestOrganization:
    client: TestClient

    @classmethod
    def setup_class(cls):
        init_omni_library()
        payload = {
            "sub": "test-user-id-123",
            "roles": [UserRole.ADMIN]
        }
        token = jwt.encode(payload, key=None, algorithm="none")
        cls.client = TestClient(app)
        cls.client.headers = {"Authorization": f"Bearer {token}"}

    def test_organization_crud_cycle(self):
        # 1. Create Organization
        create_data = OrganizationMainData(name="Test Corp")
        response = self.client.post("/create/organization", json=create_data.model_dump())
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
        response = self.client.put(f"/update/organization/{organization_id}", json=update_data.model_dump())
        assert response.status_code == 200
        updated_organization = response.json()
        assert updated_organization["name"] == "Test Corp Updated"

        # 4. Delete Organization
        response = self.client.delete(f"/delete/entity/{organization_id}")
        assert response.status_code == 200

        # 5. Verify Deletion
        response = self.client.get(f"/read/organization/{organization_id}")
        assert response.status_code == 404

    def test_read_organization_not_found(self):
        response = self.client.get("/read/organization/non-existent-id")
        assert response.status_code == 404

    def test_update_organization_not_found(self):
        update_data = OrganizationMainData(name="Jane Doe")
        response = self.client.put("/update/organization/non-existent-id", json=update_data.model_dump())
        assert response.status_code == 404

    def test_delete_organization_not_found(self):
        response = self.client.delete("/delete/entity/non-existent-id")
        assert response.status_code == 404
