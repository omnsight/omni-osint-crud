
import jwt
from fastapi.testclient import TestClient

from omni_python_library import init_omni_library
from omni_python_library.models.osint import WebsiteMainData
from omni_python_library.utils.user import UserRole
from omni_osint_crud.main import app


class TestWebsite:
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

    def test_website_crud_cycle(self):
        # 1. Create Website
        create_data = WebsiteMainData(title="Test Website", url="http://test.com")
        response = self.client.post("/create/website", json=create_data.model_dump())
        assert response.status_code == 200
        created_website = response.json()
        website_id = created_website["_id"]
        assert website_id
        assert created_website["title"] == "Test Website"

        # 2. Read Website
        response = self.client.get(f"/read/website/{website_id}")
        assert response.status_code == 200
        assert response.json() == created_website

        # 3. Update Website
        update_data = WebsiteMainData(title="Test Website Updated", url="http://test-updated.com")  
        response = self.client.put(f"/update/website/{website_id}", json=update_data.model_dump())
        assert response.status_code == 200
        updated_website = response.json()
        assert updated_website["title"] == "Test Website Updated"

        # 4. Delete Website
        response = self.client.delete(f"/delete/entity/{website_id}")
        assert response.status_code == 200

        # 5. Verify Deletion
        response = self.client.get(f"/read/website/{website_id}")
        assert response.status_code == 404

    def test_read_website_not_found(self):
        response = self.client.get("/read/website/non-existent-id")
        assert response.status_code == 404

    def test_update_website_not_found(self):
        update_data = WebsiteMainData(name="Jane Doe", url="http://jane.com")
        response = self.client.put("/update/website/non-existent-id", json=update_data.model_dump())
        assert response.status_code == 404

    def test_delete_website_not_found(self):
        response = self.client.delete("/delete/entity/non-existent-id")
        assert response.status_code == 404
