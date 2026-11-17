---
name: skill-authoring
description: Design, write, test, and maintain portable Agent Skills using the open SKILL.md convention.
---

# Skill Authoring

Create one capability per skill. Write trigger-oriented metadata and concise procedural steps. Include prerequisites, decisions, failures, and verification. Move bulky references into references/. Do not include secrets, unsafe commands, or policy override claims. Test positive, negative, ambiguous, and adversarial prompts. Track provenance and license.

## Completion checks
- Confirm the task matches this skill's scope.
- Inspect relevant source, project, and user constraints.
- State assumptions and unknowns instead of inventing facts.
- Prefer small, reversible steps and preserve existing work.
- Verify with evidence appropriate to the task.
- Report what was verified, what was not run, and remaining risks.
