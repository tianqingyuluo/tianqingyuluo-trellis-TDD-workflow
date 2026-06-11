# Cross-Layer Delivery Guide

## Map The Flow

For cross-layer features, map:

```text
User action -> UI state -> API request -> service -> persistence/provider -> response -> UI result
```

For each arrow, write down:

- input format;
- output format;
- validation owner;
- error behavior;
- test that proves the boundary.

## Boundary Failure Modes

Check for:

- date/time format mismatches;
- null or missing fields;
- enum drift;
- pagination and sorting mismatch;
- auth/session assumptions;
- stale frontend cache;
- transaction or race issues;
- external provider response differences.

## Test Strategy

Use a layered test set:

- unit tests for transformations;
- API or service tests for contract behavior;
- real integration tests for database, middleware, and provider boundaries;
- Playwright E2E for the critical user journey.

## Done Criteria

The task is not done until the same data survives the complete path that the user relies on.
