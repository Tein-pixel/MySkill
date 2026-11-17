---
name: android-tv-compose-migration
description: Migrate Android TV experiences from legacy Leanback Views to Compose for TV while preserving remote navigation and playback workflows.
---

# Android Tv Compose Migration

## Workflow

Inventory Leanback fragments, presenters, rows, focus restoration, media playback, deep links, and accessibility. Check the current Compose for TV APIs and migration guidance. Migrate a vertical slice at a time, preserving D-pad navigation, focus order, selected state, overscan-safe layout, and remote back behavior. Ensure cards and rows are readable at television viewing distance and avoid touch-only controls. Keep playback and state restoration stable when returning from detail screens. Test with TV emulators and real remote input; do not assume phone UI patterns work on TV.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
