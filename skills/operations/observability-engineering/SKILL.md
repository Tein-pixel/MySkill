---
name: observability-engineering
description: Design logs, metrics, traces, dashboards, and alerts that make software behavior diagnosable without exposing sensitive data.
---

# Observability Engineering

## Workflow

Identify service boundaries, critical user journeys, failure modes, and operational objectives. Choose structured logs, RED/USE metrics, distributed traces, and correlation IDs appropriate to the architecture. Define stable names, units, labels, cardinality limits, retention, sampling, and ownership. Avoid secrets, personal data, tokens, and raw payloads in telemetry. Build alerts around user impact and actionable thresholds, not noisy raw counts. Verify telemetry end-to-end and document gaps. Separate instrumentation from incident response and avoid claiming observability coverage based only on dashboards existing.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
