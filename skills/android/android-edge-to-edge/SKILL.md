---
name: android-edge-to-edge
description: Implement or audit Android edge-to-edge layouts, system-bar insets, keyboard handling, and safe interactive regions.
---

# Android Edge To Edge

## Workflow

Inspect Activity setup, theme, target SDK, Scaffold hierarchy, app bars, navigation areas, dialogs, lists, FABs, and text inputs. Choose one inset owner for each content region; avoid double-applying parent padding, Scaffold PaddingValues, and component-managed insets. Ensure controls remain tappable behind system bars and the IME. Check adjustResize and current platform guidance for supported API levels. Handle gesture navigation, three-button navigation, cutouts, landscape, and large text. Capture and visually inspect representative screens.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve unrelated behavior and existing project conventions.
- Verify important changes with an appropriate observable check.
- Report evidence, caveats, and unverified areas separately.
