
import jwt
from fastapi.testclient import TestClient

from omni_python_library import init_omni_library
from omni_python_library.models.osint import EventMainData
from omni_python_library.utils.user import UserRole
from omni_osint_crud.main import app


class TestEvent:
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

    def test_event_crud_cycle(self):
        # 1. Create Event
        create_data = EventMainData(title="Test Event")
        response = self.client.post("/create/event", json=create_data.model_dump())
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
        response = self.client.put(f"/update/event/{event_id}", json=update_data.model_dump())
        assert response.status_code == 200
        updated_event = response.json()
        assert updated_event["title"] == "Test Event Updated"

        # 4. Delete Event
        response = self.client.delete(f"/delete/entity/{event_id}")
        assert response.status_code == 200

        # 5. Verify Deletion
        response = self.client.get(f"/read/event/{event_id}")
        assert response.status_code == 404

    def test_read_event_not_found(self):
        response = self.client.get("/read/event/non-existent-id")
        assert response.status_code == 404

    def test_update_event_not_found(self):
        update_data = EventMainData(name="Jane Doe")
        response = self.client.put("/update/event/non-existent-id", json=update_data.model_dump())
        assert response.status_code == 404

    def test_delete_event_not_found(self):
        response = self.client.delete("/delete/entity/non-existent-id")
        assert response.status_code == 404
