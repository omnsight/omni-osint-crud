# Omni OSINT Data Management API Backend
[![codecov](https://codecov.io/github/omnsight/omni-osint-crud/graph/badge.svg?token=2LDW67VWXE)](https://codecov.io/github/omnsight/omni-osint-crud)

## Overview

This project provides a backend service for managing Open-Source Intelligence (OSINT) data. Built with Python and FastAPI, it offers a structured and efficient API for creating, reading, updating, and deleting OSINT entities. The service is designed to be a foundational component in a larger intelligence-gathering ecosystem, providing a reliable persistence layer for structured data.

The API is defined using the OpenAPI standard, and the project includes tooling to automatically generate the `openapi.json` specification. This enables seamless integration with other services and facilitates the auto-generation of client libraries.

Key technologies used:
- **FastAPI**: For building a high-performance, modern API.
- **Pydantic**: For robust data validation and settings management.
- **uv**: For fast and efficient Python package management.

Client documentation is located at [client/README.md](client/README.md).

## Project Structure

High-level overview of the project folder structure:

- `client/`: TypeScript client library generated from the OpenAPI definition. Contains source code and build scripts.
- `doc/`: Documentation artifacts, including `openapi.json` used for client generation.
- `src/omni_osint_crud/`: Python source code for the backend application.
    - `routers/`: API route definitions.
    - `main.py`: Application entry point and configuration.
- `tools/`: Utility scripts (e.g., for exporting OpenAPI specs).
- `pyproject.toml` / `uv.lock`: Python dependency management and project configuration.
- `docker-compose.yml` / `Dockerfile`: Containerization configuration.

## Local Development

### Manage with uv

This project is managed with [uv](https://github.com/astral-sh/uv).

Install dependencies:
```bash
uv sync --extra dev
```

Upgrade dependencies:
```bash
uv lock --upgrade
uv sync --extra dev

uv run poe clean
```

Run unit tests

```bash
# loading .env is necessary for local testing
docker compose up -d --wait
export $(cat .env | xargs) && uv run pytest
docker compose down
```

Run the application:
```bash
uv run uvicorn omni_osint_crud.main:app --reload
```

### Export OpenAPI Definition

Export the OpenAPI definition to `doc/openapi.json`:
```bash
uv run python scripts/export_openapi.py
```

### Code Formatting

Format the code using black:
```bash
uv run black .
uv run isort .
```

### Generate Client

```bash
cd client
npm run generate
cd ..
```
