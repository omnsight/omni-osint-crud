/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type WebsiteMainData = {
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
};

