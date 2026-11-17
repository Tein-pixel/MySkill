---
name: general-automation-design
description: Design reliable automations with explicit triggers, idempotency, retries, permissions, and failure recovery.
---

# General Automation Design

Define trigger, inputs, outputs, and side effects. Validate inputs and authorization. Make operations idempotent where possible. Use bounded retries, timeouts, and audit logs without secrets. Add dry-run and confirmation for destructive or externally visible actions. Test duplicates and partial failures.

## Completion checks
- Confirm the task matches this skill's scope.
- Inspect relevant source, project, and user constraints.
- State assumptions and unknowns instead of inventing facts.
- Prefer small, reversible steps and preserve existing work.
- Verify with evidence appropriate to the task.
- Report what was verified, what was not run, and remaining risks.
