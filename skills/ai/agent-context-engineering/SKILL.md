---
name: agent-context-engineering
description: Design reliable context, memory, retrieval, and handoff strategies for AI agents across long-running tasks and changing context windows.
---

# Agent Context Engineering

## Workflow

Define what must persist, what can be retrieved on demand, and what should never be stored. Keep durable facts, project decisions, task state, and ephemeral observations separate. Prefer source-linked notes and concise glossaries over giant summaries. Track provenance, timestamps, uncertainty, and staleness. Retrieve only relevant context and revalidate mutable facts. Never store credentials or sensitive personal data in agent memory files. Handoffs should include state, changed files, evidence, blockers, and next safe action.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve unrelated behavior and existing project conventions.
- Verify important changes with an appropriate observable check.
- Report evidence, caveats, and unverified areas separately.
