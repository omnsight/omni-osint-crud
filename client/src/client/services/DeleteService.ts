/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class DeleteService {
    /**
     * Delete Entity
     * @param id
     * @param authorization
     * @returns any Successful Response
     * @throws ApiError
     */
    public static deleteEntityDeleteEntityIdDelete(
        id: string,
        authorization?: (string | null),
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/delete/entity/{id}',
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
     * Delete Relation
     * @param id
     * @param authorization
     * @returns any Successful Response
     * @throws ApiError
     */
    public static deleteRelationDeleteRelationIdDelete(
        id: string,
        authorization?: (string | null),
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/delete/relation/{id}',
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
