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
    /**
     * Data creation timestamp
     */
    created_at?: (number | null);
    /**
     * Data update timestamp
     */
    updated_at?: (number | null);
};

