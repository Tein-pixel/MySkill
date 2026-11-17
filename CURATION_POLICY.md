# Curation policy

## Goal
Build a useful, safe, maintainable set of original skills for real tasks across domains—not maximize raw file count.

## Admission checks
A candidate skill should have one distinct user problem and trigger, a repeatable workflow beyond generic model knowledge, a verifiable output or decision process, explicit prerequisites and limits, and a clear source/license trail for adapted material.

## Research inputs
SkillLeaderboard is a discovery index. Its public methodology says the default ranking follows GitHub stars, momentum uses recent star movement, and Traction Score is a separate signal for attention, adoption, and maintenance. The site says it discovers repositories daily, checks them against skill criteria, publishes daily snapshots, and reviews corrections. These metrics are not quality certification or a security audit.

The public catalog API is read-only: GET /api/v1/repositories and GET /api/v1/skills. The endpoints support substring search and pagination. The skills endpoint returns repository, skill name, path, and source URL; it does not return skill descriptions or file contents. Always inspect the source repository and actual skill file.

## Review rubric
Score candidates separately on task specificity, operational detail, source quality/freshness, testability, portability, safety, license clarity, and maintenance. Stars and trending are discovery signals only.

## Adaptation and attribution
- Do not copy full upstream skill bodies.
- Summarize ideas in original wording and add domain-specific guardrails.
- Link sources and note meaningful influence in REFERENCES/UPSTREAM-SKILLS.md.
- Check upstream licenses before copying code, scripts, datasets, or substantial text.
- Preserve attribution and notices when redistribution is permitted.

## Maintenance
Review upstream APIs and version-sensitive advice periodically. Mark stale material and replace brittle version advice with a documented compatibility check.
