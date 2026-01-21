/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { HealthCheck } from '../models/HealthCheck';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class HealthService {
    /**
     * Health Check
     * @returns HealthCheck Successful Response
     * @throws ApiError
     */
    public static healthCheckHealthGet(): CancelablePromise<HealthCheck> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/health',
        });
    }
}
