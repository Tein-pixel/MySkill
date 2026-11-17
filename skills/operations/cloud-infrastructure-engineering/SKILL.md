---
name: cloud-infrastructure-engineering
description: Design and review cloud infrastructure with secure identity, networking, resilience, cost controls, and reproducible deployment.
---

# Cloud Infrastructure Engineering

## Workflow

Clarify provider, workloads, data sensitivity, geography, availability, and budget constraints. Inspect existing infrastructure-as-code and platform conventions before changes. Design least-privilege identities, network boundaries, encryption, backup, observability, scaling, and recovery. Prefer declarative infrastructure and reviewed plans over ad hoc console changes. Estimate cost using current provider pricing and explicit assumptions. Protect secrets and production data. Require approval for destructive changes, public exposure, or spending. Verify deployed state and rollback path.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
