
import jwt
from fastapi.testclient import TestClient

from omni_python_library import init_omni_library
from omni_python_library.models.osint import PersonMainData
from omni_python_library.utils.user import UserRole
from omni_osint_crud.main import app


class TestPerson:
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

    def test_person_crud_cycle(self):
        # 1. Create Person
        create_data = PersonMainData(name="John Doe")
        response = self.client.post("/create/person", json=create_data.model_dump())
        assert response.status_code == 200
        created_person = response.json()
        person_id = created_person["_id"]
        assert person_id
        assert created_person["name"] == "John Doe"

        # 2. Read Person
        response = self.client.get(f"/read/person/{person_id}")
        assert response.status_code == 200
        assert response.json() == created_person

        # 3. Update Person
        update_data = PersonMainData(name="John Doe Updated")
        response = self.client.put(f"/update/person/{person_id}", json=update_data.model_dump())
        assert response.status_code == 200
        updated_person = response.json()
        assert updated_person["name"] == "John Doe Updated"

        # 4. Delete Person
        response = self.client.delete(f"/delete/entity/{person_id}")
        assert response.status_code == 200

        # 5. Verify Deletion
        response = self.client.get(f"/read/person/{person_id}")
        assert response.status_code == 404

    def test_read_person_not_found(self):
        response = self.client.get("/read/person/non-existent-id")
        assert response.status_code == 404

    def test_update_person_not_found(self):
        update_data = PersonMainData(name="Jane Doe")
        response = self.client.put("/update/person/non-existent-id", json=update_data.model_dump())
        assert response.status_code == 404

    def test_delete_person_not_found(self):
        response = self.client.delete("/delete/entity/non-existent-id")
        assert response.status_code == 404
