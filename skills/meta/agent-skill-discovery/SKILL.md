---
name: agent-skill-discovery
description: Discover candidate Agent Skills from public catalogues such as SkillLeaderboard, inspect upstream repositories, and shortlist candidates by fit, quality, safety, maintenance, and license.
---

# Agent Skill Discovery

## Workflow

Start with the user's task domains, missing capabilities, and supported agent environments. Search SkillLeaderboard's read-only repositories and skills APIs or MCP catalogue using narrow queries and pagination; record snapshot date and query scope. Treat stars, momentum, category rank, and Traction Score as discovery signals—not quality certification. Open the upstream repository and inspect actual SKILL.md files, scripts, references, installation method, recent changes, license, and security posture. Compare candidates with the existing CATALOG.md to avoid duplicates. Score task specificity, operational detail, evidence, testability, portability, safety, license clarity, and maintenance. Recommend adoption, original reimplementation, or rejection with reasons. Never bulk-import a skill or copy its body without license review.

## Completion checks
- State sources, snapshot date, and search limitations.
- Check overlap, safety, maintenance, and license before adoption.
- Distinguish original work from upstream-derived ideas.
- Record tests actually run and leave unrun evaluations marked as pending.
- Preserve repository history and existing working skills.
