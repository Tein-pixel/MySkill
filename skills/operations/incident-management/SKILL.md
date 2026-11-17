---
name: incident-management
description: Coordinate safe incident response through triage, communication, mitigation, recovery, and blameless post-incident learning.
---

# Incident Management

## Workflow

Establish incident severity, scope, affected users, start time, and incident lead. Preserve evidence and maintain a single timeline. Prioritize reversible containment and user protection over speculative root-cause fixes. Communicate status at an agreed cadence without exposing sensitive information. Track hypotheses separately from confirmed facts. Verify recovery using service indicators, then prepare a blameless review with contributing factors, detection gaps, and owned actions. Do not run destructive production commands or make public statements without authorization.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
