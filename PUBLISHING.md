# Publishing The Marketplace

## Do We Need GitHub?

For new projects to install this template with `trellis init --registry`, the marketplace must be reachable as a Git provider source. The usual path is a GitHub repository, but Trellis also supports GitLab and Bitbucket-style sources.

If the repository is public:

```bash
trellis init --registry gh:<org>/<repo>/marketplace --template rigorous-ai-dev
```

If this directory stays as a subdirectory inside a larger repository:

```bash
trellis init --registry gh:<org>/<repo>/trellis-template-marketplace/marketplace --template rigorous-ai-dev
```

For private repositories, make sure the local Git credentials can read the repository, or configure token-based access according to the Trellis/Giget environment supported by your Trellis version.

## Recommended Repository Shape

Prefer a dedicated repository whose root is this directory:

```text
<repo>/
+-- README.md
+-- PUBLISHING.md
+-- optional-project-local-skills/
`-- marketplace/
    +-- index.json
    `-- specs/
        `-- rigorous-ai-dev/
```

This keeps the install command short and avoids exposing unrelated project files as part of the registry source.

## Validate Before Publishing

From the repository root:

```bash
python3 -m json.tool marketplace/index.json >/dev/null
test -d marketplace/specs/rigorous-ai-dev
```

After pushing to GitHub, test in a temporary repository:

```bash
mkdir /tmp/trellis-template-test
cd /tmp/trellis-template-test
git init
trellis init --registry gh:<org>/<repo>/marketplace --template rigorous-ai-dev
find .trellis/spec -maxdepth 2 -type f | sort
```

Expected result: `.trellis/spec/` contains `backend/`, `frontend/`, `shared/`, `guides/`, and the template `README.md`.

## Versioning

Treat template IDs as a stable API. For normal additions, keep `id: "rigorous-ai-dev"` and document the change in the repository. For breaking rewrites, publish a new ID such as:

```json
{
  "id": "rigorous-ai-dev-v2",
  "type": "spec",
  "name": "Rigorous AI Development v2",
  "path": "marketplace/specs/rigorous-ai-dev-v2"
}
```

You can also pin installs to a Git tag:

```bash
trellis init --registry gh:<org>/<repo>/marketplace#v1 --template rigorous-ai-dev
```

## Optional Project-Local Skill

`optional-project-local-skills/project-rigorous-dev/` is intentionally outside `marketplace/specs/`. Copy it into a target project only if that project wants an extra auto-trigger skill:

```bash
cp -R optional-project-local-skills/project-rigorous-dev <target>/.agents/skills/
cp -R optional-project-local-skills/project-rigorous-dev <target>/.codex/skills/
cp -R optional-project-local-skills/project-rigorous-dev <target>/.claude/skills/
```

Use the platform directories that actually exist in the target project. Do not modify native Trellis skills.

## Stable Injection After Init

A spec template alone gives Trellis the rules, but it does not force every platform to inject those rules on every turn. For stable injection, run the post-init installer from the published template repository after `trellis init`:

```bash
python3 bin/install-rigorous-workflow.py /path/to/target-project
```

The installer:

- appends a managed rigorous workflow block to `.trellis/workflow.md` so workflow-state injection reminds the agent that new feature and behavior-changing work defaults to TDD, test-first exceptions must be stated before coding, real integration and Playwright E2E are required where relevant, and refactoring waits until tests are green;
- copies `project-rigorous-dev` into `.agents/skills/` and any existing platform skill directories;
- does not modify native Trellis skills.

After running it, start a new AI session or reload context so the platform sees the new workflow and skill files.
