from fastapi import APIRouter
from pydantic import BaseModel
from omni_python_library.clients.arangodb import ArangoDBClient
from omni_python_library.clients.redis import RedisClient

router = APIRouter(tags=["health"])


class HealthCheck(BaseModel):
    status: str


@router.get("/health", response_model=HealthCheck)
def health_check():
    ArangoDBClient().db.version()
    RedisClient().client.ping()
    return HealthCheck(status="ok")
