/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Represents a source of information.
 */
export type Source = {
    /**
     * Type of source
     */
    type?: (string | null);
    /**
     * URL
     */
    url?: (string | null);
    /**
     * Name
     */
    name?: (string | null);
    /**
     * Title
     */
    title?: (string | null);
    /**
     * Description
     */
    description?: (string | null);
    /**
     * Reliability score
     */
    reliability?: (number | null);
    /**
     * Creation timestamp
     */
    created_at?: (number | null);
    /**
     * Update timestamp
     */
    updated_at?: (number | null);
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

