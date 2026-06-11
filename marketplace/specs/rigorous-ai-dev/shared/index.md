# Shared Engineering Specs

Shared rules apply to any task that crosses layers, changes behavior, touches tests, or changes Trellis workflow behavior.

## Applies To

- Feature work that touches more than one layer.
- Bug fixes where the root cause may span API, storage, service, and UI boundaries.
- Test changes, fixture changes, CI changes, and E2E coverage.
- Changes to Trellis specs, local skills, hooks, or platform setup.

## Pre-Development Checklist

- [ ] Read [`workflow-discipline.md`](workflow-discipline.md).
- [ ] Read [`tdd-and-testing.md`](tdd-and-testing.md).
- [ ] Read [`real-integration.md`](real-integration.md) if the feature depends on databases, queues, caches, search, middleware, external HTTP, file storage, auth providers, or browser/runtime APIs.
- [ ] Read [`trellis-context-injection.md`](trellis-context-injection.md) when changing specs, tasks, platform setup, hooks, agents, skills, or workflow files.
- [ ] For cross-layer work, read [`../guides/cross-layer-delivery.md`](../guides/cross-layer-delivery.md).

## Required Quality Check

- [ ] Tests prove behavior, not just implementation details.
- [ ] Mock-only tests are not treated as complete when the feature depends on real integration.
- [ ] E2E coverage exists for user-visible workflows.
- [ ] The agent can name which specs it read and why.
- [ ] Any new convention discovered during the task is written back to project-local specs.

## Forbidden Shortcuts

- Skipping requirement analysis because the change "looks small".
- Replacing a real failing integration with a mock to get a green test.
- Calling mocked API or middleware results "real integration".
- Refactoring before the behavior-preserving test set is green.
- Editing native Trellis skills instead of adding project-local specs or skills.
