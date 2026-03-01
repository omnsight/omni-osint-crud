## Omni OSINT CRUD
[![codecov](https://codecov.io/github/omnsight/omni-osint-crud/graph/badge.svg?token=2LDW67VWXE)](https://codecov.io/github/omnsight/omni-osint-crud)

A CRUD service for managing Open-Source Intelligence (OSINT) data, providing a RESTful API to handle entities like Persons, Organizations, and Events.

### 🚀 Features

- CRUD operations for OSINT entities (Person, Organization, Event, etc.).
- Health check endpoint for monitoring service status.
- Automatic API documentation via OpenAPI (Swagger).
- Generated TypeScript client for seamless frontend integration.

### 🛠 Tech Stack

- **Backend:** Python, FastAPI
- **Database:** ArangoDB, Redis
- **Frontend:** TypeScript
- **Tooling:** uv, Docker, Pydantic

## 📦 Getting Started

### Prerequisites

- Python 3.10+
- Docker
- uv

### Installation

Clone the repo:

```bash
git clone https://github.com/omnsight/omni-osint-crud.git
cd omni-osint-crud
```

Install Python dependencies:

```bash
uv lock --upgrade
uv sync --extra dev
```

Install client dependencies:

```bash
cd client
npm install
cd ..
```

## ⚙️ Configuration

Update configurations in [`.env`](.env)

## 📖 Usage

### Running the Service

Start the backend services:

```bash
docker-compose up -d --build --wait
```

Stop the backend services when you're done:

```bash
docker-compose down
```

### Using the Client

Refer to [client/README.md](client/README.md) for [client](https://www.npmjs.com/package/omni-osint-crud-client) setup and usage.

## Local Development

Refer to [DEVELOPMENT.md](DEVELOPMENT.md) for local development setup.

## 📄 License

Distributed under the Apache-2.0 License. See [LICENSE](./LICENSE) for more information.
