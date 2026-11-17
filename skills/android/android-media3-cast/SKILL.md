---
name: android-media3-cast
description: Integrate Google Cast with Android Media3 while preserving local playback, session lifecycle, queue state, and user control.
---

# Android Media3 Cast

## Workflow

Inspect the current Media3 player, session, playback queue, media metadata, and lifecycle ownership. Check current Cast and Media3 dependency compatibility and official integration guides. Model local-to-remote handoff and remote-to-local recovery explicitly, including buffering, disconnect, route changes, and session end. Keep playback state synchronized without creating duplicate players or leaking callbacks. Respect user choice and supported Cast targets. Test connection, playback, pause/seek, queue updates, disconnection, and app background/foreground transitions using authorized Cast devices or test receivers.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
