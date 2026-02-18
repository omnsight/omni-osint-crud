
import jwt
from fastapi.testclient import TestClient

from omni_python_library import init_omni_library
from omni_python_library.models.osint import (
    PersonMainData,
    OrganizationMainData,
    RelationMainData,
)
from omni_python_library.utils.user import UserRole
from omni_osint_crud.main import app


class TestRelation:
    client: TestClient

    @classmethod
    def setup_class(cls):
        init_omni_library()
        payload = {
            "sub": "test-user-id-123",
            "roles": [UserRole.ADMIN],
        }
        token = jwt.encode(payload, key=None, algorithm="none")
        cls.client = TestClient(app)
        cls.client.headers = {"Authorization": f"Bearer {token}"}

    def test_relation_crud_cycle(self):
        # 1. Create a Person and an Organization to connect
        person_data = PersonMainData(name="Test Person for Relation")
        person_res = self.client.post("/create/person", json=person_data.model_dump())
        assert person_res.status_code == 200
        person = person_res.json()
        person_id = person["_id"]

        org_data = OrganizationMainData(name="Test Org for Relation")
        org_res = self.client.post(
            "/create/organization", json=org_data.model_dump()
        )
        assert org_res.status_code == 200
        organization = org_res.json()
        organization_id = organization["_id"]

        # 2. Create Relation
        create_data = RelationMainData(
            from_id=person_id, to_id=organization_id, type="works_at"
        )
        response = self.client.post("/create/relation", json=create_data.model_dump())
        assert response.status_code == 200
        created_relation = response.json()
        relation_id = created_relation["_id"]
        assert relation_id
        assert created_relation["_from"] == person_id
        assert created_relation["_to"] == organization_id
        assert created_relation["type"] == "works_at"

        # 3. Read Relation
        response = self.client.get(f"/read/relation/{relation_id}")
        assert response.status_code == 200
        assert response.json() == created_relation

        # 4. Update Relation
        update_data = RelationMainData(
            from_id=person_id, to_id=organization_id, type="worked_at"
        )
        response = self.client.put(
            f"/update/relation/{relation_id}", json=update_data.model_dump()
        )
        assert response.status_code == 200
        updated_relation = response.json()
        assert updated_relation["type"] == "worked_at"

        # 5. Delete Relation
        response = self.client.delete(f"/delete/entity/{relation_id}")
        assert response.status_code == 200

        # 6. Verify Deletion
        response = self.client.get(f"/read/relation/{relation_id}")
        assert response.status_code == 404

        # 7. Cleanup
        self.client.delete(f"/delete/entity/{person_id}")
        self.client.delete(f"/delete/entity/{organization_id}")

    def test_read_relation_not_found(self):
        response = self.client.get("/read/relation/non-existent-id")
        assert response.status_code == 404

    def test_update_relation_not_found(self):
        update_data = RelationMainData(from_id="a", to_id="b", type="c")
        response = self.client.put(
            "/update/relation/non-existent-id", json=update_data.model_dump()
        )
        assert response.status_code == 404

    def test_delete_relation_not_found(self):
        response = self.client.delete("/delete/entity/non-existent-id")
        assert response.status_code == 404

    def test_create_relation_bad_parameters(self):
        # Missing to_id
        create_data = RelationMainData(from_id="some_id", type="works_at")
        response = self.client.post("/create/relation", json=create_data.model_dump())
        assert response.status_code == 400

        # Missing from_id
        create_data = RelationMainData(to_id="some_id", type="works_at")
        response = self.client.post("/create/relation", json=create_data.model_dump())
        assert response.status_code == 400

        # Both missing
        create_data = RelationMainData(type="works_at")
        response = self.client.post("/create/relation", json=create_data.model_dump())
        assert response.status_code == 400
