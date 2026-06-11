# Rigorous AI Development Trellis Marketplace

This repository directory is a Trellis spec template marketplace. It seeds new projects with strict AI development conventions for requirement analysis, default TDD for new feature and behavior-changing work, real integration testing, Playwright E2E verification, safe refactoring after tests are green, and Trellis context-injection checks.

## Layout

```text
trellis-template-marketplace/
+-- PUBLISHING.md
+-- bin/
+-- optional-project-local-skills/
`-- marketplace/
    +-- index.json
    `-- specs/
        `-- rigorous-ai-dev/
            +-- README.md
            +-- backend/
            +-- frontend/
            +-- shared/
            `-- guides/
```

The contents of `marketplace/specs/rigorous-ai-dev/` are copied directly into the target project's `.trellis/spec/`.

The `optional-project-local-skills/` directory is not installed by `trellis init --registry`. It contains a companion skill that teams can copy into a project after init when they want an explicit auto-trigger workflow in addition to specs.

The `bin/install-rigorous-workflow.py` script is the post-init step that makes the workflow stable: it appends an always-on rigorous workflow block to the target project's `.trellis/workflow.md` and copies the companion local skill into existing platform skill directories. The injected block makes TDD the default for new feature and behavior-changing work, with only explicitly stated exceptions.

## Install From A Published Registry

After pushing this directory to a GitHub repository, install it with:

```bash
trellis init --registry gh:<org>/<repo>/marketplace --template rigorous-ai-dev
```

For an existing Trellis project, append only missing spec files:

```bash
trellis init --registry gh:<org>/<repo>/marketplace --template rigorous-ai-dev --append
```

Then install stable workflow-state injection:

```bash
python3 bin/install-rigorous-workflow.py /path/to/target-project
```

Pin a release or branch:

```bash
trellis init --registry gh:<org>/<repo>/marketplace#v1 --template rigorous-ai-dev
```

## Local Validation

Validate JSON before publishing:

```bash
python3 -m json.tool marketplace/index.json >/dev/null
```

Then test installation in a temporary repository using a local Git source or a pushed GitHub source. The registry path must point at the directory containing `index.json`.

## Boundaries

This marketplace intentionally contains only spec files. Do not place `.trellis/tasks/`, `.trellis/workspace/`, `.codex/`, `.claude/`, `.cursor/`, or other platform prompt directories in the template spec directory.

For project-specific skill behavior, add new project-local skills after initializing a project. Do not modify native Trellis skills such as `trellis-check` or `trellis-before-dev`.
