# SkillLeaderboard research notes

Research snapshot: **17 November 2026**. The homepage reported catalog data through **16 November 2026**. Rankings and counts are time-sensitive.

## Homepage snapshot
The site reported 39.1k skills tracked, 749k stars gained in the preceding 30 days, 11.9k commits in the preceding 30 days, and 8.6M SKILL.md lines analyzed.

Visible categories were Agent Orchestration, Backend, Blockchain, Browser Automation, Business, Code Quality, Data, Databases, Design, Developer Tooling, DevOps, Diagramming, Docs, Finance, Gaming, Knowledge, Learning, Legal, Lifestyle, Marketing, Media, Mobile, Presentations, Prompting, Research, Sales, Science, Security, Skill Creation, Skill Management, Software Engineering, Testing, Token Optimization, and Writing.

## Ranking methodology
- **Popularity:** default order follows GitHub stars.
- **Momentum:** recent star change indicates current attention.
- **Traction Score:** a separate signal intended to represent broader attention, adoption, and active maintenance.

The site says it searches GitHub daily, checks repositories against skill criteria, publishes refreshed snapshots, and reviews community corrections. Included repositories ship actual SKILL.md files, skill collections, skills with supporting resources, or plugins whose primary purpose is delivering skills. Excluded entries include directories that only link to skills, runtime-internal maintenance skills, prompt collections without packaged workflows, standalone installers, and tutorials without usable skill packages.

Do not infer the exact Traction Score formula; the public methodology does not disclose complete weights or calculations.

## Useful entries in the 16 November snapshot
- mattpocock/skills — engineering and code review.
- obra/superpowers — software-development workflow.
- multica-ai/andrej-karpathy-skills — requirement clarity, simplicity, and focused changes.
- anthropics/skills — document, design, and business workflows.
- DietrichGebert/ponytail — repository quality and technical debt.
- nextlevelbuilder/ui-ux-pro-max-skill — UI/UX design intelligence.
- Graphify-Labs/graphify — navigable codebase knowledge graphs.
- addyosmani/agent-skills — specification-to-release engineering lifecycle.
- pbakaus/impeccable — UX audit and frontend refinement.
- cloudflare/security-audit-skill — defensive security review.
- mvanhorn/last30days-skill — recent-trend research.
- coreyhaines31/marketingskills — conversion and marketing workflows.
- K-Dense-AI/scientific-agent-skills — scientific research and analysis.
- emilkowalski/skills — interface animation and motion design.
- OthmanAdi/planning-with-files — durable plans and progress notes.
- google/skills — workflows for Google technologies.

These are discovery references, not endorsements or proof that every skill is suitable. Inspect source files, maintenance, prerequisites, license, and security before adoption.

## Android source audit
The official android/skills README says its focus is use cases and workflows where evaluations show agents underperform, rather than repeating familiar Android basics. Direct inspection of its main branch on 17 November 2026 found 37 SKILL.md files. Specialized topics include ANR analysis, R8 configuration, Intent security, permission security, edge-to-edge, Android Profiler, Compose performance, adaptive UI, Navigation 3, CameraX, Android CLI, testing setup, and AppFunctions.

MySkill contains original skills addressing these problem areas; it does not mirror or redistribute Google's skill files. The upstream Android skills repository states Apache-2.0 licensing. Any future redistribution of upstream source code or substantial text must follow that license and preserve required notices.

## Public API notes
The developer documentation describes read-only JSON endpoints at https://www.skillleaderboard.com/api/v1/repositories and https://www.skillleaderboard.com/api/v1/skills. Both accept optional case-insensitive substring q, limit 1–100, and offset 0–10000. Results include snapshotDate, total, limit, offset, and data. The skills endpoint returns names, paths, repository identities, and upstream URLs; it does not include skill descriptions or file contents.

## Sources
- https://www.skillleaderboard.com/
- https://www.skillleaderboard.com/methodology
- https://www.skillleaderboard.com/developers
- https://www.skillleaderboard.com/openapi.json
- https://github.com/android/skills
- https://github.com/mattpocock/skills
- https://github.com/obra/superpowers
- https://github.com/multica-ai/andrej-karpathy-skills
- https://github.com/DietrichGebert/ponytail
- https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- https://github.com/Graphify-Labs/graphify
- https://github.com/addyosmani/agent-skills
- https://github.com/pbakaus/impeccable
- https://github.com/cloudflare/security-audit-skill
- https://github.com/mvanhorn/last30days-skill
- https://github.com/coreyhaines31/marketingskills
- https://github.com/K-Dense-AI/scientific-agent-skills
- https://github.com/emilkowalski/skills
- https://github.com/OthmanAdi/planning-with-files
- https://github.com/obsidianmd/obsidian-skills
