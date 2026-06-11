# E2E Testing With Playwright

## Requirement

User-visible features must include E2E coverage for the critical workflow. Use Playwright by default when the project is a browser app. Cypress or another real browser automation tool is acceptable when it is already the project standard.

## What E2E Must Prove

E2E tests should prove the integrated workflow:

- app launches in a real browser;
- user can navigate to the relevant screen;
- user can perform the main action;
- frontend talks to the real backend or a documented local equivalent;
- persistent state or externally visible result is verified;
- errors are visible and actionable when relevant.

## Real Backend Rule

Do not mock network responses for E2E tests whose purpose is frontend/backend integration. If mocking is used for a narrow UI-only case, name the test accordingly and do not count it as real integration coverage.

## Playwright Setup Checklist

- [ ] Start the app server before tests.
- [ ] Start backend and required middleware/services before tests.
- [ ] Use deterministic seed data.
- [ ] Use isolated test users or sessions.
- [ ] Assert on visible behavior, not only hidden implementation state.
- [ ] Capture trace, screenshot, or video on failure when CI supports it.

## Viewport Coverage

For responsive workflows, test at least:

- one desktop viewport;
- one mobile or narrow viewport when the feature is used on mobile;
- any project-specific viewport where layout has historically broken.

## Selector Policy

Prefer resilient selectors:

- accessible roles and names;
- labels;
- text users actually see;
- stable `data-testid` only when semantic selectors are not practical.

Avoid brittle CSS selectors tied to implementation structure.

## Final Report

When reporting completion, include:

- Playwright command run;
- browser/project used;
- whether real backend/services were running;
- any skipped E2E coverage and reason.
