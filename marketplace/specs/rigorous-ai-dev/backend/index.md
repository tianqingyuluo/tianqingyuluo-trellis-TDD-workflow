# Backend Development Specs

Backend rules apply to API, services, persistence, queues, caches, middleware, CLI backends, scheduled jobs, workers, and integrations.

## Pre-Development Checklist

- [ ] Read [`architecture.md`](architecture.md).
- [ ] Read [`api-and-service-contracts.md`](api-and-service-contracts.md) for API or service work.
- [ ] Read [`persistence-and-middleware.md`](persistence-and-middleware.md) for database, transaction, middleware, cache, queue, or auth work.
- [ ] Read [`testing.md`](testing.md) for backend tests and verification.
- [ ] Read [`../shared/real-integration.md`](../shared/real-integration.md) when external systems are involved.

## Quality Check

- [ ] API and service boundaries have explicit input/output/error contracts.
- [ ] Persistence changes are covered by real database or migration tests when relevant.
- [ ] Middleware-dependent behavior is tested with the real middleware stack.
- [ ] External service behavior is verified with sandbox/live contract evidence or a documented substitute.
- [ ] Logs and errors are actionable without leaking secrets.

## Forbidden Patterns

- Business behavior hidden in route glue with no service-level contract.
- Tests that bypass middleware for middleware-dependent features.
- Mocking database/query behavior for changes whose risk is persistence.
- Catch-all error handling that erases root cause or returns misleading success.
