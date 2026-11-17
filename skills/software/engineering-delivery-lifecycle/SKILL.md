---
name: engineering-delivery-lifecycle
description: Coordinate software delivery from problem definition and specification through planning, incremental implementation, verification, review, and release.
---

# Engineering Delivery Lifecycle

## Workflow

Turn the request into outcomes, acceptance criteria, and non-goals. Inspect the repository before asking questions already answered by source. For non-trivial changes, record decisions and a task plan with files, interfaces, and checks. Implement one vertical slice at a time. Use tests for fast feedback, diagnose failures systematically, and review against both spec and repository standards. Verify final diff, test output, artifact, and rollback path. Pause at destructive or externally visible operations requiring approval.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve unrelated behavior and existing project conventions.
- Verify important changes with an appropriate observable check.
- Report evidence, caveats, and unverified areas separately.
