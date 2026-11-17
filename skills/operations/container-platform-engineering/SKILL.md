---
name: container-platform-engineering
description: Build and operate containerized services with reproducible images, least privilege, orchestration, resource limits, and rollout safety.
---

# Container Platform Engineering

## Workflow

Inspect runtime, base image, dependencies, build context, registry, orchestrator, and deployment policy. Use minimal trusted base images, pinned or controlled versions, non-root users, read-only filesystems where feasible, health checks, and resource requests/limits. Scan images and minimize secrets in layers and build logs. For Kubernetes, review service accounts, RBAC, probes, network policies, resource quotas, and rollout strategy. Test startup, graceful shutdown, scaling, and rollback. Do not expose cluster credentials or make production changes without explicit authorization.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
