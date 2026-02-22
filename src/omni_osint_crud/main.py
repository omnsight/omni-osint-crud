from contextlib import asynccontextmanager

from fastapi import FastAPI
from omni_python_library import init_omni_library

from omni_osint_crud.routers import (
    create_router,
    delete_router,
    health_router,
    read_router,
    update_router,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_omni_library()
    yield


app = FastAPI(title="Omni OSINT CRUD", lifespan=lifespan)

# Include routers
app.include_router(create_router)
app.include_router(read_router)
app.include_router(update_router)
app.include_router(delete_router)
app.include_router(health_router)
