---
name: android-views-to-compose-migration
description: Migrate selected Android XML layouts or View-based screens to Jetpack Compose while preserving behavior and interoperability.
---

# Android Views To Compose Migration

## Workflow

Map the existing screen, fragment/activity lifecycle, navigation, state, accessibility, themes, resources, and UI tests. Choose a screen-by-screen migration rather than rewriting the entire app. Define observable parity criteria for layout, interactions, validation, loading/error states, and restoration. Use ComposeView or AndroidView interop only where needed, and follow the existing navigation architecture. Preserve deep links, back behavior, and saved state. Add screenshot or UI tests before replacing the original path. Keep rollback possible until parity is verified. Do not upgrade unrelated dependencies or change product design during a migration unless requested.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
