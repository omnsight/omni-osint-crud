from fastapi import APIRouter, HTTPException, Depends
from typing import Dict
from omni_python_library.dal.osint_data_access_layer import OsintDataAccessLayer
from omni_python_library.models.osint import (
    Person,
    Organization,
    Event,
    Website,
    Source,
    Relation,
)
from omni_python_library.middleware.user_token import get_user_context

router = APIRouter(prefix="/read", tags=["read"])
dal = OsintDataAccessLayer()


@router.get("/person/{id}", response_model=Person)
def get_person(id: str, user_ctx: Dict = Depends(get_user_context)):
    if not dal.can_read(id, user_ctx["user_id"], user_ctx["roles"]):
        raise HTTPException(
            status_code=403, detail="Insufficient permissions to read this resource"
        )

    result = dal.get_person(id)
    if not result:
        raise HTTPException(status_code=404, detail="Person not found")
    return result


@router.get("/organization/{id}", response_model=Organization)
def get_organization(id: str, user_ctx: Dict = Depends(get_user_context)):
    if not dal.can_read(id, user_ctx["user_id"], user_ctx["roles"]):
        raise HTTPException(
            status_code=403, detail="Insufficient permissions to read this resource"
        )

    result = dal.get_organization(id)
    if not result:
        raise HTTPException(status_code=404, detail="Organization not found")
    return result


@router.get("/event/{id}", response_model=Event)
def get_event(id: str, user_ctx: Dict = Depends(get_user_context)):
    if not dal.can_read(id, user_ctx["user_id"], user_ctx["roles"]):
        raise HTTPException(
            status_code=403, detail="Insufficient permissions to read this resource"
        )

    result = dal.get_event(id)
    if not result:
        raise HTTPException(status_code=404, detail="Event not found")
    return result


@router.get("/website/{id}", response_model=Website)
def get_website(id: str, user_ctx: Dict = Depends(get_user_context)):
    if not dal.can_read(id, user_ctx["user_id"], user_ctx["roles"]):
        raise HTTPException(
            status_code=403, detail="Insufficient permissions to read this resource"
        )

    result = dal.get_website(id)
    if not result:
        raise HTTPException(status_code=404, detail="Website not found")
    return result


@router.get("/source/{id}", response_model=Source)
def get_source(id: str, user_ctx: Dict = Depends(get_user_context)):
    if not dal.can_read(id, user_ctx["user_id"], user_ctx["roles"]):
        raise HTTPException(
            status_code=403, detail="Insufficient permissions to read this resource"
        )

    result = dal.get_source(id)
    if not result:
        raise HTTPException(status_code=404, detail="Source not found")
    return result


@router.get("/relation/{id}", response_model=Relation)
def get_relation(id: str, user_ctx: Dict = Depends(get_user_context)):
    if not dal.can_read(id, user_ctx["user_id"], user_ctx["roles"]):
        raise HTTPException(
            status_code=403, detail="Insufficient permissions to read this resource"
        )

    result = dal.get_relation(id)
    if not result:
        raise HTTPException(status_code=404, detail="Relation not found")
    return result
