from omni_osint_crud.routers.create import router as create_router
from omni_osint_crud.routers.delete import router as delete_router
from omni_osint_crud.routers.health import router as health_router
from omni_osint_crud.routers.read import router as read_router
from omni_osint_crud.routers.update import router as update_router

__all__ = ["create_router", "delete_router", "health_router", "read_router", "update_router"]
