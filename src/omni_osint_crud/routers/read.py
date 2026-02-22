import logging
from typing import Dict, List, Union

from fastapi import APIRouter, Depends, HTTPException
from omni_python_library.dal import OsintDataAccessLayer, ViewDataAccessLayer
from omni_python_library.middleware import get_user_context
from omni_python_library.models import (
    Event,
    Organization,
    OsintView,
    Person,
    Relation,
    Source,
    Website,
)
from omni_python_library.utils.errors import NotFoundError, PermissionDeniedError

router = APIRouter(prefix="/read", tags=["read"])
logger = logging.getLogger(__name__)
dal = OsintDataAccessLayer()
view_dal = ViewDataAccessLayer()


@router.get("/person/{id:path}", response_model=Person, operation_id="get_person")
def get_person(id: str, user_ctx: Dict = Depends(get_user_context)):
    try:
        result = dal.get_person(id, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to read person {id} as it was not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to read person {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to read person {id}")
        raise HTTPException(status_code=500, detail="Internal service error")

    if not result:
        raise HTTPException(status_code=404, detail="Person not found")
    return result


@router.get("/organization/{id:path}", response_model=Organization, operation_id="get_organization")
def get_organization(id: str, user_ctx: Dict = Depends(get_user_context)):
    try:
        result = dal.get_organization(id, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to read organization {id} as it was not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to read organization {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to read organization {id}")
        raise HTTPException(status_code=500, detail="Internal service error")

    if not result:
        raise HTTPException(status_code=404, detail="Organization not found")
    return result


@router.get("/event/{id:path}", response_model=Event, operation_id="get_event")
def get_event(id: str, user_ctx: Dict = Depends(get_user_context)):
    try:
        result = dal.get_event(id, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to read event {id} as it was not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to read event {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to read event {id}")
        raise HTTPException(status_code=500, detail="Internal service error")

    if not result:
        raise HTTPException(status_code=404, detail="Event not found")
    return result


@router.get("/website/{id:path}", response_model=Website, operation_id="get_website")
def get_website(id: str, user_ctx: Dict = Depends(get_user_context)):
    try:
        result = dal.get_website(id, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to read website {id} as it was not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to read website {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to read website {id}")
        raise HTTPException(status_code=500, detail="Internal service error")

    if not result:
        raise HTTPException(status_code=404, detail="Website not found")
    return result


@router.get("/source/{id:path}", response_model=Source, operation_id="get_source")
def get_source(id: str, user_ctx: Dict = Depends(get_user_context)):
    try:
        result = dal.get_source(id, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to read source {id} as it was not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to read source {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to read source {id}")
        raise HTTPException(status_code=500, detail="Internal service error")

    if not result:
        raise HTTPException(status_code=404, detail="Source not found")
    return result


@router.get("/relation/{id:path}", response_model=Relation, operation_id="get_relation")
def get_relation(id: str, user_ctx: Dict = Depends(get_user_context)):
    try:
        result = dal.get_relation(id, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to read relation {id} as it was not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to read relation {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to read relation {id}")
        raise HTTPException(status_code=500, detail="Internal service error")

    if not result:
        raise HTTPException(status_code=404, detail="Relation not found")
    return result


@router.get(
    "/view/{id:path}/entities",
    response_model=List[Union[Relation, Event, Source, Person, Organization, Website]],
    operation_id="get_view_entities",
)
def get_view_entities(id: str, user_ctx: Dict = Depends(get_user_context)):
    try:
        return view_dal.get_entities(id, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to read entities for view {id} as it was not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(
            f"User {user_ctx['user_id']} failed to read entities for view {id} due to insufficient permissions"
        )
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to read entities for view {id}")
        raise HTTPException(status_code=500, detail="Internal service error")


@router.get("/view/{id:path}", response_model=OsintView, operation_id="get_view")
def get_view(id: str, user_ctx: Dict = Depends(get_user_context)):
    try:
        result = view_dal.get_view(id, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        logger.exception(f"User {user_ctx['user_id']} failed to read view {id} as it was not found")
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to read view {id} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to read view {id}")
        raise HTTPException(status_code=500, detail="Internal service error")

    if not result:
        raise HTTPException(status_code=404, detail="View not found")
    return result


@router.get("/views", response_model=List[OsintView], operation_id="query_views")
def query_views(text: str, limit: int = 100, offset: int = 0, user_ctx: Dict = Depends(get_user_context)):
    try:
        return view_dal.query_views(text=text, owner=user_ctx["user_id"], limit=limit, offset=offset)
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to query views with text '{text}'")
        raise HTTPException(status_code=500, detail="Internal service error")
