# Real Integration Requirements

## Definition

Real integration means the test exercises the real boundary that the production feature depends on. It is not enough to mock the dependency and assert that a function was called.

## Required Real Integrations

Use real or locally realistic infrastructure for:

- database engines and migrations;
- ORMs and query builders;
- API routing and middleware stacks;
- auth/session middleware when behavior depends on it;
- cache, queue, object storage, search, or message broker clients;
- external HTTP integrations when response shape, auth, retry, rate limit, or error handling matters.

## Acceptable Local Forms

Depending on the project, real integration can use:

- Docker Compose services;
- testcontainers;
- local emulator services;
- temporary databases;
- local fake servers that implement the real protocol and response contract;
- sandbox API keys for third-party providers.

## External Service Policy

If the feature calls an external API:

- use a real sandbox or test account when available;
- use real API keys from secure environment variables, never committed files;
- verify response shape against real provider responses before release;
- record setup requirements in project docs or task research.

If a live call is too expensive or unsafe for every CI run, keep a contract test with recorded or simulated responses, but still run real-provider verification before claiming final integration confidence.

## Anti-Patterns

- Starting a mock server and calling that "real integration" when the production risk is the actual provider.
- Testing only repository methods while skipping migrations.
- Testing API handlers without middleware when middleware changes behavior.
- Running frontend E2E against mocked network data when the task is about backend integration.
- Marking tests green before starting required local infrastructure.

## Verification Checklist

- [ ] Required services are started before tests run.
- [ ] Tests fail clearly if infrastructure is missing.
- [ ] Test data setup and cleanup are deterministic.
- [ ] The test covers success and relevant failure modes.
- [ ] The final report distinguishes real integration tests from mock-based tests.
