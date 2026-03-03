/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Represents a website.
 */
export type Website = {
    /**
     * URL
     */
    url?: (string | null);
    /**
     * Title of the website. Keep it short and clear.
     */
    title?: (string | null);
    /**
     * Brief description of the website. Keep it short and clear.
     */
    description?: (string | null);
    /**
     * When website is founded (timestamp)
     */
    founded_at?: (number | null);
    /**
     * When website is discovered (timestamp)
     */
    discovered_at?: (number | null);
    /**
     * When website is last visited (timestamp)
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

