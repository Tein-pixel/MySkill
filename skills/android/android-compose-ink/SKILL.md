---
name: android-compose-ink
description: Build stylus and touch drawing experiences in Jetpack Compose using supported Jetpack Ink APIs, stroke lifecycle, editing, and persistence.
---

# Android Compose Ink

## Workflow

Confirm Jetpack Ink version, device stylus capabilities, pointer input requirements, and supported APIs. Separate stroke capture, rendering, tool configuration, editing, and persistence. Handle pressure, tilt, rotation, palm rejection where supported, coordinate transforms, viewport changes, erasing, and wet-to-dry handoff. Keep rendering responsive and avoid blocking the UI thread on storage or processing. Persist strokes in a versioned representation rather than only as a flattened bitmap when editability matters. Test stylus and touch input, rotation, undo/redo, export, and large documents on supported hardware.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
