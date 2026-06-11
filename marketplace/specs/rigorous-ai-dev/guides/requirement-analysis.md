# Requirement Analysis Guide

## Purpose

Prevent implementation from drifting away from the user's actual problem.

## Before Coding

Answer these questions:

- What user-visible behavior changes?
- What is the smallest useful slice?
- What does success look like in a test?
- Which layers are touched?
- Which dependencies are real runtime dependencies?
- Which assumptions are risky?
- What can be derived from existing code instead of asking the user?

## TDD Planning

Choose the first failing test:

- pure logic regression test;
- API contract test;
- component interaction test;
- integration test against real middleware or database;
- Playwright E2E workflow test.

Start narrow, but do not stop narrow if the real risk is at an integration boundary.

## Scope Control

Explicitly mark out of scope:

- unrelated refactors;
- future UX polish;
- unrequested platform support;
- broad architecture rewrites.

If implementation reveals a requirement defect, update the task PRD before continuing.
