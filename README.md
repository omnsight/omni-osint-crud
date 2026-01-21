# omni-osint-crud

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

