# Thinking Guides

Use these guides before and during implementation to avoid shallow fixes and mock-only confidence.

## Always-On Engineering Contract

These rules are mandatory for every implementation task. They are repeated here because Trellis agents commonly read `guides/index.md` as a shared entry point.

- Requirement analysis comes before coding. Identify affected layers, runtime dependencies, and the first test that will prove the behavior.
- New feature and behavior-changing work defaults to TDD. Write or update a failing behavior/regression test before implementation unless an allowed exception is stated before coding.
- Allowed test-first exceptions are UI-only visual adjustment, prototype exploration, missing test framework with disproportionate setup cost, very small change already covered by quality gates, or initial reconnaissance needed to determine the test boundary.
- Mock-only confidence is not enough when the feature depends on real middleware, database, queue, cache, search, storage, browser runtime, or external HTTP.
- User-visible browser workflows require Playwright or the project's established real-browser E2E tool.
- Refactor only after the relevant behavior, integration, and E2E tests are green.
- Do not modify native Trellis skills to enforce these rules. Add project-local specs, workflow-state rules, or local skills instead.

## Available Guides

| Guide | Use When |
| --- | --- |
| [`requirement-analysis.md`](requirement-analysis.md) | Starting any non-trivial task or when requirements are unclear. |
| [`cross-layer-delivery.md`](cross-layer-delivery.md) | Work spans frontend, backend, persistence, or external services. |
| [`review-checklist.md`](review-checklist.md) | Before claiming implementation is complete. |

## Required Habit

Before changing a value, constant, API contract, test fixture, config key, or directory structure, search for existing references and sibling patterns.

```bash
rg "value_or_name_to_change"
```

If `rg` is unavailable, use the fastest available search tool.
