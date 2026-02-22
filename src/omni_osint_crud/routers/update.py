import logging
from typing import Dict
from pydantic import BaseModel, Field

from fastapi import APIRouter, Body, Depends, HTTPException
from omni_python_library.dal import OsintDataAccessLayer, ViewDataAccessLayer
from omni_python_library.middleware import get_user_context
from omni_python_library.models import (
    Permissive,
    Event,
    EventMainData,
    Organization,
    OrganizationMainData,
    Person,
    PersonMainData,
    Relation,
    RelationMainData,
    Source,
    SourceMainData,
    Website,
    WebsiteMainData,
    OsintView,
    OsintViewMainData,
    ViewConfig,
)
from omni_python_library.utils.errors import NotFoundError, PermissionDeniedError

router = APIRouter(prefix="/update", tags=["update"])
logger = logging.getLogger(__name__)
dal = OsintDataAccessLayer()
view_dal = ViewDataAccessLayer()


class EntityConnectionRequest(BaseModel):
    entity_id: str = Field(..., description="The ID of the entity to connect to the view.")


@router.put("/person/{id:path}/permissions", response_model=Person)
def update_person_permissions(id: str, data: Permissive = Body(...), user_ctx: Dict = Depends(get_user_context)):
    try:
        return dal.update_person(id, data, user_ctx["user_id"], [])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update person permissions for {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to update person permissions for {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Only owner can update permissions")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update person permissions for {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/person/{id:path}", response_model=Person)
def update_person(
    id: str,
    data: PersonMainData = Body(...),
    user_ctx: Dict = Depends(get_user_context),
):
    try:
        return dal.update_person(id, data, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update person {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to update person {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update person {id} with data {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/organization/{id:path}/permissions", response_model=Organization)
def update_organization_permissions(id: str, data: Permissive = Body(...), user_ctx: Dict = Depends(get_user_context)):
    try:
        return dal.update_organization(id, data, user_ctx["user_id"], [])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update organization permissions for {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to update organization permissions for {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Only owner can update permissions")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update organization permissions for {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/organization/{id:path}", response_model=Organization)
def update_organization(
    id: str,
    data: OrganizationMainData = Body(...),
    user_ctx: Dict = Depends(get_user_context),
):
    try:
        return dal.update_organization(id, data, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update organization {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to update organization {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update organization {id} with data {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/event/{id:path}/permissions", response_model=Event)
def update_event_permissions(id: str, data: Permissive = Body(...), user_ctx: Dict = Depends(get_user_context)):
    try:
        return dal.update_event(id, data, user_ctx["user_id"], [])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update event permissions for event {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to update event permissions for event {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Only owner can update permissions")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update event permissions for event {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/event/{id:path}", response_model=Event)
def update_event(id: str, data: EventMainData = Body(...), user_ctx: Dict = Depends(get_user_context)):
    try:
        return dal.update_event(id, data, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update event {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to update event {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update event {id} with data {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/website/{id:path}/permissions", response_model=Website)
def update_website_permissions(id: str, data: Permissive = Body(...), user_ctx: Dict = Depends(get_user_context)):
    try:
        return dal.update_website(id, data, user_ctx["user_id"], [])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update website permissions for website {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to update website permissions for website {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Only owner can update permissions")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update website permissions for website {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/website/{id:path}", response_model=Website)
def update_website(
    id: str,
    data: WebsiteMainData = Body(...),
    user_ctx: Dict = Depends(get_user_context),
):
    try:
        return dal.update_website(id, data, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update website {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to update website {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update website {id} with data {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/source/{id:path}/permissions", response_model=Source)
def update_source_permissions(id: str, data: Permissive = Body(...), user_ctx: Dict = Depends(get_user_context)):
    try:
        return dal.update_source(id, data, user_ctx["user_id"], [])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update source permissions for source {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to update source permissions for source {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Only owner can update permissions")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update source permissions for source {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/source/{id:path}", response_model=Source)
def update_source(
    id: str,
    data: SourceMainData = Body(...),
    user_ctx: Dict = Depends(get_user_context),
):
    try:
        return dal.update_source(id, data, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update source {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to update source {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update source {id} with data {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/relation/{id:path}/permissions", response_model=Relation)
def update_relation_permissions(id: str, data: Permissive = Body(...), user_ctx: Dict = Depends(get_user_context)):
    try:
        return dal.update_relation(id, data, user_ctx["user_id"], [])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update relation permissions for relation {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to update relation permissions for relation {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Only owner can update permissions")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update relation permissions for relation {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/relation/{id:path}", response_model=Relation)
def update_relation(
    id: str,
    data: RelationMainData = Body(...),
    user_ctx: Dict = Depends(get_user_context),
):
    if data.name is not None and (not data.name or not data.name.isascii()):
        raise HTTPException(status_code=400, detail="Relation name cannot be empty and must be ASCII")

    try:
        return dal.update_relation(id, data, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update relation {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to update relation {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update relation {id} with data {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/view/{id:path}/configs", response_model=OsintView)
def add_view_config(id: str, config: ViewConfig = Body(...), user_ctx: Dict = Depends(get_user_context)):
    try:
        return view_dal.add_view_config(id, config, owner=user_ctx["user_id"], roles=user_ctx["roles"])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to add config to view {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to add config to view {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to add config to view {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/view/{id:path}/entities", response_model=OsintView)
def connect_entity_to_view(id: str, payload: EntityConnectionRequest = Body(...), user_ctx: Dict = Depends(get_user_context)):
    try:
        return view_dal.connect_entity_to_view(
            id, payload.entity_id, owner=user_ctx["user_id"], roles=user_ctx["roles"]
        )
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to connect entity {payload.entity_id} to view {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to connect entity {payload.entity_id} to view {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to connect entity {payload.entity_id} to view {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/view/{id:path}/permissions", response_model=OsintView)
def update_view_permissions(id: str, data: Permissive = Body(...), user_ctx: Dict = Depends(get_user_context)):
    try:
        return view_dal.update_view(id, data, user_ctx["user_id"], [])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to update view permissions for {id} due to not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to update view permissions for {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Only owner can update permissions")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update view permissions for {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/view/{id:path}", response_model=OsintView)
def update_view(
    id: str,
    data: OsintViewMainData = Body(...),
    user_ctx: Dict = Depends(get_user_context),
):
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
