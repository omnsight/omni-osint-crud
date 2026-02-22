/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class DeleteService {
    /**
     * Delete Relation
     * @param id
     * @param authorization
     * @returns any Successful Response
     * @throws ApiError
     */
    public static deleteRelation(
        id: string,
        authorization?: (string | null),
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/relation/{id}',
            path: {
                'id': id,
            },
            headers: {
                'authorization': authorization,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete View
     * @param id
     * @param authorization
     * @returns any Successful Response
     * @throws ApiError
     */
    public static deleteView(
        id: string,
        authorization?: (string | null),
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/view/{id}',
            path: {
                'id': id,
            },
            headers: {
                'authorization': authorization,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Entity
     * @param id
     * @param authorization
     * @returns any Successful Response
     * @throws ApiError
     */
    public static deleteEntity(
        id: string,
        authorization?: (string | null),
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/entity/{id}',
            path: {
                'id': id,
            },
            headers: {
                'authorization': authorization,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
