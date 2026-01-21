/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { LocationData } from './LocationData';
export type EventMainData = {
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
};

