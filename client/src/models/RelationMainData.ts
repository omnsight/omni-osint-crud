/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type RelationMainData = {
    /**
     * Name of the relation used in database key (must be ascii letters)
     */
    name?: (string | null);
    /**
     * Confidence score
     */
    confidence?: (number | null);
    /**
     * Label name of the relation (can be any language) to display
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

