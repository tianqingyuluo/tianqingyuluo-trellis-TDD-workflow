# Review Checklist

Use this before claiming a task is complete.

## Requirements

- [ ] The implementation matches the PRD or latest user instruction.
- [ ] Assumptions are explicit.
- [ ] Out-of-scope work was not mixed in.

## Tests

- [ ] A failing test existed first, or the reason for not using test-first is documented.
- [ ] Unit/component tests cover local behavior.
- [ ] Real integration tests cover real dependencies where relevant.
- [ ] Playwright or equivalent E2E tests cover user-visible workflows.
- [ ] Mock-only coverage is not overstated.

## Integration

- [ ] Required services were actually started.
- [ ] API keys or secrets came from secure env vars.
- [ ] Middleware and auth behavior were included when relevant.
- [ ] Data setup and cleanup are deterministic.

## Trellis Context

- [ ] Relevant specs were read before implementation.
- [ ] Task JSONL includes relevant specs if the platform uses injected task context.
- [ ] Hook/prelude behavior is verified when Trellis setup changed.
- [ ] Native Trellis skills were not modified for project-specific rules.

## Maintainability

- [ ] Repeated code was extracted only when it reduces real duplication.
- [ ] Function and variable names express domain intent.
- [ ] Comments explain why, not what.
- [ ] Specs were updated with durable lessons from the task.
