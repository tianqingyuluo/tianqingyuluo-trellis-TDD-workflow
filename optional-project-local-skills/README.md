# Optional Project-Local Skills

These skills are optional companions. They are not installed by `trellis init --registry`, because Trellis spec marketplaces should install only `.trellis/spec/` content.

Prefer running `../bin/install-rigorous-workflow.py` from the template repository. It copies this skill and patches `.trellis/workflow.md` so the rigorous rules are injected through workflow-state on every relevant turn.

Copy `project-rigorous-dev/` into the target project's local skill directories when you want auto-trigger behavior in addition to specs:

```bash
cp -R project-rigorous-dev <target>/.agents/skills/
cp -R project-rigorous-dev <target>/.codex/skills/
cp -R project-rigorous-dev <target>/.claude/skills/
```

Only copy to platform directories that exist in the target project. Do not edit native Trellis skills.
