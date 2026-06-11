# Trellis Context Injection And Local Customization

## Do Not Modify Native Skills

Do not edit native Trellis workflow skills for project-specific rules:

- `trellis-brainstorm`
- `trellis-before-dev`
- `trellis-check`
- `trellis-update-spec`
- `trellis-break-loop`
- `trellis-start`
- `trellis-continue`
- `trellis-finish-work`

Native files can be replaced or changed by future Trellis updates. Project conventions belong in `.trellis/spec/` or in a new project-local skill.

## Add Project-Local Skills Instead

When behavior needs a reusable AI capability, add a new skill, for example:

```text
.agents/skills/project-rigorous-dev/SKILL.md
.codex/skills/project-rigorous-dev/SKILL.md
.claude/skills/project-rigorous-dev/SKILL.md
```

The skill should:

- describe its trigger conditions in frontmatter;
- tell the agent which specs to read;
- avoid duplicating long-lived rules that already belong in `.trellis/spec/`;
- be committed as a project-local extension.

## Hook And Prelude Verification

Before relying on Trellis behavior, verify the target platform's context path:

- Session context: new sessions can see developer identity, git status, active tasks, and spec indexes.
- Workflow state: each user turn receives the current `[workflow-state:*]` instruction or equivalent prelude.
- Task context: implement/check agents can see PRD plus `implement.jsonl` or `check.jsonl` specs.
- Shell context: task commands resolve the same active task as the AI session when the platform supports session identity bridging.

## Platform Differences

Not every platform supports all hooks.

- Some platforms have SessionStart and UserPromptSubmit hooks.
- Some platforms have sub-agent context injection.
- Some platforms rely on agent pull-based preludes.
- Some platforms rely only on workflow files and skills.

Do not copy hook files blindly between platforms. Confirm the platform supports the event and that settings register the hook.

## Required Checks When Changing Trellis Setup

- [ ] Run the platform's documented context-start or start workflow.
- [ ] Run `python3 ./.trellis/scripts/get_context.py`.
- [ ] Run `python3 ./.trellis/scripts/get_context.py --mode phase`.
- [ ] Run `python3 ./.trellis/scripts/get_context.py --mode packages`.
- [ ] Confirm current task resolution with `python3 ./.trellis/scripts/task.py current --source` when a task exists.
- [ ] Confirm `implement.jsonl` and `check.jsonl` contain relevant spec paths for tasks using sub-agent context.

## Failure Rule

If specs are not being injected, do not continue as if they are. Fix the hook/prelude/settings path or explicitly read the required specs before editing.
