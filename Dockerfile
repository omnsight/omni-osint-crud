FROM python:3.11-slim-bookworm

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# Copy the project's dependency files
COPY pyproject.toml uv.lock ./

# Install the project's dependencies using the lockfile and settings
RUN uv sync --frozen --no-install-project --no-dev

# Copy the project source code
COPY src ./src
COPY README.md ./

# Install the project
RUN uv sync --frozen --no-dev

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Reset the entrypoint, don't invoke `uv`
ENTRYPOINT []

# Run the application
CMD ["uvicorn", "omni_osint_crud.main:app", "--host", "0.0.0.0", "--port", "8000"]
