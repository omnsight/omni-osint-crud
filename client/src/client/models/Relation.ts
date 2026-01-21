/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Represents a relationship between two entities.
 */
export type Relation = {
    /**
     * Name of the relation
     */
    name?: (string | null);
    /**
     * Confidence score
     */
    confidence?: (number | null);
    /**
     * Label
     */
    label?: (string | null);
    /**
     * Creation timestamp
     */
    created_at?: (number | null);
    /**
     * Update timestamp
     */
    updated_at?: (number | null);
    /**
     * Additional attributes
     */
    attributes?: (Record<string, any> | null);
    /**
     * Source document ID
     */
    _from?: (string | null);
    /**
     * Target document ID
     */
    _to?: (string | null);
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

