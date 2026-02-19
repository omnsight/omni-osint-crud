# Client

This directory contains the generated TypeScript client for the API.

## Installation

```bash
cd client
npm install
```

## Usage

Here is a sample code snippet demonstrating how to use the client to invoke API calls.

```typescript
import { OpenAPI } from './src/client';

// Configure the base URL and a static token
OpenAPI.BASE = 'http://localhost:8000';
OpenAPI.TOKEN = 'your-static-jwt-token-here';

const health = await HealthService.healthCheckHealthGet();
console.log('Health check result:', health);
```

## Re-generating the Client

If the backend API changes, you can re-generate the client code:

1.  Ensure the backend is running or you have the latest `doc/openapi.json`.
2.  Run the generation script:

```bash
npm run generate
```
