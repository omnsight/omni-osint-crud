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
import { OpenAPI, HealthService, ReadService } from './src/client';

// Configure the base URL of the API
OpenAPI.BASE = 'http://localhost:8000';

async function main() {
  try {
    // 1. Check API Health
    console.log('Checking API health...');
    const health = await HealthService.healthCheckHealthGet();
    console.log('Health check result:', health);

    // 2. Read a Person (example)
    // Replace 'some-id' with a valid ID
    // const person = await ReadService.getPersonReadPersonIdGet('some-id');
    // console.log('Person:', person);

  } catch (error) {
    console.error('Error invoking API:', error);
  }
}

main();
```

## Re-generating the Client

If the backend API changes, you can re-generate the client code:

1.  Ensure the backend is running or you have the latest `doc/openapi.json`.
2.  Run the generation script:

```bash
npm run generate
```
