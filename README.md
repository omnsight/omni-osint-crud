# omni-osint-crud

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
uv sync
```

Upgrade dependencies:
```bash
uv lock --upgrade
uv sync
```

Run the application:
```bash
uv run uvicorn omni_osint_crud.main:app --reload
```

### Export OpenAPI Definition

Export the OpenAPI definition to `doc/openapi.json`:
```bash
uv run python tools/export_openapi.py
```


