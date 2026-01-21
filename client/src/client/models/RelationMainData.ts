/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type RelationMainData = {
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
};

