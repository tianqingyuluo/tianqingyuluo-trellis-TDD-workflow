# Persistence And Middleware

## Persistence Changes

Database-related changes must consider:

- schema migration order;
- data backfill or default values;
- indexes and query plans for new access patterns;
- transactions and isolation;
- rollback safety;
- cleanup of test data.

## Required Tests

Use real database or migration tests when changing:

- migrations;
- ORM mappings;
- transaction behavior;
- query filters, joins, pagination, or ordering;
- constraints and uniqueness;
- serialization into stored fields.

Mocks can supplement these tests, but cannot replace them for persistence risk.

## Middleware

When behavior depends on middleware, tests must include that middleware.

Examples:

- auth/session middleware;
- request body parsing;
- CSRF or CORS behavior;
- rate limiting;
- tenant or locale injection;
- error formatting middleware.

Do not call a handler directly and claim middleware-dependent behavior is covered.

## Runtime Configuration

Configuration used by tests must be explicit:

- environment variables documented;
- service ports deterministic or discovered;
- secrets injected securely;
- CI setup clear enough to reproduce locally.
