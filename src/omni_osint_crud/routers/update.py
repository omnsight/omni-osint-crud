import logging
from typing import Dict

from fastapi import APIRouter, Body, Depends, HTTPException
from omni_python_library.dal.osint_data_access_layer import OsintDataAccessLayer
from omni_python_library.middleware.user_token import get_user_context
from omni_python_library.models.common import Permissive
from omni_python_library.models.osint import (
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
)
from omni_python_library.utils import NotFoundError, PermissionDeniedError

router = APIRouter(prefix="/update", tags=["update"])
logger = logging.getLogger(__name__)
dal = OsintDataAccessLayer()


@router.put("/person/{id:path}", response_model=Person)
def update_person(
    id: str,
    data: PersonMainData = Body(...),
    user_ctx: Dict = Depends(get_user_context),
):
    try:
        return dal.update_person(id, data, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update person {id} with data {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/person/{id}/permissions", response_model=Person)
def update_person_permissions(id: str, data: Permissive = Body(...), user_ctx: Dict = Depends(get_user_context)):
    try:
        return dal.update_person(id, data, user_ctx["user_id"], [])
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Only owner can update permissions")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update person permissions for {id}")
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
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update organization {id} with data {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/organization/{id}/permissions", response_model=Organization)
def update_organization_permissions(id: str, data: Permissive = Body(...), user_ctx: Dict = Depends(get_user_context)):
    try:
        return dal.update_organization(id, data, user_ctx["user_id"], [])
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Only owner can update permissions")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update organization permissions for {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/event/{id:path}", response_model=Event)
def update_event(id: str, data: EventMainData = Body(...), user_ctx: Dict = Depends(get_user_context)):
    try:
        return dal.update_event(id, data, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update event {id} with data {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/event/{id}/permissions", response_model=Event)
def update_event_permissions(id: str, data: Permissive = Body(...), user_ctx: Dict = Depends(get_user_context)):
    try:
        return dal.update_event(id, data, user_ctx["user_id"], [])
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Only owner can update permissions")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update event permissions for event {id}")
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
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update website {id} with data {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/website/{id}/permissions", response_model=Website)
def update_website_permissions(id: str, data: Permissive = Body(...), user_ctx: Dict = Depends(get_user_context)):
    try:
        return dal.update_website(id, data, user_ctx["user_id"], [])
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Only owner can update permissions")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update website permissions for website {id}")
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
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update source {id} with data {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/source/{id}/permissions", response_model=Source)
def update_source_permissions(id: str, data: Permissive = Body(...), user_ctx: Dict = Depends(get_user_context)):
    try:
        return dal.update_source(id, data, user_ctx["user_id"], [])
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Only owner can update permissions")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update source permissions for source {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/relation/{id:path}", response_model=Relation)
def update_relation(
    id: str,
    data: RelationMainData = Body(...),
    user_ctx: Dict = Depends(get_user_context),
):
    try:
        return dal.update_relation(id, data, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update relation {id} with data {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/relation/{id}/permissions", response_model=Relation)
def update_relation_permissions(id: str, data: Permissive = Body(...), user_ctx: Dict = Depends(get_user_context)):
    try:
        return dal.update_relation(id, data, user_ctx["user_id"], [])
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Only owner can update permissions")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update relation permissions for relation {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
