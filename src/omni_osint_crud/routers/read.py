import logging
from typing import Dict

from fastapi import APIRouter, Depends, HTTPException
from omni_python_library.dal.osint_data_access_layer import OsintDataAccessLayer
from omni_python_library.middleware.user_token import get_user_context
from omni_python_library.models.osint import (
    Event,
    Organization,
    Person,
    Relation,
    Source,
    Website,
)
from omni_python_library.utils import NotFoundError, PermissionDeniedError

router = APIRouter(prefix="/read", tags=["read"])
logger = logging.getLogger(__name__)
dal = OsintDataAccessLayer()


@router.get("/person/{id:path}", response_model=Person)
def get_person(id: str, user_ctx: Dict = Depends(get_user_context)):
    try:
        result = dal.get_person(id, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to read person {id}")
        raise HTTPException(status_code=500, detail="Internal service error")

    if not result:
        raise HTTPException(status_code=404, detail="Person not found")
    return result


@router.get("/organization/{id:path}", response_model=Organization)
def get_organization(id: str, user_ctx: Dict = Depends(get_user_context)):
    try:
        result = dal.get_organization(id, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to read organization {id}")
        raise HTTPException(status_code=500, detail="Internal service error")

    if not result:
        raise HTTPException(status_code=404, detail="Organization not found")
    return result


@router.get("/event/{id:path}", response_model=Event)
def get_event(id: str, user_ctx: Dict = Depends(get_user_context)):
    try:
        result = dal.get_event(id, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to read event {id}")
        raise HTTPException(status_code=500, detail="Internal service error")

    if not result:
        raise HTTPException(status_code=404, detail="Event not found")
    return result


@router.get("/website/{id:path}", response_model=Website)
def get_website(id: str, user_ctx: Dict = Depends(get_user_context)):
    try:
        result = dal.get_website(id, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to read website {id}")
        raise HTTPException(status_code=500, detail="Internal service error")

    if not result:
        raise HTTPException(status_code=404, detail="Website not found")
    return result


@router.get("/source/{id:path}", response_model=Source)
def get_source(id: str, user_ctx: Dict = Depends(get_user_context)):
    try:
        result = dal.get_source(id, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to read source {id}")
        raise HTTPException(status_code=500, detail="Internal service error")

    if not result:
        raise HTTPException(status_code=404, detail="Source not found")
    return result


@router.get("/relation/{id:path}", response_model=Relation)
def get_relation(id: str, user_ctx: Dict = Depends(get_user_context)):
    try:
        result = dal.get_relation(id, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to read relation {id}")
        raise HTTPException(status_code=500, detail="Internal service error")

    if not result:
        raise HTTPException(status_code=404, detail="Relation not found")
    return result
