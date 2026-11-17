---
name: codebase-cartography
description: Map an unfamiliar codebase into navigable modules, dependency flows, entry points, and high-risk change areas before engineering work.
---

# Codebase Cartography

## Workflow

Start with repository instructions, build manifests, package/module layout, entry points, tests, and CI. Trace important behavior across UI, domain, services, storage, and external systems. Build a concise module map with responsibilities, dependencies, data flow, and test seams. Use import/call graphs when available, but verify graph findings against source. Distinguish confirmed structure from inferred architecture. Save a durable map only when useful.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve unrelated behavior and existing project conventions.
- Verify important changes with an appropriate observable check.
- Report evidence, caveats, and unverified areas separately.
