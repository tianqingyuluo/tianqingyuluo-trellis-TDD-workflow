#!/usr/bin/env python3
"""Install stable rigorous workflow injection into a Trellis project."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path


START = "<!-- RIGOROUS_AI_DEV:START -->"
END = "<!-- RIGOROUS_AI_DEV:END -->"
STATE_START = "<!-- RIGOROUS_AI_DEV_WORKFLOW_STATE:START -->"
STATE_END = "<!-- RIGOROUS_AI_DEV_WORKFLOW_STATE:END -->"

WORKFLOW_BLOCK = f"""{START}

## Rigorous AI Development Contract

This project installed the `rigorous-ai-dev` Trellis workflow. These rules are mandatory and apply even when a task looks small:

- Requirement analysis before coding: identify affected layers, runtime dependencies, and the first test that proves the behavior.
- TDD by default: write or update a failing behavior/regression test before implementation where practical.
- Real integration is required when behavior depends on databases, middleware, queues, caches, search, storage, browser runtime, external HTTP, auth, or provider APIs. Mock-only tests do not prove these paths.
- Browser/user-visible workflows require Playwright or the project's established real-browser E2E tool against a real app/backend or documented local equivalent.
- Refactor only after relevant unit/component, real integration, and E2E tests are green.
- Do not modify native Trellis skills. Add project-local specs, workflow-state rules, or project-local skills instead.

Before implementation, read:

- `.trellis/spec/shared/index.md`
- `.trellis/spec/shared/workflow-discipline.md`
- `.trellis/spec/shared/tdd-and-testing.md`
- `.trellis/spec/shared/real-integration.md`
- `.trellis/spec/frontend/e2e-playwright.md` for browser workflows
- `.trellis/spec/shared/trellis-context-injection.md` when changing Trellis setup

During final reporting, explicitly list unit/component, real integration, E2E, lint/typecheck, and any skipped checks with reasons.

{END}"""

WORKFLOW_STATE_BLOCK = f"""{STATE_START}
**Rigorous AI development contract (mandatory)**: before implementation, do requirement analysis and identify affected layers, runtime dependencies, and the first behavior/regression test. Prefer TDD: write or update a failing test before code where practical. Mock-only tests are not enough when behavior depends on databases, middleware, queues, caches, search, storage, browser runtime, external HTTP, auth, or provider APIs. Browser/user-visible workflows require Playwright or the project's established real-browser E2E tool against a real app/backend or documented local equivalent. Refactor only after relevant unit/component, real integration, and E2E tests are green. Do not modify native Trellis skills; use project-local specs, workflow-state rules, or local skills instead.
{STATE_END}"""

WORKFLOW_STATE_RE = re.compile(
    r"(?ms)(^\[workflow-state:([^\]]+)\]\n)(.*?)(^\[/workflow-state:\2\]\s*)"
)

SKILL_TARGETS = [
    ".agents/skills",
    ".codex/skills",
    ".claude/skills",
    ".cursor/skills",
    ".opencode/skills",
    ".kiro/skills",
    ".gemini/skills",
    ".qoder/skills",
    ".codebuddy/skills",
    ".github/skills",
    ".factory/skills",
    ".pi/skills",
    ".kilocode/skills",
    ".agent/skills",
    ".windsurf/skills",
]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def replace_managed_block(text: str, block: str) -> str:
    if START in text and END in text:
        before, rest = text.split(START, 1)
        _, after = rest.split(END, 1)
        return before.rstrip() + "\n\n" + block + after
    return text.rstrip() + "\n\n" + block + "\n"


def replace_state_block(body: str) -> str:
    if STATE_START in body and STATE_END in body:
        before, rest = body.split(STATE_START, 1)
        _, after = rest.split(STATE_END, 1)
        return before.rstrip() + "\n" + WORKFLOW_STATE_BLOCK + after
    return body.rstrip() + "\n" + WORKFLOW_STATE_BLOCK + "\n"


def inject_workflow_state_blocks(text: str) -> tuple[str, int]:
    count = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        open_tag, _status, body, close_tag = match.groups()
        return open_tag + replace_state_block(body) + close_tag

    updated = WORKFLOW_STATE_RE.sub(repl, text)
    return updated, count


def install_workflow(project: Path) -> None:
    workflow = project / ".trellis" / "workflow.md"
    if not workflow.exists():
        raise FileNotFoundError(f"Missing Trellis workflow file: {workflow}")
    text = workflow.read_text(encoding="utf-8")
    text, injected_count = inject_workflow_state_blocks(text)
    if injected_count == 0:
        raise ValueError(f"No [workflow-state:*] blocks found in {workflow}")
    text = replace_managed_block(text, WORKFLOW_BLOCK)
    workflow.write_text(text, encoding="utf-8")


def install_skill(project: Path, force_all_targets: bool) -> list[Path]:
    source = repo_root() / "optional-project-local-skills" / "project-rigorous-dev"
    if not source.exists():
        raise FileNotFoundError(f"Missing source skill: {source}")

    installed: list[Path] = []
    for rel_target in SKILL_TARGETS:
        target_parent = project / rel_target
        if not force_all_targets and not target_parent.exists():
            continue
        target_parent.mkdir(parents=True, exist_ok=True)
        target = target_parent / "project-rigorous-dev"
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source, target)
        installed.append(target)
    return installed


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Install rigorous-ai-dev workflow-state injection and local skill into a Trellis project."
    )
    parser.add_argument(
        "project",
        nargs="?",
        default=".",
        help="Target Trellis project root. Defaults to current directory.",
    )
    parser.add_argument(
        "--all-skill-targets",
        action="store_true",
        help="Create every known platform skill directory instead of only copying to directories that already exist.",
    )
    args = parser.parse_args()

    project = Path(args.project).resolve()
    try:
        install_workflow(project)
        installed = install_skill(project, args.all_skill_targets)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"Updated workflow-state injection: {project / '.trellis' / 'workflow.md'}")
    if installed:
        print("Installed project-local skill:")
        for path in installed:
            print(f"- {path}")
    else:
        print("No platform skill directories existed; workflow-state injection was still installed.")
    print("Restart or reload the AI session so hooks/preludes pick up the new workflow and skill.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
