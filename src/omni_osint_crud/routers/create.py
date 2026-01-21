from fastapi import APIRouter, HTTPException, Depends
import logging
from omni_python_library.dal.osint_data_access_layer import OsintDataAccessLayer
from omni_python_library.models.osint import (
    Person,
    Organization,
    Event,
    Website,
    Source,
    Relation,
    PersonMainData,
    OrganizationMainData,
    EventMainData,
    WebsiteMainData,
    SourceMainData,
    RelationMainData,
)
from omni_python_library.middleware.user_token import (
    get_owner_from_token,
    validate_create_permission,
)

router = APIRouter(
    prefix="/create",
    tags=["create"],
    dependencies=[Depends(validate_create_permission)],
)
logger = logging.getLogger(__name__)
dal = OsintDataAccessLayer()


@router.post("/person", response_model=Person)
def create_person(person: PersonMainData, owner: str = Depends(get_owner_from_token)):
    try:
        return dal.create_person(person, owner)
    except Exception:
        logger.exception(f"User {owner} failed to create person {person}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/organization", response_model=Organization)
def create_organization(
    organization: OrganizationMainData, owner: str = Depends(get_owner_from_token)
):
    try:
        return dal.create_organization(organization, owner)
    except Exception:
        logger.exception(f"User {owner} failed to create organization {organization}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/event", response_model=Event)
def create_event(event: EventMainData, owner: str = Depends(get_owner_from_token)):
    try:
        return dal.create_event(event, owner)
    except Exception:
        logger.exception(f"User {owner} failed to create event {event}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/website", response_model=Website)
def create_website(
    website: WebsiteMainData, owner: str = Depends(get_owner_from_token)
):
    try:
        return dal.create_website(website, owner)
    except Exception:
        logger.exception(f"User {owner} failed to create website {website}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/source", response_model=Source)
def create_source(source: SourceMainData, owner: str = Depends(get_owner_from_token)):
    try:
        return dal.create_source(source, owner)
    except Exception:
        logger.exception(f"User {owner} failed to create source {source}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/relation", response_model=Relation)
def create_relation(
    relation: RelationMainData, owner: str = Depends(get_owner_from_token)
):
    try:
        return dal.create_relation(relation, owner)
    except Exception:
        logger.exception(f"User {owner} failed to create relation {relation}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
