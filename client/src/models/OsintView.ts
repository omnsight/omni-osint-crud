/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ViewConfig } from './ViewConfig';
export type OsintView = {
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
     * Name of the view
     */
    name?: (string | null);
    /**
     * Description of the view
     */
    description?: (string | null);
    /**
     * List of view configurations
     */
    configs?: (Array<ViewConfig> | null);
};

