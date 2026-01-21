/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Represents an organization.
 */
export type Organization = {
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
    /**
     * Owner of the document
     */
    owner?: string;
    /**
     * Users/Roles with read access
     */
    read?: Array<string>;
    /**
     * Users/Roles with write access
     */
    write?: Array<string>;
    /**
     * ArangoDB document ID
     */
    _id?: (string | null);
    /**
     * ArangoDB document key
     */
    _key?: (string | null);
    /**
     * ArangoDB document revision
     */
    _rev?: (string | null);
};

