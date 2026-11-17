---
name: minimal-change-engineering
description: Make precise, low-risk changes in existing codebases while preserving unrelated behavior, comments, architecture, and user features.
---

# Minimal Change Engineering

## Workflow

Identify the exact requested behavior and trace the narrowest code path. State assumptions and stop when a material ambiguity changes the design. Change only lines that serve the request or are required for correctness. Match established conventions. Do not refactor unrelated code, rename unrelated symbols, reformat whole files, remove existing comments, or delete pre-existing dead code as a side effect. Clean up only artifacts made obsolete by your own change. Explain why every changed file is necessary.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve unrelated behavior and existing project conventions.
- Verify important changes with an appropriate observable check.
- Report evidence, caveats, and unverified areas separately.
