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
     * Name of the organization
     */
    name?: (string | null);
    /**
     * When organization is founded (timestamp)
     */
    founded_at?: (number | null);
    /**
     * When organization is discovered (timestamp)
     */
    discovered_at?: (number | null);
    /**
     * When organization is last visited (timestamp)
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

