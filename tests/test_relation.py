from unittest.mock import patch

import jwt
from fastapi.testclient import TestClient
from omni_python_library import init_omni_library
from omni_python_library.models.osint import (
    OrganizationMainData,
    PersonMainData,
    RelationMainData,
)
from omni_python_library.utils.config.user import UserRole

from omni_osint_crud.main import app


class TestRelation:
    client: TestClient
    no_roles_client: TestClient
    user_client: TestClient

    @classmethod
    def setup_class(cls):
        init_omni_library()
        # Client with admin roles
        payload = {
            "sub": "test-user-id-123",
            "roles": [UserRole.ADMIN],
        }
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

    ######################################################################################################
    # Overall Flow
    ######################################################################################################

    def test_relation_crud_cycle(self):
        # 1. Create a Person and an Organization to connect
        person_data = PersonMainData(name="Test Person for Relation")
        person_res = self.client.post("/person", json=person_data.model_dump(exclude_unset=True))
        assert person_res.status_code == 200
        person = person_res.json()
        person_id = person["_id"]

        org_data = OrganizationMainData(name="Test Org for Relation")
        org_res = self.client.post("/organization", json=org_data.model_dump(exclude_unset=True))
        assert org_res.status_code == 200
        organization = org_res.json()
        organization_id = organization["_id"]

        # 2. Create Relation
        create_data = RelationMainData(from_id=person_id, to_id=organization_id, name="works_at")
        response = self.client.post("/relation", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        created_relation = response.json()
        relation_id = created_relation["_id"]
        assert relation_id
        assert created_relation["_from"] == person_id
        assert created_relation["_to"] == organization_id
        assert created_relation["name"] == "works_at"

        # 3. Read Relation
        response = self.client.get(f"/relation/{relation_id}")
        assert response.status_code == 200
        assert response.json() == created_relation

        # 4. Update Relation
        update_data = RelationMainData(from_id=person_id, to_id=organization_id, name="worked_at")
        response = self.client.put(f"/relation/{relation_id}", json=update_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        updated_relation = response.json()
        assert updated_relation["name"] == "worked_at"

        # 5. Delete Relation
        response = self.client.delete(f"/relation/{relation_id}")
        assert response.status_code == 200

        # 6. Verify Deletion
        response = self.client.get(f"/relation/{relation_id}")
        assert response.status_code == 404

        # 7. Cleanup
        self.client.delete(f"/entity/{person_id}")
        self.client.delete(f"/entity/{organization_id}")

    ######################################################################################################
    # Test Creates
    ######################################################################################################

    def test_create_relation_missing_parameters(self):
        # Missing to_id
        create_data = RelationMainData(from_id="some_id", name="works_at")
        response = self.client.post("/relation", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 400

        # Missing from_id
        create_data = RelationMainData(to_id="some_id", name="works_at")
        response = self.client.post("/relation", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 400

        # Both missing
        create_data = RelationMainData(name="works_at")
        response = self.client.post("/relation", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 400

    def test_create_relation_invalid_name(self):
        # Name is None
        create_data = RelationMainData(from_id="a", to_id="b", name=None)
        response = self.client.post("/relation", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 400

        # Name is empty
        create_data = RelationMainData(from_id="a", to_id="b", name="")
        response = self.client.post("/relation", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 400

        # Name is not ASCII
        create_data = RelationMainData(from_id="a", to_id="b", name="relation-with-non-ascii-©")
        response = self.client.post("/relation", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 400

    def test_create_relation_permission_denied(self):
        create_data = RelationMainData(from_id="a", to_id="b", name="c")
        response = self.no_roles_client.post("/relation", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 403

    @patch("omni_osint_crud.routers.create.dal.create_relation")
    def test_create_relation_internal_error(self, mock_create_relation):
        mock_create_relation.side_effect = Exception("DB error")
        create_data = RelationMainData(from_id="a", to_id="b", name="c")
        response = self.client.post("/relation", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 500

    ######################################################################################################
    # Test Reads
    ######################################################################################################

    def test_read_relation_not_found(self):
        response = self.client.get("/relation/relations/non-existent-id")
        assert response.status_code == 404

    def test_read_relation_not_found_bad_id(self):
        response = self.client.get("/relation/bad_collection/bad_key")
        assert response.status_code == 404

    def test_read_relation_permission_denied(self):
        person_data = PersonMainData(name="Test Person for Relation")
        person_res = self.client.post("/person", json=person_data.model_dump(exclude_unset=True))
        assert person_res.status_code == 200
        person = person_res.json()
        person_id = person["_id"]

        org_data = OrganizationMainData(name="Test Org for Relation")
        org_res = self.client.post("/organization", json=org_data.model_dump(exclude_unset=True))
        assert org_res.status_code == 200
        organization = org_res.json()
        organization_id = organization["_id"]

        create_data = RelationMainData(from_id=person_id, to_id=organization_id, name="works_at")
        response = self.client.post("/relation", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        created_relation = response.json()
        relation_id = created_relation["_id"]

        response = self.no_roles_client.get(f"/relation/{relation_id}")
        assert response.status_code == 403

    @patch("omni_osint_crud.routers.read.dal.get_relation")
    def test_read_relation_internal_error(self, mock_read_relation):
        mock_read_relation.side_effect = Exception("DB error")
        response = self.client.get("/relation/relations/some-id")
        assert response.status_code == 500

    ######################################################################################################
    # Test Updates
    ######################################################################################################

    # Test update_relation

    def test_update_relation_not_found(self):
        update_data = RelationMainData(from_id="a", to_id="b", name="c")
        response = self.client.put(
            "/relation/relations/non-existent-id", json=update_data.model_dump(exclude_unset=True)
        )
        assert response.status_code == 404

    def test_update_relation_invalid_name(self):
        # 1. Create a Person and an Organization to connect
        person_data = PersonMainData(name="Test Person for Relation")
        person_res = self.client.post("/person", json=person_data.model_dump(exclude_unset=True))
        assert person_res.status_code == 200
        person = person_res.json()
        person_id = person["_id"]

        org_data = OrganizationMainData(name="Test Org for Relation")
        org_res = self.client.post("/organization", json=org_data.model_dump(exclude_unset=True))
        assert org_res.status_code == 200
        organization = org_res.json()
        organization_id = organization["_id"]

        # 2. Create Relation
        create_data = RelationMainData(from_id=person_id, to_id=organization_id, name="works_at")
        response = self.client.post("/relation", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        created_relation = response.json()
        relation_id = created_relation["_id"]

        # 3. Update with empty name
        update_data = {"name": ""}
        response = self.client.put(f"/relation/{relation_id}", json=update_data)
        assert response.status_code == 400

        # 4. Update with non-ASCII name
        update_data = {"name": "relation-with-non-ascii-©"}
        response = self.client.put(f"/relation/{relation_id}", json=update_data)
        assert response.status_code == 400

        # 5. Cleanup
        self.client.delete(f"/entity/{person_id}")
        self.client.delete(f"/entity/{organization_id}")
        self.client.delete(f"/relation/{relation_id}")

    def test_update_relation_permission_denied(self):
        person_data = PersonMainData(name="Test Person for Relation")
        person_res = self.client.post("/person", json=person_data.model_dump(exclude_unset=True))
        assert person_res.status_code == 200
        person = person_res.json()
        person_id = person["_id"]

        org_data = OrganizationMainData(name="Test Org for Relation")
        org_res = self.client.post("/organization", json=org_data.model_dump(exclude_unset=True))
        assert org_res.status_code == 200
        organization = org_res.json()
        organization_id = organization["_id"]

        create_data = RelationMainData(from_id=person_id, to_id=organization_id, name="works_at")
        response = self.client.post("/relation", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        created_relation = response.json()
        relation_id = created_relation["_id"]

        update_data = RelationMainData(from_id="a", to_id="b", name="c")
        response = self.no_roles_client.put(f"/relation/{relation_id}", json=update_data.model_dump(exclude_unset=True))
        assert response.status_code == 403

    @patch("omni_osint_crud.routers.update.dal.update_relation")
    def test_update_relation_internal_error(self, mock_update_relation):
        mock_update_relation.side_effect = Exception("DB error")
        update_data = RelationMainData(from_id="a", to_id="b", name="c")
        response = self.client.put("/relation/relations/some-id", json=update_data.model_dump(exclude_unset=True))
        assert response.status_code == 500

    # Test update_relation_permissions

    def test_update_relation_permissions_not_found(self):
        update_data = {"owner": "new-owner"}
        response = self.client.put("/relation/relations/non-existent-id/permissions", json=update_data)
        assert response.status_code == 404

    def test_update_relation_permissions_permission_denied(self):
        # 1. Create a relation with the admin client
        person_data = PersonMainData(name="Test Person for Relation")
        person_res = self.client.post("/person", json=person_data.model_dump(exclude_unset=True))
        person = person_res.json()
        person_id = person["_id"]

        org_data = OrganizationMainData(name="Test Org for Relation")
        org_res = self.client.post("/organization", json=org_data.model_dump(exclude_unset=True))
        organization = org_res.json()
        organization_id = organization["_id"]

        create_data = RelationMainData(from_id=person_id, to_id=organization_id, name="works_at")
        response = self.client.post("/relation", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        created_relation = response.json()
        relation_id = created_relation["_id"]

        # 2. Grant the user_client read access
        permission_data = {"read": ["test-user-id-789"]}
        response = self.client.put(f"/relation/{relation_id}/permissions", json=permission_data)
        assert response.status_code == 200

        # 3. Attempt to update permissions with the user_client (non-owner)
        update_data = {"owner": "new-owner"}
        response = self.user_client.put(f"/relation/{relation_id}/permissions", json=update_data)
        assert response.status_code == 403

    @patch("omni_osint_crud.routers.update.dal.update_relation")
    def test_update_relation_permissions_internal_error(self, mock_update_relation):
        mock_update_relation.side_effect = Exception("DB error")
        update_data = {"owner": "new-owner"}
        response = self.client.put("/relation/relations/some-id/permissions", json=update_data)
        assert response.status_code == 500

    ######################################################################################################
    # Test Deletes
    ######################################################################################################

    def test_delete_relation_not_found(self):
        response = self.client.delete("/relation/relations/non-existent-id")
        assert response.status_code == 404

    def test_delete_relation_permission_denied(self):
        person_data = PersonMainData(name="Test Person for Relation")
        person_res = self.client.post("/person", json=person_data.model_dump(exclude_unset=True))
        assert person_res.status_code == 200
        person = person_res.json()
        person_id = person["_id"]

        org_data = OrganizationMainData(name="Test Org for Relation")
        org_res = self.client.post("/organization", json=org_data.model_dump(exclude_unset=True))
        assert org_res.status_code == 200
        organization = org_res.json()
        organization_id = organization["_id"]

        create_data = RelationMainData(from_id=person_id, to_id=organization_id, name="works_at")
        response = self.client.post("/relation", json=create_data.model_dump(exclude_unset=True))
        assert response.status_code == 200
        created_relation = response.json()
        relation_id = created_relation["_id"]

        response = self.no_roles_client.delete(f"/relation/{relation_id}")
        assert response.status_code == 403

    @patch("omni_osint_crud.routers.delete.dal.delete_relation")
    def test_delete_relation_internal_error(self, mock_delete_relation):
        mock_delete_relation.side_effect = Exception("DB error")
        response = self.client.delete("/relation/relations/some-id")
        assert response.status_code == 500
