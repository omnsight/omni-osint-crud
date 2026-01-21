/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { LocationData } from './LocationData';
/**
 * Represents an event.
 */
export type Event = {
    /**
     * Type of event
     */
    type?: (string | null);
    /**
     * Location of the event
     */
    location?: (LocationData | null);
    /**
     * Title
     */
    title?: (string | null);
    /**
     * Description
     */
    description?: (string | null);
    /**
     * Timestamp when the event happened
     */
    happened_at?: (number | null);
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

