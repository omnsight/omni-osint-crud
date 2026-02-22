import { HealthService, OpenAPI } from '..';

describe('HealthService', () => {
  beforeAll(() => {
    OpenAPI.BASE = 'http://localhost:8000';
    const payload = {
      sub: 'test-user-id-123',
      roles: ['admin'],
    };
    const header = Buffer.from(JSON.stringify({ alg: 'none' })).toString('base64url');
    const claims = Buffer.from(JSON.stringify(payload)).toString('base64url');
    const token = `${header}.${claims}.`;
    OpenAPI.TOKEN = token;
  });

  it('should return a health check', async () => {
    const healthCheck = await HealthService.healthCheck();
    expect(healthCheck).toBeDefined();
    expect(healthCheck.status).toEqual('ok');
  });
});
