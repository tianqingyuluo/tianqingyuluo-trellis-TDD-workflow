---
name: project-rigorous-dev
description: |
  Use when a project installed the rigorous-ai-dev Trellis spec template and the user asks to implement, test, review, refactor, verify Trellis hook/prelude injection, or enforce TDD, real integration, and Playwright E2E rules.
---

# Project Rigorous Development

This is a project-local companion skill for repositories that installed the `rigorous-ai-dev` spec template. It does not replace native Trellis skills.

## Trigger Check

Use this skill when the task involves:

- implementing or changing behavior;
- adding tests or fixing test gaps;
- doing real integration or E2E verification;
- changing Trellis specs, hooks, agents, skills, or workflow files;
- reviewing whether native Trellis skills were modified.

## Required Reads

Before acting, read the relevant installed specs:

1. `.trellis/spec/shared/index.md`
2. `.trellis/spec/shared/workflow-discipline.md`
3. `.trellis/spec/shared/tdd-and-testing.md`
4. `.trellis/spec/shared/real-integration.md` when real services, middleware, databases, queues, caches, search, storage, browser runtime, or external HTTP are involved.
5. `.trellis/spec/shared/trellis-context-injection.md` when Trellis setup or project rules are involved.
6. `.trellis/spec/frontend/e2e-playwright.md` for browser/user-visible workflows.
7. `.trellis/spec/backend/index.md` or `.trellis/spec/frontend/index.md` for layer-specific work.

## Rules

- Do not modify native Trellis skills. Add or update project-local specs or this project-local skill instead.
- Confirm which specs were read before implementation.
- New feature and behavior-changing work defaults to TDD: write the failing test before implementation.
- Skip test-first only after naming one allowed exception before coding: UI-only visual adjustment better verified by screenshot/interaction, prototype exploration with rapidly changing requirements, missing test framework where setup is disproportionately costly, very small change already covered by quality gates, or initial codebase reconnaissance needed to determine the test boundary.
- Use real integration tests when behavior depends on real runtime boundaries.
- Use Playwright or the project's established real-browser E2E tool for user-visible workflows.
- Do not call mocked API or middleware tests "real integration".
- Refactor only after relevant behavior tests are green.

## Hook And Prelude Verification

When the task touches Trellis setup, run or request the equivalent checks:

```bash
python3 ./.trellis/scripts/get_context.py
python3 ./.trellis/scripts/get_context.py --mode phase
python3 ./.trellis/scripts/get_context.py --mode packages
python3 ./.trellis/scripts/task.py current --source
```

Then verify:

- session-start or prelude loads current task and specs;
- workflow-state is injected or available through the platform workflow;
- implement/check agents can read PRD and JSONL context where the platform supports it;
- platforms without hooks still have explicit instructions to read the specs.

## Output Format

Report:

```text
Specs read:
- ...

TDD/default workflow:
- Failing test first, or named exception:
- Replacement verification when exception used:

Tests/verification:
- Unit/component:
- Real integration:
- E2E:
- Lint/typecheck:

Trellis context:
- Hook/prelude status:
- Native skills modified: no

Remaining risks:
- ...
```
