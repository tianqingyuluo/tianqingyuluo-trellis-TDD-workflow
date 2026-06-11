# UI And Component Rules

## Component Boundaries

Components should expose domain intent:

- container components coordinate data and workflow state;
- presentational components render data and emit events;
- hooks encapsulate reusable client logic;
- route/page components compose the workflow.

Avoid components that fetch data, mutate global state, perform formatting, and handle complex UI interactions all in one place.

## Required UI States

For user-facing workflows, handle:

- loading;
- empty;
- success;
- validation errors;
- server errors;
- permission or auth failures;
- offline or retry states when relevant.

## Accessibility

Interactive UI must support:

- keyboard operation;
- focus visibility;
- accessible labels for icon-only controls;
- semantic HTML where possible;
- error messages tied to fields when forms are involved.

## Layout

Text must not overflow or overlap in supported viewport sizes. Controls should have stable dimensions where state changes could otherwise shift layout.

## Visual Verification

For visual or layout-heavy work, use screenshots or browser inspection before claiming completion. If Playwright is available, prefer screenshot-based checks for responsive states that are easy to regress.
