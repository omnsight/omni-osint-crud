# Omni OSINT CRUD Client

This directory contains the generated [TypeScript client](https://www.npmjs.com/package/omni-osint-crud-client) for the Omni Osint CRUD API.

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
import { client } from 'omni-osint-crud-client/client';
import { healthCheck } from 'omni-osint-crud-client';

client.setConfig({
  baseURL: "http://localhost:8000",
  withCredentials: true,
});
client.instance.interceptors.request.use((config) => {
  config.headers['Authorization'] = `Bearer ${token}`;
  return config;
});

async function main() {
  console.log('Performing health check...');
  const { data, error, status } = await healthCheck();
  if (error) {
    console.error(`Error [${status}] during health check:`, error);
  } else {
    console.log('Health Check Status:', data.status);
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
