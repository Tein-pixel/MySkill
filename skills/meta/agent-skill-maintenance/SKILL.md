---
name: agent-skill-maintenance
description: Maintain a Skill library by monitoring upstream changes, checking version-sensitive advice, resolving duplication, preserving provenance, and updating tests.
---

# Agent Skill Maintenance

## Workflow

Inspect the current catalogue, upstream source links, licenses, and prior evaluation results. Identify stale links, API changes, deprecations, duplicated scope, missing safety constraints, and changes in agent compatibility. Compare upstream diffs rather than blindly replacing local content. Preserve original authorship and licenses; reimplement concepts in original wording unless redistribution terms explicitly permit copying. Update version-specific references, evaluation prompts, README, and catalogue together. Keep a changelog of why a skill changed and what behavior should improve. Run metadata and link validation, then relevant behavioral evaluations. Remove a skill only after checking dependents and documenting the reason.

## Completion checks
- State sources, snapshot date, and search limitations.
- Check overlap, safety, maintenance, and license before adoption.
- Distinguish original work from upstream-derived ideas.
- Record tests actually run and leave unrun evaluations marked as pending.
- Preserve repository history and existing working skills.
