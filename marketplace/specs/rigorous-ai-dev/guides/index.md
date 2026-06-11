# Thinking Guides

Use these guides before and during implementation to avoid shallow fixes and mock-only confidence.

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
