---
name: android-glance-widget-engineering
description: Build and maintain Android home-screen widgets with Jetpack Glance, canonical layouts, state updates, background work, and memory constraints.
---

# Android Glance Widget Engineering

## Workflow

Inspect widget providers, Glance and WorkManager versions, app data ownership, update triggers, and current RemoteViews behavior. Use supported Glance composables and canonical layout patterns appropriate to the widget's purpose and host dimensions. Keep widget state small and serializable; avoid storing large bitmaps or sensitive user data in widget state. Design explicit loading, empty, stale, and unavailable states. Respect update quotas and schedule background refreshes responsibly. Verify resize behavior, pinning, configuration, tap actions, process recreation, and memory use on supported launchers.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
