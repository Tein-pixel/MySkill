---
name: llm-evaluation-engineering
description: Build repeatable evaluations for LLM and agent systems using representative datasets, rubrics, graders, safety tests, and regression analysis.
---

# Llm Evaluation Engineering

## Workflow

Define intended tasks, users, error categories, success criteria, and unacceptable failures. Create a versioned dataset covering normal, edge, ambiguous, adversarial, and out-of-scope cases. Combine deterministic checks, rubric-based review, and human judgment where needed. Calibrate graders against human examples and watch for judge bias. Track model, prompt, tool, retrieval, and dataset versions. Report confidence and failure slices, not a single score alone. Do not claim improvement without comparable runs and statistical context.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
