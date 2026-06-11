# Frontend Development Specs

Frontend rules apply to UI, browser behavior, forms, state, routes, visual workflows, accessibility, and E2E tests.

## Pre-Development Checklist

- [ ] Read [`ui-and-component-rules.md`](ui-and-component-rules.md).
- [ ] Read [`state-and-data-contracts.md`](state-and-data-contracts.md) for data-fetching, forms, and client/server contract work.
- [ ] Read [`e2e-playwright.md`](e2e-playwright.md) for user-visible workflow testing.
- [ ] Read [`../shared/tdd-and-testing.md`](../shared/tdd-and-testing.md).
- [ ] For cross-layer changes, read [`../guides/cross-layer-delivery.md`](../guides/cross-layer-delivery.md).

## Quality Check

- [ ] User-visible behavior has component or E2E coverage.
- [ ] Playwright or equivalent E2E tests cover critical flows.
- [ ] Frontend tests do not rely on mocked backend data when the task is about frontend/backend integration.
- [ ] UI states cover loading, empty, error, success, and permission-denied states where relevant.
- [ ] Text and layout remain usable across desktop and mobile viewport sizes.

## Forbidden Patterns

- Treating a mocked network response as proof that the real product workflow works.
- Hiding API contract mismatches with frontend-only fallback data.
- Adding visual complexity that harms the primary workflow.
- Ignoring accessibility and keyboard behavior for interactive controls.
