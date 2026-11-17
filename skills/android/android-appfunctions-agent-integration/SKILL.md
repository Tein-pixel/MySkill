---
name: android-appfunctions-agent-integration
description: Discover and expose safe Android app workflows through platform AppFunctions so system agents can invoke supported user actions.
---

# Android Appfunctions Agent Integration

## Workflow

Inspect target SDK, compile SDK, architecture, library availability, and current official API state. Select only bounded workflows the app already exposes, such as creating a note or controlling media. Do not expose broad database access, arbitrary file access, account secrets, financial details, or destructive bulk operations. Define typed inputs/outputs, validation, idempotency, permission checks, and visible failure handling. Write concise KDoc and metadata so calling agents understand the capability. Test discovery, registration, invalid input, authorization, and invocation on supported devices.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve unrelated behavior and existing project conventions.
- Verify important changes with an appropriate observable check.
- Report evidence, caveats, and unverified areas separately.
