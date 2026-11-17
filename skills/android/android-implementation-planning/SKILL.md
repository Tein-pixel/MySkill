---
name: android-implementation-planning
description: Create incremental, risk-aware Android implementation plans with dependencies, test seams, and rollback considerations.
---

# Android Implementation Planning

Break accepted scope into independently testable vertical slices. Identify modules, interfaces, migrations, API changes, UI states, permissions, and toolchain risks. Order by dependency. Define a check for each slice. Preserve existing features and prefer reversible changes.

## Completion checks
- Confirm the task matches this skill's scope.
- Inspect relevant source, project, and user constraints.
- State assumptions and unknowns instead of inventing facts.
- Prefer small, reversible steps and preserve existing work.
- Verify with evidence appropriate to the task.
- Report what was verified, what was not run, and remaining risks.
