---
name: repository-quality-audit
description: Audit repository health, maintainability, dependency risk, test coverage, release hygiene, and technical debt with evidence-ranked findings.
---

# Repository Quality Audit

## Workflow

Inspect contribution guidance, dependency manifests, lockfiles, build/test/lint workflows, source structure, documentation, and release configuration. Check duplicate logic, oversized modules, unsafe defaults, missing tests, stale dependencies, broken links, generated files, and secret exposure. Run existing checks where available. Separate confirmed defects from opportunities and speculation. Rank by impact, likelihood, cost, and blast radius. Do not refactor during the audit.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve unrelated behavior and existing project conventions.
- Verify important changes with an appropriate observable check.
- Report evidence, caveats, and unverified areas separately.
