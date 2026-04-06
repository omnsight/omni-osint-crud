import logging
from typing import Dict

from fastapi import APIRouter, Body, Depends, HTTPException, Path
from omni_python_library.dal import OsintDataAccessLayer, ViewDataAccessLayer
from omni_python_library.middleware import get_user_context
from omni_python_library.models import (
    Event,
    EventMainData,
    Organization,
    OrganizationMainData,
    OsintView,
    OsintViewMainData,
    Permissive,
    Person,
    PersonMainData,
    Relation,
    RelationMainData,
    Source,
    SourceMainData,
    Website,
    WebsiteMainData,
)
from omni_python_library.utils.errors import NotFoundError, PermissionDeniedError
from pydantic import BaseModel, Field

router = APIRouter(tags=["update"])
logger = logging.getLogger(__name__)
dal = OsintDataAccessLayer()
view_dal = ViewDataAccessLayer()


class EntityConnectionRequest(BaseModel):
    entity_id: str = Field(..., description="The ID of the entity to connect to the view.")


@router.put("/persons/{id:path}/permissions", response_model=Person, operation_id="update_person_permissions")
def update_person_permissions(
    id: str = Path(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    data: Permissive = Body(...),
    user_ctx: Dict = Depends(get_user_context),
):
    if not user_ctx["user_id"]:
        raise HTTPException(status_code=401, detail="No permission")
    try:
        logger.info(f"User {user_ctx['user_id']} is updating person permissions for {id} with data {data}")
        return dal.update_person(id, data, user_ctx["user_id"], [])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update person permissions for {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(
            f"User {user_ctx['user_id']} failed to update person permissions for {id} due to insufficient permissions"
        )
        raise HTTPException(status_code=403, detail="Only owner can update permissions")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update person permissions for {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/persons/{id:path}", response_model=Person, operation_id="update_person")
def update_person(
    id: str = Path(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    data: PersonMainData = Body(...),
    include_pending: bool = False,
    user_ctx: Dict = Depends(get_user_context),
):
    if not user_ctx["user_id"]:
        raise HTTPException(status_code=401, detail="No permission")
    try:
        logger.info(f"User {user_ctx['user_id']} is updating person {id} with data {data}")
        return dal.update_person(id, data, user_ctx["user_id"], user_ctx["roles"], include_pending)
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update person {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to update person {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update person {id} with data {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put(
    "/organizations/{id:path}/permissions", response_model=Organization, operation_id="update_organization_permissions"
)
def update_organization_permissions(
    id: str = Path(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    data: Permissive = Body(...),
    user_ctx: Dict = Depends(get_user_context),
):
    if not user_ctx["user_id"]:
        raise HTTPException(status_code=401, detail="No permission")
    try:
        logger.info(f"User {user_ctx['user_id']} is updating organization permissions for {id} with data {data}")
        return dal.update_organization(id, data, user_ctx["user_id"], [])
    except NotFoundError:
        logger.exception(
            f"User {user_ctx['user_id']} failed to update organization permissions for {id} due to not found"
        )
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(
            f"User {user_ctx['user_id']} failed to update organization permissions for {id} due to insufficient permissions"
        )
        raise HTTPException(status_code=403, detail="Only owner can update permissions")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update organization permissions for {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/organizations/{id:path}", response_model=Organization, operation_id="update_organization")
def update_organization(
    id: str = Path(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    data: OrganizationMainData = Body(...),
    include_pending: bool = False,
    user_ctx: Dict = Depends(get_user_context),
):
    if not user_ctx["user_id"]:
        raise HTTPException(status_code=401, detail="No permission")
    try:
        logger.info(f"User {user_ctx['user_id']} is updating organization {id} with data {data}")
        return dal.update_organization(id, data, user_ctx["user_id"], user_ctx["roles"], include_pending)
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update organization {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(
            f"User {user_ctx['user_id']} failed to update organization {id} due to insufficient permissions"
        )
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update organization {id} with data {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/events/{id:path}/permissions", response_model=Event, operation_id="update_event_permissions")
def update_event_permissions(
    id: str = Path(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    data: Permissive = Body(...),
    user_ctx: Dict = Depends(get_user_context),
):
    if not user_ctx["user_id"]:
        raise HTTPException(status_code=401, detail="No permission")
    try:
        logger.info(f"User {user_ctx['user_id']} is updating event permissions for event {id} with data {data}")
        return dal.update_event(id, data, user_ctx["user_id"], [])
    except NotFoundError:
        logger.exception(
            f"User {user_ctx['user_id']} failed to update event permissions for event {id} due to not found"
        )
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(
            f"User {user_ctx['user_id']} failed to update event permissions for event {id} due to insufficient permissions"
        )
        raise HTTPException(status_code=403, detail="Only owner can update permissions")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update event permissions for event {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/events/{id:path}", response_model=Event, operation_id="update_event")
def update_event(
    id: str = Path(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    data: EventMainData = Body(...),
    include_pending: bool = False,
    user_ctx: Dict = Depends(get_user_context),
):
    if not user_ctx["user_id"]:
        raise HTTPException(status_code=401, detail="No permission")
    try:
        logger.info(f"User {user_ctx['user_id']} is updating event {id} with data {data}")
        return dal.update_event(id, data, user_ctx["user_id"], user_ctx["roles"], include_pending)
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update event {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to update event {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update event {id} with data {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/websites/{id:path}/permissions", response_model=Website, operation_id="update_website_permissions")
def update_website_permissions(
    id: str = Path(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    data: Permissive = Body(...),
    user_ctx: Dict = Depends(get_user_context),
):
    if not user_ctx["user_id"]:
        raise HTTPException(status_code=401, detail="No permission")
    try:
        logger.info(f"User {user_ctx['user_id']} is updating website permissions for website {id} with data {data}")
        return dal.update_website(id, data, user_ctx["user_id"], [])
    except NotFoundError:
        logger.exception(
            f"User {user_ctx['user_id']} failed to update website permissions for website {id} due to not found"
        )
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(
            f"User {user_ctx['user_id']} failed to update website permissions for website {id} due to insufficient permissions"
        )
        raise HTTPException(status_code=403, detail="Only owner can update permissions")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update website permissions for website {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/websites/{id:path}", response_model=Website, operation_id="update_website")
def update_website(
    id: str = Path(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    data: WebsiteMainData = Body(...),
    include_pending: bool = False,
    user_ctx: Dict = Depends(get_user_context),
):
    if not user_ctx["user_id"]:
        raise HTTPException(status_code=401, detail="No permission")
    try:
        logger.info(f"User {user_ctx['user_id']} is updating website {id} with data {data}")
        return dal.update_website(id, data, user_ctx["user_id"], user_ctx["roles"], include_pending)
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update website {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to update website {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update website {id} with data {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/sources/{id:path}/permissions", response_model=Source, operation_id="update_source_permissions")
def update_source_permissions(
    id: str = Path(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    data: Permissive = Body(...),
    user_ctx: Dict = Depends(get_user_context),
):
    if not user_ctx["user_id"]:
        raise HTTPException(status_code=401, detail="No permission")
    try:
        logger.info(f"User {user_ctx['user_id']} is updating source permissions for source {id} with data {data}")
        return dal.update_source(id, data, user_ctx["user_id"], [])
    except NotFoundError:
        logger.exception(
            f"User {user_ctx['user_id']} failed to update source permissions for source {id} due to not found"
        )
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(
            f"User {user_ctx['user_id']} failed to update source permissions for source {id} due to insufficient permissions"
        )
        raise HTTPException(status_code=403, detail="Only owner can update permissions")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update source permissions for source {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/sources/{id:path}", response_model=Source, operation_id="update_source")
def update_source(
    id: str = Path(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    data: SourceMainData = Body(...),
    include_pending: bool = False,
    user_ctx: Dict = Depends(get_user_context),
):
    if not user_ctx["user_id"]:
        raise HTTPException(status_code=401, detail="No permission")
    try:
        logger.info(f"User {user_ctx['user_id']} is updating source {id} with data {data}")
        return dal.update_source(id, data, user_ctx["user_id"], user_ctx["roles"], include_pending)
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update source {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to update source {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update source {id} with data {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/relations/{id:path}/permissions", response_model=Relation, operation_id="update_relation_permissions")
def update_relation_permissions(
    id: str = Path(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    data: Permissive = Body(...),
    user_ctx: Dict = Depends(get_user_context),
):
    if not user_ctx["user_id"]:
        raise HTTPException(status_code=401, detail="No permission")
    try:
        logger.info(f"User {user_ctx['user_id']} is updating relation permissions for relation {id} with data {data}")
        return dal.update_relation(id, data, user_ctx["user_id"], [])
    except NotFoundError:
        logger.exception(
            f"User {user_ctx['user_id']} failed to update relation permissions for relation {id} due to not found"
        )
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(
            f"User {user_ctx['user_id']} failed to update relation permissions for relation {id} due to insufficient permissions"
        )
        raise HTTPException(status_code=403, detail="Only owner can update permissions")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update relation permissions for relation {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/relations/{id:path}", response_model=Relation, operation_id="update_relation")
def update_relation(
    id: str = Path(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    data: RelationMainData = Body(...),
    include_pending: bool = False,
    user_ctx: Dict = Depends(get_user_context),
):
    if not user_ctx["user_id"]:
        raise HTTPException(status_code=401, detail="No permission")
    if data.name is not None and (not data.name or not data.name.isascii()):
        raise HTTPException(status_code=400, detail="Relation name cannot be empty and must be ASCII")

    try:
        logger.info(f"User {user_ctx['user_id']} is updating relation {id} with data {data}")
        return dal.update_relation(id, data, user_ctx["user_id"], user_ctx["roles"], include_pending)
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update relation {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to update relation {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update relation {id} with data {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/views/{id:path}/entities", response_model=OsintView, operation_id="connect_entity_to_view")
def connect_entity_to_view(
    id: str = Path(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    payload: EntityConnectionRequest = Body(...),
    user_ctx: Dict = Depends(get_user_context),
):
    if not user_ctx["user_id"]:
        raise HTTPException(status_code=401, detail="No permission")
    try:
        return view_dal.connect_entity_to_view(
            id, payload.entity_id, owner=user_ctx["user_id"], roles=user_ctx["roles"]
        )
    except NotFoundError:
        logger.exception(
            f"User {user_ctx['user_id']} failed to connect entity {payload.entity_id} to view {id} due to not found"
        )
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(
            f"User {user_ctx['user_id']} failed to connect entity {payload.entity_id} to view {id} due to insufficient permissions"
        )
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to connect entity {payload.entity_id} to view {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/views/{id:path}/permissions", response_model=OsintView, operation_id="update_view_permissions")
def update_view_permissions(
    id: str = Path(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    data: Permissive = Body(...),
    user_ctx: Dict = Depends(get_user_context),
):
    if not user_ctx["user_id"]:
        raise HTTPException(status_code=401, detail="No permission")
    try:
        return view_dal.update_view(id, data, user_ctx["user_id"], [])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update view permissions for {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(
            f"User {user_ctx['user_id']} failed to update view permissions for {id} due to insufficient permissions"
        )
        raise HTTPException(status_code=403, detail="Only owner can update permissions")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update view permissions for {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/views/{id:path}", response_model=OsintView, operation_id="update_view")
def update_view(
    id: str = Path(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    data: OsintViewMainData = Body(...),
    user_ctx: Dict = Depends(get_user_context),
):
    if not user_ctx["user_id"]:
        raise HTTPException(status_code=401, detail="No permission")
    try:
        return view_dal.update_view(id, data, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update view {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to update view {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update view {id} with data {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
