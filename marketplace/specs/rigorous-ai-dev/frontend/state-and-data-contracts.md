# State And Data Contracts

## Client/Server Contract

For data loaded from APIs:

- define the response shape;
- handle missing or null fields intentionally;
- validate or normalize at the boundary;
- keep date, enum, and pagination formats explicit;
- avoid duplicating backend business logic in the UI.

## State Ownership

Choose the narrowest state owner:

- local component state for purely local UI details;
- form state for user input and validation;
- server-state tools for cached remote data;
- global state only for data truly shared across distant parts of the app.

## Error Handling

User-facing errors should be actionable. Do not swallow backend errors and display stale success states.

## Testing

When frontend behavior depends on backend responses:

- use component tests for local rendering permutations;
- use API contract tests or E2E tests for real response shape;
- do not rely only on mocked data when the risk is contract mismatch.
