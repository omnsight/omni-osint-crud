/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Event } from './Event';
import type { Organization } from './Organization';
import type { Person } from './Person';
import type { Relation } from './Relation';
import type { Source } from './Source';
import type { Website } from './Website';
export type Entities = {
    /**
     * A list of events related to the entity.
     */
    events?: Array<Event>;
    /**
     * A list of sources related to the entity.
     */
    sources?: Array<Source>;
    /**
     * A list of persons related to the entity.
     */
    persons?: Array<Person>;
    /**
     * A list of organizations related to the entity.
     */
    organizations?: Array<Organization>;
    /**
     * A list of websites related to the entity.
     */
    websites?: Array<Website>;
    /**
     * A list of relations related to the entity.
     */
    relations?: Array<Relation>;
};

