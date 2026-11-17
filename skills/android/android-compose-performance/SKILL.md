---
name: android-compose-performance
description: Investigate Jetpack Compose recomposition, state reads, lazy layouts, allocations, stability, and frame-time regressions.
---

# Android Compose Performance

## Workflow

Start from measured jank or CPU symptoms; do not optimize recomposition counts in isolation. Inspect state ownership, phase of state reads, effects, remember keys, lazy item identity, expensive calculations, image work, and allocations. Check Compose compiler/runtime versions and current official guidance before recommending stability annotations or newer APIs. Avoid blanket stability annotations and speculative memoization. Use Layout Inspector, tracing, Macrobenchmark, or frame metrics where available. Compare before/after performance on the same scenario.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve unrelated behavior and existing project conventions.
- Verify important changes with an appropriate observable check.
- Report evidence, caveats, and unverified areas separately.
