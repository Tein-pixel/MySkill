---
name: site-reliability-engineering
description: Improve service reliability through SLOs, error budgets, capacity planning, resilience, and operational feedback loops.
---

# Site Reliability Engineering

## Workflow

Identify user-facing service level indicators and define measurable SLOs with a time window. Set error-budget policy and escalation thresholds with stakeholders. Analyze availability, latency, traffic, saturation, and correctness. Review capacity, dependencies, graceful degradation, retries, timeouts, bulkheads, and recovery. Prioritize engineering work by observed reliability risk rather than arbitrary uptime targets. Use post-incident learning without blame. Avoid promising a reliability percentage unsupported by measurements.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
