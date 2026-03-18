/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Entities } from '../models/Entities';
import type { Event } from '../models/Event';
import type { Organization } from '../models/Organization';
import type { OsintView } from '../models/OsintView';
import type { Person } from '../models/Person';
import type { Relation } from '../models/Relation';
import type { Source } from '../models/Source';
import type { Website } from '../models/Website';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class ReadService {
    /**
     * Get Person
     * @param id
     * @param includePending
     * @param authorization
     * @returns Person Successful Response
     * @throws ApiError
     */
    public static getPerson(
        id: string,
        includePending: boolean = false,
        authorization?: (string | null),
    ): CancelablePromise<Person> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/person/{id}',
            path: {
                'id': id,
            },
            headers: {
                'authorization': authorization,
            },
            query: {
                'include_pending': includePending,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Organization
     * @param id
     * @param includePending
     * @param authorization
     * @returns Organization Successful Response
     * @throws ApiError
     */
    public static getOrganization(
        id: string,
        includePending: boolean = false,
        authorization?: (string | null),
    ): CancelablePromise<Organization> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/organization/{id}',
            path: {
                'id': id,
            },
            headers: {
                'authorization': authorization,
            },
            query: {
                'include_pending': includePending,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Event
     * @param id
     * @param includePending
     * @param authorization
     * @returns Event Successful Response
     * @throws ApiError
     */
    public static getEvent(
        id: string,
        includePending: boolean = false,
        authorization?: (string | null),
    ): CancelablePromise<Event> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/event/{id}',
            path: {
                'id': id,
            },
            headers: {
                'authorization': authorization,
            },
            query: {
                'include_pending': includePending,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Website
     * @param id
     * @param includePending
     * @param authorization
     * @returns Website Successful Response
     * @throws ApiError
     */
    public static getWebsite(
        id: string,
        includePending: boolean = false,
        authorization?: (string | null),
    ): CancelablePromise<Website> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/website/{id}',
            path: {
                'id': id,
            },
            headers: {
                'authorization': authorization,
            },
            query: {
                'include_pending': includePending,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Source
     * @param id
     * @param includePending
     * @param authorization
     * @returns Source Successful Response
     * @throws ApiError
     */
    public static getSource(
        id: string,
        includePending: boolean = false,
        authorization?: (string | null),
    ): CancelablePromise<Source> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/source/{id}',
            path: {
                'id': id,
            },
            headers: {
                'authorization': authorization,
            },
            query: {
                'include_pending': includePending,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Relation
     * @param id
     * @param includePending
     * @param authorization
     * @returns Relation Successful Response
     * @throws ApiError
     */
    public static getRelation(
        id: string,
        includePending: boolean = false,
        authorization?: (string | null),
    ): CancelablePromise<Relation> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/relation/{id}',
            path: {
                'id': id,
            },
            headers: {
                'authorization': authorization,
            },
            query: {
                'include_pending': includePending,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get View Entities
     * @param id
     * @param authorization
     * @returns Entities Successful Response
     * @throws ApiError
     */
    public static getViewEntities(
        id: string,
        authorization?: (string | null),
    ): CancelablePromise<Entities> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/view/{id}/entities',
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
     * Get View
     * @param id
     * @param authorization
     * @returns OsintView Successful Response
     * @throws ApiError
     */
    public static getView(
        id: string,
        authorization?: (string | null),
    ): CancelablePromise<OsintView> {
        return __request(OpenAPI, {
            method: 'GET',
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
     * Query Views
     * @param text
     * @param limit
     * @param offset
     * @param authorization
     * @returns OsintView Successful Response
     * @throws ApiError
     */
    public static queryViews(
        text?: (string | null),
        limit: number = 100,
        offset?: number,
        authorization?: (string | null),
    ): CancelablePromise<Array<OsintView>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/views',
            headers: {
                'authorization': authorization,
            },
            query: {
                'text': text,
                'limit': limit,
                'offset': offset,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
