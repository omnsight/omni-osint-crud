
import jwt
from fastapi.testclient import TestClient
from unittest.mock import patch
from omni_python_library import init_omni_library
from omni_python_library.models.osint import SourceMainData
from omni_python_library.utils.user import UserRole
from src.omni_osint_crud.main import app


class TestSource:
    client: TestClient
    no_roles_client: TestClient

    @classmethod
    def setup_class(cls):
        init_omni_library()
        # Client with admin roles
        payload = {
            "sub": "test-user-id-123",
            "roles": [UserRole.ADMIN]
        }
        token = jwt.encode(payload, key=None, algorithm="none")
        cls.client = TestClient(app)
        cls.client.headers = {"Authorization": f"Bearer {token}"}

        # Client with no roles
        no_roles_payload = {
            "sub": "test-user-id-456",
            "roles": []
        }
        no_roles_token = jwt.encode(no_roles_payload, key=None, algorithm="none")
        cls.no_roles_client = TestClient(app)
        cls.no_roles_client.headers = {"Authorization": f"Bearer {no_roles_token}"}

    def test_source_crud_cycle(self):
        # 1. Create Source
        create_data = SourceMainData(name="Test Source", url="http://source.com")
        response = self.client.post("/create/source", json=create_data.model_dump())
        assert response.status_code == 200
        created_source = response.json()
        source_id = created_source["_id"]
        assert source_id
        assert created_source["name"] == "Test Source"

        # 2. Read Source
        response = self.client.get(f"/read/source/{source_id}")
        assert response.status_code == 200
        assert response.json() == created_source

        # 3. Update Source
        update_data = SourceMainData(name="Test Source Updated", url="http://source-updated.com")
        response = self.client.put(f"/update/source/{source_id}", json=update_data.model_dump())
        assert response.status_code == 200
        updated_source = response.json()
        assert updated_source["name"] == "Test Source Updated"

        # 4. Delete Source
        response = self.client.delete(f"/delete/entity/{source_id}")
        assert response.status_code == 200

        # 5. Verify Deletion
        response = self.client.get(f"/read/source/{source_id}")
        assert response.status_code == 404

    def test_create_source_permission_denied(self):
        create_data = SourceMainData(name="Test Source", url="http://source.com")
        response = self.no_roles_client.post("/create/source", json=create_data.model_dump())
        assert response.status_code == 403

    def test_read_source_not_found(self):
        response = self.client.get("/read/source/non-existent-id")
        assert response.status_code == 404

    def test_read_source_bad_id(self):
        response = self.client.get("/read/source/bad_collection/bad_key")
        assert response.status_code == 404

    def test_update_source_permission_denied(self):
        create_data = SourceMainData(name="Test Source", url="http://source.com")
        response = self.client.post("/create/source", json=create_data.model_dump())
        assert response.status_code == 200
        created_source = response.json()
        source_id = created_source["_id"]

        update_data = SourceMainData(name="Jane Doe", url="http://jane.com")
        response = self.no_roles_client.put(f"/update/source/{source_id}", json=update_data.model_dump())
        assert response.status_code == 403

    def test_update_source_not_found(self):
        update_data = SourceMainData(name="Jane Doe", url="http://jane.com")
        response = self.client.put("/update/source/non-existent-id", json=update_data.model_dump())
        assert response.status_code == 404

    def test_delete_source_permission_denied(self):
        create_data = SourceMainData(name="Test Source", url="http://source.com")
        response = self.client.post("/create/source", json=create_data.model_dump())
        assert response.status_code == 200
        created_source = response.json()
        source_id = created_source["_id"]

        response = self.no_roles_client.delete(f"/delete/entity/{source_id}")
        assert response.status_code == 403

    def test_delete_source_not_found(self):
        response = self.client.delete("/delete/entity/non-existent-id")
        assert response.status_code == 404

    @patch("omni_osint_crud.routers.create.dal.create_source")
    def test_create_source_internal_error(self, mock_create_source):
        mock_create_source.side_effect = Exception("DB error")
        create_data = SourceMainData(name="Test Source", url="http://source.com")
        response = self.client.post("/create/source", json=create_data.model_dump())
        assert response.status_code == 500

    @patch("omni_osint_crud.routers.read.dal.get_source")
    def test_read_source_internal_error(self, mock_read_source):
        mock_read_source.side_effect = Exception("DB error")
        response = self.client.get("/read/source/some-id")
        assert response.status_code == 500

    @patch("omni_osint_crud.routers.update.dal.update_source")
    def test_update_source_internal_error(self, mock_update_source):
        mock_update_source.side_effect = Exception("DB error")
        update_data = SourceMainData(name="Jane Doe", url="http://jane.com")
        response = self.client.put("/update/source/some-id", json=update_data.model_dump())
        assert response.status_code == 500

    @patch("omni_osint_crud.routers.delete.dal.delete_entity")
    def test_delete_source_internal_error(self, mock_delete_entity):
        mock_delete_entity.side_effect = Exception("DB error")
        response = self.client.delete("/delete/entity/some-id")
        assert response.status_code == 500
