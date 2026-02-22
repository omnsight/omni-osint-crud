from unittest.mock import patch

import jwt
from fastapi.testclient import TestClient
from omni_python_library import init_omni_library
from omni_python_library.models.osint import PersonMainData
from omni_python_library.utils.config import UserRole

from omni_osint_crud.main import app


class TestPerson:
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

    def test_person_crud_cycle(self):
        # 1. Create Person
        create_data = PersonMainData(name="John Doe")
        response = self.client.post("/create/person", json=create_data.model_dump(exclude_unset=True))
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
        response = self.client.put(f"/update/person/{person_id}", json=update_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        updated_person = response.json()
        assert updated_person["name"] == "John Doe Updated"

        # 4. Delete Person
        response = self.client.delete(f"/delete/entity/{person_id}")
        assert response.status_code == 200

        # 5. Verify Deletion
        response = self.client.get(f"/read/person/{person_id}")
        assert response.status_code == 404

    def test_create_person_permission_denied(self):
        create_data = PersonMainData(name="John Doe")
        response = self.no_roles_client.post("/create/person", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 403

    def test_read_person_not_found(self):
        response = self.client.get("/read/person/non-existent-id")
        assert response.status_code == 404

    def test_read_person_bad_id(self):
        response = self.client.get("/read/person/bad_collection/bad_key")
        assert response.status_code == 404

    def test_update_person_permission_denied(self):
        create_data = PersonMainData(name="John Doe")
        response = self.client.post("/create/person", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        created_person = response.json()
        person_id = created_person["_id"]

        update_data = PersonMainData(name="Jane Doe")
        response = self.no_roles_client.put(
            f"/update/person/{person_id}", json=update_data.model_dump(exclude_unset=True)
        )
        assert response.status_code == 403

    def test_update_person_not_found(self):
        update_data = PersonMainData(name="Jane Doe")
        response = self.client.put("/update/person/non-existent-id", json=update_data.model_dump(exclude_unset=True))
        assert response.status_code == 404

    def test_delete_person_permission_denied(self):
        create_data = PersonMainData(name="John Doe")
        response = self.client.post("/create/person", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        created_person = response.json()
        person_id = created_person["_id"]

        response = self.no_roles_client.delete(f"/delete/entity/{person_id}")
        assert response.status_code == 403

    def test_delete_person_not_found(self):
        response = self.client.delete("/delete/entity/non-existent-id")
        assert response.status_code == 404

    @patch("omni_osint_crud.routers.create.dal.create_person")
    def test_create_person_internal_error(self, mock_create_person):
        mock_create_person.side_effect = Exception("DB error")
        create_data = PersonMainData(name="John Doe")
        response = self.client.post("/create/person", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 500

    @patch("omni_osint_crud.routers.read.dal.get_person")
    def test_read_person_internal_error(self, mock_read_person):
        mock_read_person.side_effect = Exception("DB error")
        response = self.client.get("/read/person/some-id")
        assert response.status_code == 500

    @patch("omni_osint_crud.routers.update.dal.update_person")
    def test_update_person_internal_error(self, mock_update_person):
        mock_update_person.side_effect = Exception("DB error")
        update_data = PersonMainData(name="Jane Doe")
        response = self.client.put("/update/person/some-id", json=update_data.model_dump(exclude_unset=True))
        assert response.status_code == 500

    @patch("omni_osint_crud.routers.delete.dal.delete_entity")
    def test_delete_person_internal_error(self, mock_delete_entity):
        mock_delete_entity.side_effect = Exception("DB error")
        response = self.client.delete("/delete/entity/some-id")
        assert response.status_code == 500

    def test_update_person_permissions_not_found(self):
        update_data = {"owner": "new-owner"}
        response = self.client.put("/update/person/non-existent-id/permissions", json=update_data)
        assert response.status_code == 404

    def test_update_person_permissions_permission_denied(self):
        # 1. Create a person with the admin client
        create_data = PersonMainData(name="Test Person")
        response = self.client.post("/create/person", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        created_person = response.json()
        person_id = created_person["_id"]

        # 2. Grant the user_client read access
        permission_data = {"read": ["test-user-id-789"]}
        response = self.client.put(f"/update/person/{person_id}/permissions", json=permission_data)
        assert response.status_code == 200

        # 3. Attempt to update permissions with the user_client (non-owner)
        update_data = {"owner": "new-owner"}
        response = self.user_client.put(f"/update/person/{person_id}/permissions", json=update_data)
        assert response.status_code == 403

    @patch("omni_osint_crud.routers.update.dal.update_person")
    def test_update_person_permissions_internal_error(self, mock_update_person):
        mock_update_person.side_effect = Exception("DB error")
        update_data = {"owner": "new-owner"}
        response = self.client.put("/update/person/some-id/permissions", json=update_data)
        assert response.status_code == 500
