# Contributing to MySkill

## Before adding a skill
1. Search CATALOG.md for overlap.
2. Define one specific job and trigger description.
3. Inspect primary documentation and upstream sources.
4. Check source license and avoid copying third-party skill bodies.
5. Add positive and negative evaluation prompts.

## Authoring
- Use skills/<domain>/<skill-name>/SKILL.md.
- Match the frontmatter name to the directory name.
- Make description specific about when the skill should trigger.
- Include operational steps, prerequisites, decisions, failure handling, and verification.
- Move large references to a sibling references/ folder.
- Never put secrets, private user data, or unsafe instructions into skills.

## Validation
Run python3 scripts/validate_skills.py and inspect GitHub Actions. This checks metadata and links, not whether an agent follows the instructions. Behavioral evaluation must run on a compatible agent runtime and be reported separately.

## Review criteria
Specificity, operational value, evidence, testability, portability, safety, license clarity, and maintenance.
