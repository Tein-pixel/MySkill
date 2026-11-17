---
name: android-r8-optimization
description: Analyze Android R8 and ProGuard configuration, keep rules, shrinking, obfuscation, and release-size tradeoffs.
---

# Android R8 Optimization

## Workflow

Inspect actual AGP/R8 versions, release variants, minification settings, consumer rules, reflection, JNI, serialization, and generated keep rules. Confirm which analyzer features are available for that exact toolchain. Identify redundant or overly broad rules without deleting rules required by runtime reflection. Prefer generated reports and artifacts over guesses. Make one rule change at a time, run the release minification task, and smoke-test reflective, navigation, DI, serialization, and native paths. Report measured size impact only when before/after artifacts exist.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve unrelated behavior and existing project conventions.
- Verify important changes with an appropriate observable check.
- Report evidence, caveats, and unverified areas separately.
