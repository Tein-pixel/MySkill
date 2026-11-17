---
name: android-intent-component-security
description: Review Android exported components, incoming Intents, PendingIntents, deep links, providers, and inter-app communication boundaries.
---

# Android Intent Component Security

## Workflow

Inspect manifest declarations and externally reachable entry points. Trace untrusted extras, nested Intents, selectors, data URIs, URI permission flags, implicit targets, and PendingIntent mutability. Prefer explicit internal Intents and immutable PendingIntents unless a documented platform flow needs mutability. Validate actions, data, and component targets before forwarding messages. Review exported receivers, services, and providers for suitable permissions and caller checks. Account for API-level differences using current Android documentation. Show the reachable path and impact; do not infer a vulnerability from a manifest flag alone.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve unrelated behavior and existing project conventions.
- Verify important changes with an appropriate observable check.
- Report evidence, caveats, and unverified areas separately.
