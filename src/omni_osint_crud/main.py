import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from omni_python_library import init_omni_library
from omni_python_library.clients.openai import OpenAIClient

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
    OpenAIClient().add_client(
        model_use="embedding",
        api_key=os.getenv("OPENAI_API_KEY"),
        model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"),
    )
    yield


app = FastAPI(title="Omni OSINT CRUD", lifespan=lifespan)

# Include routers
app.include_router(create_router)
app.include_router(read_router)
app.include_router(update_router)
app.include_router(delete_router)
app.include_router(health_router)
