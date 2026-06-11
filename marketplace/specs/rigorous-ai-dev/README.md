# Rigorous AI Development Specs

These specs define a strict AI-assisted development workflow. They are meant to be installed into `.trellis/spec/` and then adapted to the real target repository.

## Core Rule

Do not let implementation outrun understanding. The agent must first analyze requirements, map the design, write or update tests, verify behavior with real systems where behavior depends on integration, and only then refactor.

## Installed Layers

| Layer | Purpose |
| --- | --- |
| [`backend/`](backend/index.md) | Backend architecture, API, persistence, real middleware, and service-level testing rules. |
| [`frontend/`](frontend/index.md) | UI, component, browser workflow, accessibility, and Playwright E2E rules. |
| [`shared/`](shared/index.md) | Cross-layer contracts, TDD, real integration, and Trellis context-injection rules. |
| [`guides/`](guides/index.md) | Thinking guides for requirement analysis, implementation sequencing, and review. |

## How Agents Should Use This Template

1. Read the relevant layer `index.md` before implementation.
2. Follow the linked checklist files, not only the index.
3. Add the relevant spec paths to the task's `implement.jsonl` and `check.jsonl` when the platform uses task-context JSONL.
4. If the platform has no sub-agent context hook, read these files directly before editing.
5. After fixing repeated bugs, update the project-local spec with the prevention rule.

## Project-Local Skills

If a project needs extra AI behavior, add a new project-local skill such as:

```text
.agents/skills/project-rigorous-dev/SKILL.md
.codex/skills/project-rigorous-dev/SKILL.md
.claude/skills/project-rigorous-dev/SKILL.md
```

Do not modify native Trellis skills. Native skills can change during `trellis update`, and local edits can be overwritten or become merge conflicts.
