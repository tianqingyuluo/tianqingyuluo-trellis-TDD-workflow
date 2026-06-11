# TDD And Testing Requirements

## Test-Driven Development

For behavior changes, prefer this loop:

1. Write a failing test that captures the target behavior or regression.
2. Run the test and confirm it fails for the right reason.
3. Implement the minimum code to pass.
4. Run the targeted test and relevant surrounding tests.
5. Refactor with tests green.

If test-first is impractical, explicitly record why and add tests immediately after the implementation.

## Test Pyramid

Use the narrowest test that can prove the behavior, then add broader tests for boundary confidence:

- Unit tests for pure logic, parsing, validation, transformations, and edge cases.
- Component or API tests for framework behavior.
- Integration tests for database, middleware, service, cache, queue, external HTTP, file storage, and auth boundaries.
- E2E tests for user-visible workflows and cross-layer behavior.

## Mock Policy

Mocks are allowed for:

- isolating pure code;
- simulating rare error paths that are hard to produce safely;
- controlling time, randomness, or network failures;
- asserting that the code sends a request with the expected contract.

Mocks are not sufficient when:

- the feature's risk is in database schema, query semantics, transactions, migrations, or persistence;
- middleware, auth, cache, queue, or search behavior is central to the feature;
- frontend and backend contracts must be verified together;
- the user requested real integration;
- a previous mock-based test missed the bug.

## Evidence Rule

Every test added must have a clear claim:

- "This proves validation rejects X."
- "This proves the API serializes Y."
- "This proves the browser flow saves Z through the real backend."

Do not add tests that only assert implementation details without proving user or contract behavior.

## Regression Rule

For bugs, write a regression test that fails on the original bug before fixing it. If the bug involves a cross-layer contract, the regression must cover the boundary where the contract broke.
