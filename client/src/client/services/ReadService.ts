/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Event } from '../models/Event';
import type { Organization } from '../models/Organization';
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
     * @param authorization
     * @returns Person Successful Response
     * @throws ApiError
     */
    public static getPersonReadPersonIdGet(
        id: string,
        authorization?: (string | null),
    ): CancelablePromise<Person> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/read/person/{id}',
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
     * Get Organization
     * @param id
     * @param authorization
     * @returns Organization Successful Response
     * @throws ApiError
     */
    public static getOrganizationReadOrganizationIdGet(
        id: string,
        authorization?: (string | null),
    ): CancelablePromise<Organization> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/read/organization/{id}',
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
     * Get Event
     * @param id
     * @param authorization
     * @returns Event Successful Response
     * @throws ApiError
     */
    public static getEventReadEventIdGet(
        id: string,
        authorization?: (string | null),
    ): CancelablePromise<Event> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/read/event/{id}',
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
     * Get Website
     * @param id
     * @param authorization
     * @returns Website Successful Response
     * @throws ApiError
     */
    public static getWebsiteReadWebsiteIdGet(
        id: string,
        authorization?: (string | null),
    ): CancelablePromise<Website> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/read/website/{id}',
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
     * Get Source
     * @param id
     * @param authorization
     * @returns Source Successful Response
     * @throws ApiError
     */
    public static getSourceReadSourceIdGet(
        id: string,
        authorization?: (string | null),
    ): CancelablePromise<Source> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/read/source/{id}',
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
     * Get Relation
     * @param id
     * @param authorization
     * @returns Relation Successful Response
     * @throws ApiError
     */
    public static getRelationReadRelationIdGet(
        id: string,
        authorization?: (string | null),
    ): CancelablePromise<Relation> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/read/relation/{id}',
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
