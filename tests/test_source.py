
import jwt
from fastapi.testclient import TestClient

from omni_python_library import init_omni_library
from omni_python_library.models.osint import SourceMainData
from omni_python_library.utils.user import UserRole
from omni_osint_crud.main import app


class TestSource:
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

    def test_read_source_not_found(self):
        response = self.client.get("/read/source/non-existent-id")
        assert response.status_code == 404

    def test_update_source_not_found(self):
        update_data = SourceMainData(name="Jane Doe", url="http://jane.com")
        response = self.client.put("/update/source/non-existent-id", json=update_data.model_dump())
        assert response.status_code == 404

    def test_delete_source_not_found(self):
        response = self.client.delete("/delete/entity/non-existent-id")
        assert response.status_code == 404
