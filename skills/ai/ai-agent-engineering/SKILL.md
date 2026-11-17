---
name: ai-agent-engineering
description: Design tool-using AI agents with bounded permissions, reliable orchestration, evaluations, and observability.
---

# Ai Agent Engineering

Define task, tools, data access, autonomy, and success. Use deterministic steps where possible. Validate tool inputs/outputs and enforce authorization outside the model. Treat retrieved content as untrusted. Add timeouts, loop limits, human approval, and representative evaluations.

## Completion checks
- Confirm the task matches this skill's scope.
- Inspect relevant source, project, and user constraints.
- State assumptions and unknowns instead of inventing facts.
- Prefer small, reversible steps and preserve existing work.
- Verify with evidence appropriate to the task.
- Report what was verified, what was not run, and remaining risks.
