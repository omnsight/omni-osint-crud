import logging
from typing import Dict, List

from fastapi import APIRouter, Depends, HTTPException, Path, Query
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
from pydantic import BaseModel, Field

router = APIRouter(tags=["read"])
logger = logging.getLogger(__name__)
dal = OsintDataAccessLayer()
view_dal = ViewDataAccessLayer()


class Entities(BaseModel):
    events: List[Event] = Field(default_factory=list, description="A list of events related to the entity.")
    sources: List[Source] = Field(default_factory=list, description="A list of sources related to the entity.")
    people: List[Person] = Field(default_factory=list, description="A list of persons related to the entity.")
    organizations: List[Organization] = Field(
        default_factory=list, description="A list of organizations related to the entity."
    )
    websites: List[Website] = Field(default_factory=list, description="A list of websites related to the entity.")
    relations: List[Relation] = Field(default_factory=list, description="A list of relations related to the entity.")


class QueryViewsResponse(BaseModel):
    views: List[OsintView] = Field(default_factory=list, description="A list of views")
    offset: int = Field(default=0, description="The offset from which to start returning results.")


@router.get("/persons", response_model=Person, operation_id="get_person")
def get_person(
    id: str = Query(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    include_pending: bool = False,
    user_ctx: Dict = Depends(get_user_context),
):
    try:
        result = dal.get_person(id, user_ctx["user_id"], user_ctx["roles"], include_pending)
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


@router.get("/organizations", response_model=Organization, operation_id="get_organization")
def get_organization(
    id: str = Query(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    include_pending: bool = False,
    user_ctx: Dict = Depends(get_user_context),
):
    try:
        result = dal.get_organization(id, user_ctx["user_id"], user_ctx["roles"], include_pending)
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


@router.get("/events", response_model=Event, operation_id="get_event")
def get_event(
    id: str = Query(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    include_pending: bool = False,
    user_ctx: Dict = Depends(get_user_context),
):
    try:
        result = dal.get_event(id, user_ctx["user_id"], user_ctx["roles"], include_pending)
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


@router.get("/websites", response_model=Website, operation_id="get_website")
def get_website(
    id: str = Query(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    include_pending: bool = False,
    user_ctx: Dict = Depends(get_user_context),
):
    try:
        result = dal.get_website(id, user_ctx["user_id"], user_ctx["roles"], include_pending)
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


@router.get("/sources", response_model=Source, operation_id="get_source")
def get_source(
    id: str = Query(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    include_pending: bool = False,
    user_ctx: Dict = Depends(get_user_context),
):
    try:
        result = dal.get_source(id, user_ctx["user_id"], user_ctx["roles"], include_pending)
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


@router.get("/relations", response_model=Relation, operation_id="get_relation")
def get_relation(
    id: str = Query(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    include_pending: bool = False,
    user_ctx: Dict = Depends(get_user_context),
):
    try:
        result = dal.get_relation(id, user_ctx["user_id"], user_ctx["roles"], include_pending)
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
    "/views/entities",
    response_model=Entities,
    operation_id="get_view_entities",
)
def get_view_entities(
    id: str = Query(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    user_ctx: Dict = Depends(get_user_context),
):
    try:
        results = view_dal.get_entities(id, user_ctx["user_id"], user_ctx["roles"])
        return Entities(
            events=[e for e in results if isinstance(e, Event)],
            sources=[s for s in results if isinstance(s, Source)],
            people=[p for p in results if isinstance(p, Person)],
            organizations=[o for o in results if isinstance(o, Organization)],
            websites=[w for w in results if isinstance(w, Website)],
            relations=[r for r in results if isinstance(r, Relation)],
        )
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


@router.get("/views", response_model=OsintView, operation_id="get_view")
def get_view(
    id: str = Query(
        pattern=r"^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$", description="The ArangoDB Document ID (e.g., collection/123)"
    ),
    user_ctx: Dict = Depends(get_user_context),
):
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


@router.get("/views/query", response_model=QueryViewsResponse, operation_id="query_views")
def query_views(text: str | None = None, limit: int = 100, offset: int = 0, user_ctx: Dict = Depends(get_user_context)):
    try:
        results = view_dal.query_views(text=text, owner=user_ctx["user_id"], limit=limit, offset=offset)
        return QueryViewsResponse(views=results, offset=offset + len(results))
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to query views with text '{text}'")
        raise HTTPException(status_code=500, detail="Internal service error")
