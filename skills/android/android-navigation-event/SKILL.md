---
name: android-navigation-event
description: Implement and audit Android predictive-back and navigation-event handling with lifecycle-safe gesture progress and cancellation.
---

# Android Navigation Event

## Workflow

Inspect the app's enabled predictive-back behavior, Activity callbacks, Compose navigation integration, and current NavigationEvent library version. Consult current Android docs and library samples before selecting APIs. Define what happens on gesture start, progress, cancellation, and commit, and ensure visual transitions remain synchronized with navigation state. Avoid duplicate back dispatch between Activity, Compose, and navigation libraries. Preserve system back, toolbar back, nested navigation, and dialog behavior. Test gesture navigation and three-button navigation across supported API levels.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
