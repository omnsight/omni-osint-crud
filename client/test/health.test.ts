import { client } from '../src/client.gen';
import { healthCheck } from '../src/sdk.gen';

describe('HealthService', () => {
  beforeAll(() => {
    const payload = {
      sub: 'test-user-id-123',
      roles: ['admin'],
    };
    const header = Buffer.from(JSON.stringify({ alg: 'none' })).toString('base64url');
    const claims = Buffer.from(JSON.stringify(payload)).toString('base64url');
    const token = `${header}.${claims}.`;

    client.setConfig({
      baseURL: "http://localhost:8000",
      withCredentials: true,
    });
    client.instance.interceptors.request.use((config) => {
      config.headers['Authorization'] = `Bearer ${token}`;
      return config;
    });
  });

  it('should return a health check', async () => {
    const {data, error, status} = await healthCheck();
    console.log(data, error, status);
    expect(data).toBeDefined();
    expect(status).toEqual(200);
  });
});
