import logging
import os
import sys
from pythonjsonlogger import jsonlogger
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from omni_python_library import init_omni_library
from omni_python_library.middleware import RawASGILoggingMiddleware

from omni_osint_crud.routers import (
    create_router,
    delete_router,
    health_router,
    read_router,
    update_router,
)

# Configure logging
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
log_level = logging.DEBUG if DEBUG else logging.INFO
log_handler = logging.StreamHandler(sys.stdout)
formatter = jsonlogger.JsonFormatter(fmt="%(asctime)s %(levelname)s %(name)s %(message)s", datefmt="%Y-%m-%dT%H:%M:%SZ")
log_handler.setFormatter(formatter)
root_logger = logging.getLogger()
root_logger.handlers = []
root_logger.addHandler(log_handler)
root_logger.setLevel(log_level)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Service - Osint Crud - starting up...")
    init_omni_library()

    loggers = ["uvicorn", "uvicorn.access", "uvicorn.error", "fastapi"]
    for logger_name in loggers:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = []
        # Optional: Prevent propagation to the root logger
        logging_logger.propagate = False
    logger.info(f"Stopped default logging for {loggers}")

    yield
    logger.info("Service - Osint Crud - shut down")


app = FastAPI(title="Omni OSINT CRUD", lifespan=lifespan)
app.add_middleware(RawASGILoggingMiddleware)
raw_origins = os.getenv("ALLOWED_ORIGINS", "")
origins = [origin.strip() for origin in raw_origins.split(",") if origin.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTPException: {exc.status_code} {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


# Include routers
app.include_router(create_router)
app.include_router(read_router)
app.include_router(update_router)
app.include_router(delete_router)
app.include_router(health_router)
