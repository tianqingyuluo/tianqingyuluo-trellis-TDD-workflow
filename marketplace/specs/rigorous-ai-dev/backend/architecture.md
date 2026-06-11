# Backend Architecture

## Layering

Keep backend responsibilities explicit:

- Routes/controllers translate transport details into service calls.
- Services own business workflows and transaction boundaries.
- Repositories or data access modules own persistence details.
- Integration clients own third-party protocol details.
- Domain utilities own pure transformations and validation helpers.

Do not let UI or transport concerns leak into persistence code. Do not let database schema details leak into frontend contracts.

## Boundary Contracts

For every changed boundary, define:

- input shape;
- output shape;
- validation responsibility;
- error variants;
- retry and idempotency behavior when relevant;
- logging requirements.

## Naming

Names should expose domain intent. Avoid vague names such as:

- `data`
- `temp`
- `handler2`
- `processThing`
- `utils`

Use names that identify the business concept and boundary.

## Function Size

Keep functions short enough for a reviewer to understand without scrolling across multiple responsibilities. If one function parses input, checks auth, starts a transaction, calls a provider, transforms output, and formats a response, split it.

Split by responsibility:

- parsing and validation;
- authorization;
- transaction orchestration;
- provider call;
- response mapping.
