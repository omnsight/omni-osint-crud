/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ViewMode } from './ViewMode';
import type { ViewUI } from './ViewUI';
export type ViewConfig = {
    /**
     * UI type for the view
     */
    ui: ViewUI;
    /**
     * Mode of the view
     */
    mode: ViewMode;
    /**
     * List of entity ids this view config highlights. For example, compare mode will render these entities in parallel highlighting their differences.
     */
    entities: Array<string>;
};

