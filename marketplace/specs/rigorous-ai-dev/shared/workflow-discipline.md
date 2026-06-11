# Workflow Discipline

## Requirement Phase

Before implementation, the agent must:

1. Restate the user goal and identify the behavior that must change.
2. Identify affected layers and data boundaries.
3. Search the repository for existing patterns, constants, helpers, and tests.
4. Record assumptions and resolve blocking ambiguity before coding.
5. Decide which tests will prove the change.

Do not code first and retrofit intent later.

## Design Phase

Before writing code, define:

- the smallest user-visible behavior slice;
- inputs, outputs, and errors at each boundary;
- data transformations and ownership;
- runtime dependencies such as database, cache, queue, browser, file system, or external HTTP;
- rollback or fallback behavior when the change is risky.

For complex work, persist this in the task PRD, `info.md`, or a research note.

## Implementation Phase

Implementation follows this order:

1. Add or update tests that express the desired behavior.
2. Make the smallest code change that turns the tests green.
3. Add integration or E2E coverage for real boundaries.
4. Refactor only after the behavior tests are green.
5. Re-run the full relevant verification set.

## Refactoring Rule

Refactor after correctness is proven. During refactoring:

- keep behavior tests green;
- do not combine unrelated cleanup with feature behavior;
- extract shared functions or classes only when they reduce real duplication or clarify boundaries;
- avoid vague names such as `data`, `temp`, `helper`, or `utils` unless the surrounding domain already gives them precise meaning;
- keep single functions small enough to fit on one screen where practical. If a function grows beyond that, split it by domain responsibility rather than by arbitrary line count.

## Completion Rule

A task is not complete until:

- unit or component tests pass where relevant;
- integration tests pass for real dependencies where relevant;
- E2E tests pass for user-visible behavior where relevant;
- lint and type checks pass;
- the agent has checked whether specs need updates.
