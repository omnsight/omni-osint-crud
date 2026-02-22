from fastapi import APIRouter
from omni_python_library.clients.arangodb import ArangoDBClient
from omni_python_library.clients.redis import RedisClient
from pydantic import BaseModel, Field

router = APIRouter(tags=["health"])


class HealthCheck(BaseModel):
    status: str = Field(description="The health status of the service.")


@router.get("/health", response_model=HealthCheck, operation_id="health_check")
def health_check():
    ArangoDBClient().db.version()
    RedisClient().client.ping()
    return HealthCheck(status="ok")
