---
name: multi-agent-orchestration
description: Coordinate multiple AI agents with bounded tasks, independent context, explicit interfaces, and integration gates.
---

# Multi Agent Orchestration

## Workflow

Use parallel agents only when tasks are separable and shared-file conflicts are controlled. Give each worker a bounded objective, exact scope, inputs, outputs, and verification criteria. Use fresh context for independent reviews. Keep a coordinator responsible for architecture, integration, conflict resolution, and final checks. Treat worker output as untrusted until inspected and tested. Avoid redundant agents and parallel writes to the same files. Require approval before consequential external actions.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve unrelated behavior and existing project conventions.
- Verify important changes with an appropriate observable check.
- Report evidence, caveats, and unverified areas separately.
