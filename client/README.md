# Omni OSINT CRUD Client

This directory contains the generated TypeScript client for the API.

## Usage

To use the client in your Node.js project, you can install it directly from GitHub. Add the following to your `package.json`:

```json
{
  "dependencies": {
    "omni-osint-crud-client": "latest"
  }
}
```

After installation, you can use the client in your application as shown below:

```typescript
import { OpenAPI, HealthService, HealthCheck } from 'omni-osint-crud/client';

// Configure the API client
OpenAPI.BASE = 'http://localhost:8000'; // Adjust if your server runs on a different host/port
// Configure authentication (e.g., with a bearer token)
OpenAPI.TOKEN = 'your-bearer-token';

async function main() {
  try {
    console.log('Performing health check...');
    const healthStatus: HealthCheck = await HealthService.healthCheck();
    console.log('Health Check Status:', healthStatus);
  } catch (error) {
    console.error('Error during health check:', error);
  }
}

main();
```

## 💻 Setup Client

Located in `client/` directory.

Install client dependencies:
```bash
npm install
```

Generate client:
```bash
npm run generate
```

## 👨‍💻 Client Development

Run unit tests:
```bash
docker compose up -d --wait
cd client
npm run test
cd ..
docker compose down
```

Build the client:
```bash
npm run build
```

Publish the client:
```bash
npm login
npm publish
```
