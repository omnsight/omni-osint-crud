## 🛠️ Installation Guide

This project is managed with [uv](https://github.com/astral-sh/uv).

Install/Upgrade dependencies:
```bash
uv lock --upgrade
uv sync --extra dev
```

Clean up:
```bash
uv run poe clean
```

## 🚀 Run Service Locally & Debug

Run the application:
```bash
uv run uvicorn omni_osint_crud.main:app --reload
```

Run service:
```bash
docker-compose up -d --build --wait
docker compose down

docker inspect <container name>

docker logs <container name>
```

## 🧪 Running Unit Tests

```bash
# loading .env is necessary for local testing
docker compose up -d --wait
export $(cat .env | xargs) && uv run pytest
docker compose down
```

## ✨ Formatting Code

Format the code using black:
```bash
uv run black .
uv run isort .
```

## 📄 Export OpenAPI Definition

Export the OpenAPI definition to `doc/openapi.json`:
```bash
uv run python scripts/export_openapi.py
```

### Updage Release Version

```bash
# major
uv run python scripts/update_version.py -r 1
# minor
uv run python scripts/update_version.py -r 2
# patch
uv run python scripts/update_version.py -r 3
```
