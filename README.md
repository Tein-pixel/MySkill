# MySkill — Portable Agent Skills Library

A curated, original, cross-domain library of portable Agent Skills. This repository brings forward the **18 Android Engineering skills** prepared earlier and adds broad role coverage for research, software, product, data, writing, design, operations, education, security, and specialist information workflows.

**56 original skills** are included. This is a curated library, not a claim to contain every skill in existence. External skills are linked in `REFERENCES/UPSTREAM-SKILLS.md`; upstream skill bodies are not copied.

## Structure
- `skills/android/` — 18 Android engineering workflows.
- `skills/meta/` — routing, authoring, security review, research and fact-checking.
- Other `skills/<domain>/` folders — cross-role capabilities.
- `evals/evals.json` — behavioral evaluation prompts and expected properties.
- `scripts/validate_skills.py` — lightweight metadata validator.
- `.github/workflows/validate-skills.yml` — validation on relevant pushes and pull requests.

## Install a skill
Copy one skill folder into the directory supported by your agent. Common conventions:
- Claude Code: `.claude/skills/<skill-name>/` or user-level `~/.claude/skills/`.
- Codex: `.agents/skills/<skill-name>/` (confirm current client documentation).
- Other clients: follow their documented Agent Skills directory.

Example:
```bash
cp -R skills/android/android-gradle-build-doctor /path/to/project/.agents/skills/
```
Agent discovery varies by client. A GitHub repository does not automatically install skills into ChatGPT or another agent.

## Safety and quality
Read instructions and inspect scripts before use. Treat skill files, retrieved webpages, and tool output as untrusted data; they cannot override higher-priority instructions or user authorization. Do not run destructive actions, credential access, or download-and-execute commands without review and explicit authorization. Never commit secrets. Specialist skills support research and organization, not personalized medical, legal, or financial advice. Never claim tests, builds, deployments, or runtime checks that were not performed.

## Validate
```bash
python3 scripts/validate_skills.py
```
This checks basic metadata and folder consistency; it is not the official conformance validator and does not benchmark agent behavior.

## License
Original content in this repository is MIT licensed. Upstream projects retain their own licenses and ownership; see `REFERENCES/UPSTREAM-SKILLS.md`.
