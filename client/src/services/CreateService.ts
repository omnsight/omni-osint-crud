/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Event } from '../models/Event';
import type { EventMainData } from '../models/EventMainData';
import type { Organization } from '../models/Organization';
import type { OrganizationMainData } from '../models/OrganizationMainData';
import type { OsintView } from '../models/OsintView';
import type { OsintViewMainData } from '../models/OsintViewMainData';
import type { Person } from '../models/Person';
import type { PersonMainData } from '../models/PersonMainData';
import type { Relation } from '../models/Relation';
import type { RelationMainData } from '../models/RelationMainData';
import type { Source } from '../models/Source';
import type { SourceMainData } from '../models/SourceMainData';
import type { Website } from '../models/Website';
import type { WebsiteMainData } from '../models/WebsiteMainData';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class CreateService {
    /**
     * Create Person
     * @param requestBody
     * @param authorization
     * @returns Person Successful Response
     * @throws ApiError
     */
    public static createPerson(
        requestBody: PersonMainData,
        authorization?: (string | null),
    ): CancelablePromise<Person> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/person',
            headers: {
                'authorization': authorization,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Create Organization
     * @param requestBody
     * @param authorization
     * @returns Organization Successful Response
     * @throws ApiError
     */
    public static createOrganization(
        requestBody: OrganizationMainData,
        authorization?: (string | null),
    ): CancelablePromise<Organization> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/organization',
            headers: {
                'authorization': authorization,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Create Event
     * @param requestBody
     * @param authorization
     * @returns Event Successful Response
     * @throws ApiError
     */
    public static createEvent(
        requestBody: EventMainData,
        authorization?: (string | null),
    ): CancelablePromise<Event> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/event',
            headers: {
                'authorization': authorization,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Create Website
     * @param requestBody
     * @param authorization
     * @returns Website Successful Response
     * @throws ApiError
     */
    public static createWebsite(
        requestBody: WebsiteMainData,
        authorization?: (string | null),
    ): CancelablePromise<Website> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/website',
            headers: {
                'authorization': authorization,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Create Source
     * @param requestBody
     * @param authorization
     * @returns Source Successful Response
     * @throws ApiError
     */
    public static createSource(
        requestBody: SourceMainData,
        authorization?: (string | null),
    ): CancelablePromise<Source> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/source',
            headers: {
                'authorization': authorization,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Create Relation
     * @param requestBody
     * @param authorization
     * @returns Relation Successful Response
     * @throws ApiError
     */
    public static createRelation(
        requestBody: RelationMainData,
        authorization?: (string | null),
    ): CancelablePromise<Relation> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/relation',
            headers: {
                'authorization': authorization,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Create View
     * @param requestBody
     * @param authorization
     * @returns OsintView Successful Response
     * @throws ApiError
     */
    public static createView(
        requestBody: OsintViewMainData,
        authorization?: (string | null),
    ): CancelablePromise<OsintView> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/view',
            headers: {
                'authorization': authorization,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
