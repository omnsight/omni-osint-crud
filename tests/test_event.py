from unittest.mock import patch

import jwt
from fastapi.testclient import TestClient
from omni_python_library import init_omni_library
from omni_python_library.models.osint import EventMainData
from omni_python_library.utils.config import UserRole

from omni_osint_crud.main import app


class TestEvent:
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

    def test_event_crud_cycle(self):
        # 1. Create Event
        create_data = EventMainData(title="Test Event")
        response = self.client.post("/create/event", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        created_event = response.json()
        event_id = created_event["_id"]
        assert event_id
        assert created_event["title"] == "Test Event"

        # 2. Read Event
        response = self.client.get(f"/read/event/{event_id}")
        assert response.status_code == 200
        assert response.json() == created_event

        # 3. Update Event
        update_data = EventMainData(title="Test Event Updated")
        response = self.client.put(f"/update/event/{event_id}", json=update_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        updated_event = response.json()
        assert updated_event["title"] == "Test Event Updated"

        # 4. Delete Event
        response = self.client.delete(f"/delete/entity/{event_id}")
        assert response.status_code == 200

        # 5. Verify Deletion
        response = self.client.get(f"/read/event/{event_id}")
        assert response.status_code == 404

    def test_create_event_permission_denied(self):
        create_data = EventMainData(title="Test Event")
        response = self.no_roles_client.post("/create/event", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 403

    def test_read_event_not_found(self):
        response = self.client.get("/read/event/non-existent-id")
        assert response.status_code == 404

    def test_read_event_bad_id(self):
        response = self.client.get("/read/event/bad_collection/bad_key")
        assert response.status_code == 404

    def test_update_event_permission_denied(self):
        create_data = EventMainData(title="Test Event")
        response = self.client.post("/create/event", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        created_event = response.json()
        event_id = created_event["_id"]

        update_data = EventMainData(title="Jane Doe")
        response = self.no_roles_client.put(
            f"/update/event/{event_id}", json=update_data.model_dump(exclude_unset=True)
        )
        assert response.status_code == 403

    def test_update_event_not_found(self):
        update_data = EventMainData(title="Jane Doe")
        response = self.client.put("/update/event/non-existent-id", json=update_data.model_dump(exclude_unset=True))
        assert response.status_code == 404

    def test_delete_event_permission_denied(self):
        create_data = EventMainData(title="Test Event")
        response = self.client.post("/create/event", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        created_event = response.json()
        event_id = created_event["_id"]

        response = self.no_roles_client.delete(f"/delete/entity/{event_id}")
        assert response.status_code == 403

    def test_delete_event_not_found(self):
        response = self.client.delete("/delete/entity/non-existent-id")
        assert response.status_code == 404

    @patch("omni_osint_crud.routers.create.dal.create_event")
    def test_create_event_internal_error(self, mock_create_event):
        mock_create_event.side_effect = Exception("DB error")
        create_data = EventMainData(title="Test Event")
        response = self.client.post("/create/event", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 500

    @patch("omni_osint_crud.routers.read.dal.get_event")
    def test_read_event_internal_error(self, mock_read_event):
        mock_read_event.side_effect = Exception("DB error")
        response = self.client.get("/read/event/some-id")
        assert response.status_code == 500

    @patch("omni_osint_crud.routers.update.dal.update_event")
    def test_update_event_internal_error(self, mock_update_event):
        mock_update_event.side_effect = Exception("DB error")
        update_data = EventMainData(title="Jane Doe")
        response = self.client.put("/update/event/some-id", json=update_data.model_dump(exclude_unset=True))
        assert response.status_code == 500

    @patch("omni_osint_crud.routers.delete.dal.delete_entity")
    def test_delete_event_internal_error(self, mock_delete_entity):
        mock_delete_entity.side_effect = Exception("DB error")
        response = self.client.delete("/delete/entity/some-id")
        assert response.status_code == 500

    def test_update_event_permissions_not_found(self):
        update_data = {"owner": "new-owner"}
        response = self.client.put("/update/event/non-existent-id/permissions", json=update_data)
        assert response.status_code == 404

    def test_update_event_permissions_permission_denied(self):
        # 1. Create an event with the admin client
        create_data = EventMainData(title="Test Event")
        response = self.client.post("/create/event", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        created_event = response.json()
        event_id = created_event["_id"]

        # 2. Grant the user_client read access
        permission_data = {"read": ["test-user-id-789"]}
        response = self.client.put(f"/update/event/{event_id}/permissions", json=permission_data)
        assert response.status_code == 200

        # 3. Attempt to update permissions with the user_client (non-owner)
        update_data = {"owner": "new-owner"}
        response = self.user_client.put(f"/update/event/{event_id}/permissions", json=update_data)
        assert response.status_code == 403

    @patch("omni_osint_crud.routers.update.dal.update_event")
    def test_update_event_permissions_internal_error(self, mock_update_event):
        mock_update_event.side_effect = Exception("DB error")
        update_data = {"owner": "new-owner"}
        response = self.client.put("/update/event/some-id/permissions", json=update_data)
        assert response.status_code == 500
