---
name: android-xr-development
description: Design Android XR projected or immersive experiences using supported Compose XR toolkits, spatial UI principles, and hardware capability checks.
---

# Android Xr Development

## Workflow

First determine the XR device class and supported SDK/toolkit: projected display glasses and immersive XR have different capabilities. Check current Android XR documentation, API status, hardware availability, and required permissions before implementation. Keep core app workflows usable without XR where possible. For projected experiences, design glanceable spatial overlays that respect field of view, user movement, readability, and safety. Gate camera, microphone, and sensor access behind visible user intent and least privilege. Handle unavailable hardware gracefully. Test with supported emulators or hardware; never claim device validation without it.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
