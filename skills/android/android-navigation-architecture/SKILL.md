---
name: android-navigation-architecture
description: Design or migrate Android app navigation including typed routes, back stacks, deep links, state restoration, and adaptive scenes.
---

# Android Navigation Architecture

## Workflow

Inspect current navigation library, route representation, entry ownership, deep links, saved state, multiple top-level destinations, and authentication boundaries. Follow the existing navigation stack unless migration is requested or justified. Design typed route contracts and safe argument parsing; preserve back-stack behavior and process recreation. For Navigation 3, verify version-specific APIs before adopting scenes or entry decorators. Test deep links, back behavior, multiple back stacks, restored state, and invalid arguments.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve unrelated behavior and existing project conventions.
- Verify important changes with an appropriate observable check.
- Report evidence, caveats, and unverified areas separately.
