# Backend Testing

## Minimum Backend Verification

For backend behavior changes:

- unit tests for pure logic;
- API/service tests for contracts;
- real integration tests for persistence, middleware, queues, caches, search, or external providers where relevant;
- regression tests for bugs.

## Running Services

When tests need real infrastructure:

- start the service explicitly with Docker Compose, testcontainers, local emulator, or equivalent;
- ensure tests fail clearly if the service is unavailable;
- isolate test data per run;
- clean up data deterministically.

## External APIs

Prefer real sandbox verification when the provider's behavior matters. Use recorded fixtures only after at least one real response has validated the contract.

## Reporting

The final task report must distinguish:

- unit tests run;
- integration tests run against real services;
- E2E tests run;
- tests not run and why.
