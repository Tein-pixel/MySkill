---
name: android-camera-workflow
description: Build or debug Android camera features with CameraX lifecycle, preview, capture, analysis, recording, and hardware variation.
---

# Android Camera Workflow

## Workflow

Inspect current Camera1/Camera2/CameraX usage, lifecycle owner, use-case binding, selector, permissions, executor ownership, and output destinations. Prefer CameraX unless a documented hardware feature needs lower-level interop. Handle asynchronous start/stop events, immutable builder return values, rotation, mirroring, device capabilities, and lifecycle unbinding. Keep image analysis off the main thread and close frames promptly. Test front/rear cameras, missing features, permission denial, rotation, interruptions, and low-resource devices.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve unrelated behavior and existing project conventions.
- Verify important changes with an appropriate observable check.
- Report evidence, caveats, and unverified areas separately.
