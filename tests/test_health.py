from fastapi.testclient import TestClient
from src.omni_osint_crud.main import app


class TestHealth:
    client: TestClient

    @classmethod
    def setup_class(cls):
        cls.client = TestClient(app)

    def test_health_check(self):
        response = self.client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
