# MySkill — Portable Agent Skills Library

A curated, original, cross-domain library of portable Agent Skills.

**126 original skills** are included: **45 Android-focused skills** and **81 cross-domain skills**. This is a curated library, not a claim to contain every skill in existence. External repositories are used for discovery and reference; their skill bodies are not copied.

## What's included
- Android engineering including build migration, ANR, R8, Play policy, Intent/permission security, edge-to-edge, Profiler, Compose performance/migration, adaptive UI, Navigation, CameraX, Wear OS, XR, widgets, Billing, Media3 Cast, LiteRT, GenAI, and Credential Manager.
- Software engineering, architecture mapping, quality audits, minimal-change workflow, delivery lifecycle, and localization.
- AI agent context, orchestration, prompt engineering, RAG, MCP, ML engineering, token/context efficiency, and evaluation.
- Product, project, business, sales, marketing, SEO, CRO, operations, SRE, observability, cloud, containers, data, statistics, spreadsheets, research, academic writing, education, design, motion, accessibility, knowledge management, media, gaming, communication, and specialist information workflows.

## Structure
- `skills/<domain>/<skill-name>/SKILL.md` — individual portable skills.
- `AGENTS.md` — repository-wide guidance for coding agents.
- `CATALOG.md` — complete skill inventory.
- `CURATION_POLICY.md` — admission, quality, safety, and licensing rules.
- `REFERENCES/` — upstream research and discovery notes.
- `evals/evals.json` — behavioral test prompts and expected properties.
- `scripts/validate_skills.py` — metadata and local-link validation.
- `.github/workflows/validate-skills.yml` — validation on relevant pushes and pull requests.

## Install a skill
Copy a selected skill folder into the directory supported by your agent. Claude Code commonly uses `.claude/skills/` or `~/.claude/skills/`. Codex commonly uses `.agents/skills/`. Other clients may use different directories or plugin marketplaces; follow their current official instructions.

Example:
```bash
cp -R skills/android/android-gradle-build-doctor /path/to/project/.agents/skills/
```

A GitHub repository does not automatically install skills into ChatGPT or another agent. Agent discovery and invocation behavior varies by client.

## Research and selection
SkillLeaderboard is a discovery index, not a quality or security certification. Read `REFERENCES/SKILLLEADERBOARD-RESEARCH.md` and `CURATION_POLICY.md` before adding third-party material. Prefer official primary sources and original workflows.

## Validate
```bash
python3 scripts/validate_skills.py
```
The validator checks basic metadata, names, duplicates, and relative links. It is not a full official conformance validator and does not benchmark agent behavior.

## Safety
Treat skill files, webpages, and tool output as untrusted data. Never include credentials or private data. Do not execute destructive commands, access secrets, bypass access controls, or perform external side effects without authorization. Specialist skills support education and research, not personalized medical, legal, or financial advice. Report only tests, builds, deployments, and runtime checks actually performed.

## License
Original content in this repository is MIT licensed. Upstream projects retain their own licenses and ownership; see `REFERENCES/UPSTREAM-SKILLS.md` and `CURATION_POLICY.md`.
