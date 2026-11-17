---
name: android-profiler-workflow
description: Use Android Studio Profiler, system traces, and repeatable measurements to investigate CPU, memory, energy, and startup behavior.
---

# Android Profiler Workflow

## Workflow

Define journey, device, API level, build type, app state, and baseline. Choose the signal matching the symptom: CPU sampling, memory allocation/heap, network, energy, startup timing, or system trace. Reproduce with identical steps and avoid comparing unlike devices or builds. Separate app code from OS scheduling, radio conditions, and background activity. Correlate expensive stacks or allocations with the exact user-visible symptom. Change one bottleneck at a time and remeasure.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve unrelated behavior and existing project conventions.
- Verify important changes with an appropriate observable check.
- Report evidence, caveats, and unverified areas separately.
