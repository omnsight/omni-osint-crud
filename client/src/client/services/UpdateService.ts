/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Event } from '../models/Event';
import type { EventMainData } from '../models/EventMainData';
import type { Organization } from '../models/Organization';
import type { OrganizationMainData } from '../models/OrganizationMainData';
import type { Permissive } from '../models/Permissive';
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
export class UpdateService {
    /**
     * Update Person
     * @param id
     * @param requestBody
     * @param authorization
     * @returns Person Successful Response
     * @throws ApiError
     */
    public static updatePersonUpdatePersonIdPut(
        id: string,
        requestBody: PersonMainData,
        authorization?: (string | null),
    ): CancelablePromise<Person> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/update/person/{id}',
            path: {
                'id': id,
            },
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
     * Update Person Permissions
     * @param id
     * @param requestBody
     * @param authorization
     * @returns Person Successful Response
     * @throws ApiError
     */
    public static updatePersonPermissionsUpdatePersonIdPermissionsPut(
        id: string,
        requestBody: Permissive,
        authorization?: (string | null),
    ): CancelablePromise<Person> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/update/person/{id}/permissions',
            path: {
                'id': id,
            },
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
     * Update Organization
     * @param id
     * @param requestBody
     * @param authorization
     * @returns Organization Successful Response
     * @throws ApiError
     */
    public static updateOrganizationUpdateOrganizationIdPut(
        id: string,
        requestBody: OrganizationMainData,
        authorization?: (string | null),
    ): CancelablePromise<Organization> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/update/organization/{id}',
            path: {
                'id': id,
            },
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
     * Update Organization Permissions
     * @param id
     * @param requestBody
     * @param authorization
     * @returns Organization Successful Response
     * @throws ApiError
     */
    public static updateOrganizationPermissionsUpdateOrganizationIdPermissionsPut(
        id: string,
        requestBody: Permissive,
        authorization?: (string | null),
    ): CancelablePromise<Organization> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/update/organization/{id}/permissions',
            path: {
                'id': id,
            },
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
     * Update Event
     * @param id
     * @param requestBody
     * @param authorization
     * @returns Event Successful Response
     * @throws ApiError
     */
    public static updateEventUpdateEventIdPut(
        id: string,
        requestBody: EventMainData,
        authorization?: (string | null),
    ): CancelablePromise<Event> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/update/event/{id}',
            path: {
                'id': id,
            },
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
     * Update Event Permissions
     * @param id
     * @param requestBody
     * @param authorization
     * @returns Event Successful Response
     * @throws ApiError
     */
    public static updateEventPermissionsUpdateEventIdPermissionsPut(
        id: string,
        requestBody: Permissive,
        authorization?: (string | null),
    ): CancelablePromise<Event> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/update/event/{id}/permissions',
            path: {
                'id': id,
            },
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
     * Update Website
     * @param id
     * @param requestBody
     * @param authorization
     * @returns Website Successful Response
     * @throws ApiError
     */
    public static updateWebsiteUpdateWebsiteIdPut(
        id: string,
        requestBody: WebsiteMainData,
        authorization?: (string | null),
    ): CancelablePromise<Website> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/update/website/{id}',
            path: {
                'id': id,
            },
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
     * Update Website Permissions
     * @param id
     * @param requestBody
     * @param authorization
     * @returns Website Successful Response
     * @throws ApiError
     */
    public static updateWebsitePermissionsUpdateWebsiteIdPermissionsPut(
        id: string,
        requestBody: Permissive,
        authorization?: (string | null),
    ): CancelablePromise<Website> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/update/website/{id}/permissions',
            path: {
                'id': id,
            },
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
     * Update Source
     * @param id
     * @param requestBody
     * @param authorization
     * @returns Source Successful Response
     * @throws ApiError
     */
    public static updateSourceUpdateSourceIdPut(
        id: string,
        requestBody: SourceMainData,
        authorization?: (string | null),
    ): CancelablePromise<Source> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/update/source/{id}',
            path: {
                'id': id,
            },
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
     * Update Source Permissions
     * @param id
     * @param requestBody
     * @param authorization
     * @returns Source Successful Response
     * @throws ApiError
     */
    public static updateSourcePermissionsUpdateSourceIdPermissionsPut(
        id: string,
        requestBody: Permissive,
        authorization?: (string | null),
    ): CancelablePromise<Source> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/update/source/{id}/permissions',
            path: {
                'id': id,
            },
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
     * Update Relation
     * @param id
     * @param requestBody
     * @param authorization
     * @returns Relation Successful Response
     * @throws ApiError
     */
    public static updateRelationUpdateRelationIdPut(
        id: string,
        requestBody: RelationMainData,
        authorization?: (string | null),
    ): CancelablePromise<Relation> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/update/relation/{id}',
            path: {
                'id': id,
            },
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
     * Update Relation Permissions
     * @param id
     * @param requestBody
     * @param authorization
     * @returns Relation Successful Response
     * @throws ApiError
     */
    public static updateRelationPermissionsUpdateRelationIdPermissionsPut(
        id: string,
        requestBody: Permissive,
        authorization?: (string | null),
    ): CancelablePromise<Relation> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/update/relation/{id}/permissions',
            path: {
                'id': id,
            },
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
