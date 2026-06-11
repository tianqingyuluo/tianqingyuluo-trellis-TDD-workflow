# API And Service Contracts

## API Contracts

When adding or changing an endpoint, document or infer:

- HTTP method and path;
- request params, query, headers, and body;
- response body for success and failure;
- status codes;
- auth/session requirements;
- idempotency and retry behavior.

## Validation

Validate at the boundary closest to untrusted input. Do not rely on downstream exceptions as normal validation.

## Error Handling

Errors should:

- preserve the root cause for logs or diagnostics;
- return safe, user-appropriate messages;
- expose stable error codes where clients need branching behavior;
- avoid leaking secrets, tokens, internal URLs, or database internals.

## Contract Tests

When clients depend on an API contract:

- add API-level tests for status codes and response shape;
- add frontend or E2E coverage for user-visible flows;
- update OpenAPI or API docs if the project maintains them;
- verify serialization details such as dates, nulls, enums, and pagination.
