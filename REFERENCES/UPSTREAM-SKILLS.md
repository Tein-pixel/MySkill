# Upstream research and discovery sources

Research date: 2026-11-17. These repositories are references and discovery catalogs, not permission to copy their contents.

| Source | Value | Policy |
|---|---|---|
| https://agentskills.io/specification | Open folder-based Agent Skills format and progressive disclosure | Follow current specification |
| https://github.com/anthropics/skills | Official examples, skill creator, document/artifact workflows | Link upstream; respect license |
| https://github.com/obra/superpowers | Brainstorming, planning, TDD, debugging, verification, skill-writing | Adopt principles in original wording |
| https://github.com/mattpocock/skills | Requirement alignment, glossary, ADRs, composable engineering | Adopt principles in original wording |
| https://github.com/VoltAgent/awesome-agent-skills | Large curated catalog of official/community skills | Discovery only; inspect source and license |
| https://github.com/nodegenie/awesome-agent-skills | Skill discovery and security scanning concepts | Do not assume indexed skill is safe |
| https://www.theskillmd.com/ | Industry-oriented skill index with source/license metadata | Discovery only; verify upstream freshness |

## Research conclusions
1. Prefer portable folders with a focused `SKILL.md` and optional references/scripts/assets.
2. Use progressive disclosure: short trigger metadata, detailed instructions only on activation.
3. Combine requirement clarification, planning, small implementation slices, testing, debugging, and verification.
4. Prefer small composable skills over one giant prompt.
5. Treat skills as untrusted instructions because they may request actions using agent permissions.
6. Curate quality instead of bulk-copying thousands of entries.

This repository does not mirror upstream skill libraries, claim all skills are benchmarked, or guarantee automatic installation across agents.
