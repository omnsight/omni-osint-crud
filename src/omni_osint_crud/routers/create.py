import logging
from typing import Dict

from fastapi import APIRouter, Depends, HTTPException
from omni_python_library.dal import OsintDataAccessLayer, ViewDataAccessLayer
from omni_python_library.middleware import get_user_context
from omni_python_library.models import (
    Event,
    EventMainData,
    Organization,
    OrganizationMainData,
    OsintView,
    OsintViewMainData,
    Person,
    PersonMainData,
    Relation,
    RelationMainData,
    Source,
    SourceMainData,
    Website,
    WebsiteMainData,
)
from omni_python_library.utils.errors import PermissionDeniedError

router = APIRouter(
    tags=["create"],
)
logger = logging.getLogger(__name__)
dal = OsintDataAccessLayer()
view_dal = ViewDataAccessLayer()


@router.post("/person", response_model=Person, operation_id="create_person")
def create_person(person: PersonMainData, include_pending: bool = False, user_ctx: Dict = Depends(get_user_context)):
    try:
        return dal.create_person(person, user_ctx["user_id"], user_ctx["roles"], include_pending)
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to create person {person} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Only the owner can create this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to create person {person}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/organization", response_model=Organization, operation_id="create_organization")
def create_organization(
    organization: OrganizationMainData, include_pending: bool = False, user_ctx: Dict = Depends(get_user_context)
):
    try:
        return dal.create_organization(organization, user_ctx["user_id"], user_ctx["roles"], include_pending)
    except PermissionDeniedError:
        logger.exception(
            f"User {user_ctx['user_id']} failed to create organization {organization} due to insufficient permissions"
        )
        raise HTTPException(status_code=403, detail="Only the owner can create this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to create organization {organization}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/event", response_model=Event, operation_id="create_event")
def create_event(event: EventMainData, include_pending: bool = False, user_ctx: Dict = Depends(get_user_context)):
    try:
        return dal.create_event(event, user_ctx["user_id"], user_ctx["roles"], include_pending)
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to create event {event} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Only the owner can create this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to create event {event}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/website", response_model=Website, operation_id="create_website")
def create_website(website: WebsiteMainData, include_pending: bool = False, user_ctx: Dict = Depends(get_user_context)):
    try:
        return dal.create_website(website, user_ctx["user_id"], user_ctx["roles"], include_pending)
    except PermissionDeniedError:
        logger.exception(
            f"User {user_ctx['user_id']} failed to create website {website} due to insufficient permissions"
        )
        raise HTTPException(status_code=403, detail="Only the owner can create this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to create website {website}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/source", response_model=Source, operation_id="create_source")
def create_source(source: SourceMainData, include_pending: bool = False, user_ctx: Dict = Depends(get_user_context)):
    try:
        return dal.create_source(source, user_ctx["user_id"], user_ctx["roles"], include_pending)
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to create source {source} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Only the owner can create this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to create source {source}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/relation", response_model=Relation, operation_id="create_relation")
def create_relation(
    relation: RelationMainData, include_pending: bool = False, user_ctx: Dict = Depends(get_user_context)
):
    if not relation.from_id or not relation.to_id:
        raise HTTPException(status_code=400, detail="Source and target document IDs are required")

    if not relation.name or not relation.name.isascii():
        raise HTTPException(status_code=400, detail="Relation name is required and must be non-empty ASCII")

    try:
        return dal.create_relation(relation, user_ctx["user_id"], user_ctx["roles"], include_pending)
    except PermissionDeniedError:
        logger.exception(
            f"User {user_ctx['user_id']} failed to create relation {relation} due to insufficient permissions"
        )
        raise HTTPException(status_code=403, detail="Only the owner can create this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to create relation {relation}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/view", response_model=OsintView, operation_id="create_view")
def create_view(view: OsintViewMainData, user_ctx: Dict = Depends(get_user_context)):
    if not view.name:
        raise HTTPException(status_code=400, detail="View name is required")

    if not view.description:
        raise HTTPException(status_code=400, detail="View description is required")

    if view.configs is None:
        raise HTTPException(status_code=400, detail="View configs are required")

    try:
        return view_dal.create_view(view, user_ctx["user_id"], user_ctx["roles"])
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to create view {view} due to insufficient permissions")
        raise HTTPException(status_code=403, detail="Only the owner can create this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to create view {view}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
