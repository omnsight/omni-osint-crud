/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { EntityConnectionRequest } from '../models/EntityConnectionRequest';
import type { Event } from '../models/Event';
import type { EventMainData } from '../models/EventMainData';
import type { Organization } from '../models/Organization';
import type { OrganizationMainData } from '../models/OrganizationMainData';
import type { OsintView } from '../models/OsintView';
import type { OsintViewMainData } from '../models/OsintViewMainData';
import type { Permissive } from '../models/Permissive';
import type { Person } from '../models/Person';
import type { PersonMainData } from '../models/PersonMainData';
import type { Relation } from '../models/Relation';
import type { RelationMainData } from '../models/RelationMainData';
import type { Source } from '../models/Source';
import type { SourceMainData } from '../models/SourceMainData';
import type { ViewConfig } from '../models/ViewConfig';
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
     * @param includePending
     * @param authorization
     * @returns Person Successful Response
     * @throws ApiError
     */
    public static updatePerson(
        id: string,
        requestBody: PersonMainData,
        includePending: boolean = false,
        authorization?: (string | null),
    ): CancelablePromise<Person> {
        return __request(OpenAPI, {
            method: 'PUT',
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
     * @param includePending
     * @param authorization
     * @returns Organization Successful Response
     * @throws ApiError
     */
    public static updateOrganization(
        id: string,
        requestBody: OrganizationMainData,
        includePending: boolean = false,
        authorization?: (string | null),
    ): CancelablePromise<Organization> {
        return __request(OpenAPI, {
            method: 'PUT',
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
     * @param includePending
     * @param authorization
     * @returns Event Successful Response
     * @throws ApiError
     */
    public static updateEvent(
        id: string,
        requestBody: EventMainData,
        includePending: boolean = false,
        authorization?: (string | null),
    ): CancelablePromise<Event> {
        return __request(OpenAPI, {
            method: 'PUT',
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
     * @param includePending
     * @param authorization
     * @returns Website Successful Response
     * @throws ApiError
     */
    public static updateWebsite(
        id: string,
        requestBody: WebsiteMainData,
        includePending: boolean = false,
        authorization?: (string | null),
    ): CancelablePromise<Website> {
        return __request(OpenAPI, {
            method: 'PUT',
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
     * @param includePending
     * @param authorization
     * @returns Source Successful Response
     * @throws ApiError
     */
    public static updateSource(
        id: string,
        requestBody: SourceMainData,
        includePending: boolean = false,
        authorization?: (string | null),
    ): CancelablePromise<Source> {
        return __request(OpenAPI, {
            method: 'PUT',
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
     * @param includePending
     * @param authorization
     * @returns Relation Successful Response
     * @throws ApiError
     */
    public static updateRelation(
        id: string,
        requestBody: RelationMainData,
        includePending: boolean = false,
        authorization?: (string | null),
    ): CancelablePromise<Relation> {
        return __request(OpenAPI, {
            method: 'PUT',
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
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Connect Entity To View
     * @param id
     * @param requestBody
     * @param authorization
     * @returns OsintView Successful Response
     * @throws ApiError
     */
    public static connectEntityToView(
        id: string,
        requestBody: EntityConnectionRequest,
        authorization?: (string | null),
    ): CancelablePromise<OsintView> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/view/{id}/entities',
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
     * Update View
     * @param id
     * @param requestBody
     * @param authorization
     * @returns OsintView Successful Response
     * @throws ApiError
     */
    public static updateView(
        id: string,
        requestBody: OsintViewMainData,
        authorization?: (string | null),
    ): CancelablePromise<OsintView> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/view/{id}',
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
    public static updatePersonPermissions(
        id: string,
        requestBody: Permissive,
        authorization?: (string | null),
    ): CancelablePromise<Person> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/person/{id}/permissions',
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
    public static updateOrganizationPermissions(
        id: string,
        requestBody: Permissive,
        authorization?: (string | null),
    ): CancelablePromise<Organization> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/organization/{id}/permissions',
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
    public static updateEventPermissions(
        id: string,
        requestBody: Permissive,
        authorization?: (string | null),
    ): CancelablePromise<Event> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/event/{id}/permissions',
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
    public static updateWebsitePermissions(
        id: string,
        requestBody: Permissive,
        authorization?: (string | null),
    ): CancelablePromise<Website> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/website/{id}/permissions',
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
    public static updateSourcePermissions(
        id: string,
        requestBody: Permissive,
        authorization?: (string | null),
    ): CancelablePromise<Source> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/source/{id}/permissions',
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
    public static updateRelationPermissions(
        id: string,
        requestBody: Permissive,
        authorization?: (string | null),
    ): CancelablePromise<Relation> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/relation/{id}/permissions',
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
     * Add View Config
     * @param id
     * @param requestBody
     * @param authorization
     * @returns OsintView Successful Response
     * @throws ApiError
     */
    public static addViewConfig(
        id: string,
        requestBody: ViewConfig,
        authorization?: (string | null),
    ): CancelablePromise<OsintView> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/view/{id}/configs',
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
     * Update View Permissions
     * @param id
     * @param requestBody
     * @param authorization
     * @returns OsintView Successful Response
     * @throws ApiError
     */
    public static updateViewPermissions(
        id: string,
        requestBody: Permissive,
        authorization?: (string | null),
    ): CancelablePromise<OsintView> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/view/{id}/permissions',
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
