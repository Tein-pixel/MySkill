---
name: android-agp9-migration
description: Plan and execute Android Gradle Plugin 9 migrations with version-aware compatibility checks and reversible steps.
---

# Android Agp9 Migration

## Workflow

Inspect the project's AGP, Gradle wrapper, JDK, Kotlin/Kotlin Multiplatform status, KSP, Hilt, kapt, BuildConfig usage, custom DSL, and convention plugins. Read the exact AGP 9 migration guide for the selected version and check its compatibility matrix before changing anything. Do not assume an AGP 8 project can safely jump directly to AGP 9; identify required intermediate migrations and user-controlled Android Studio Upgrade Assistant steps. Inventory breaking changes, update dependencies deliberately, migrate DSL and compiler integrations in small slices, and preserve a rollback point. Verify sync, help, dry-run build, unit tests, and release build when feasible. Never add compatibility flags just to silence errors.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
