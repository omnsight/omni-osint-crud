/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type OrganizationMainData = {
    /**
     * Type of organization
     */
    type?: (string | null);
    /**
     * Name
     */
    name?: (string | null);
    /**
     * Founded timestamp
     */
    founded_at?: (number | null);
    /**
     * Discovered timestamp
     */
    discovered_at?: (number | null);
    /**
     * Last visited timestamp
     */
    last_visited?: (number | null);
    /**
     * Tags
     */
    tags?: (Array<string> | null);
    /**
     * Additional attributes
     */
    attributes?: (Record<string, any> | null);
};

