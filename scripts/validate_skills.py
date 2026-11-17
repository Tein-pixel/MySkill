#!/usr/bin/env python3
"""Dependency-free metadata and local-link checks for MySkill."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
paths = sorted(SKILLS.glob("**/SKILL.md"))
errors = []
seen = {}

for path in paths:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        errors.append(f"{path}: missing YAML frontmatter")
        continue
    try:
        end = lines.index("---", 1)
    except ValueError:
        errors.append(f"{path}: unterminated frontmatter")
        continue

    front = "\n".join(lines[1:end])
    body = "\n".join(lines[end + 1:]).strip()
    name_match = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", front)
    description_match = re.search(r"(?m)^description:\s*(.+)$", front)

    if not name_match:
        errors.append(f"{path}: missing or invalid name")
        continue

    name = name_match.group(1)
    if not description_match:
        errors.append(f"{path}: missing description")
    elif len(description_match.group(1)) > 1024:
        errors.append(f"{path}: description exceeds 1024 characters")

    if name != path.parent.name:
        errors.append(f"{path}: skill name does not match folder")
    if len(name) > 64:
        errors.append(f"{path}: name exceeds 64 characters")
    if name in seen:
        errors.append(f"{path}: duplicate skill name also found at {seen[name]}")
    seen[name] = path

    if not body:
        errors.append(f"{path}: empty skill body")

    for target in re.findall(r"\]\(([^)]+)\)", body):
        target = target.strip().split("#", 1)[0]
        if not target or "://" in target or target.startswith("mailto:"):
            continue
        resolved = ROOT / target.lstrip("/") if target.startswith("/") else path.parent / target
        if not resolved.exists():
            errors.append(f"{path}: broken local link -> {target}")

print(f"Checked {len(paths)} SKILL.md files.")
if errors:
    print("\n".join(errors))
    sys.exit(1)

print("PASS: metadata, naming, duplicate, body, and local-link checks.")
print("Note: this is not the official Agent Skills validator or a behavioral benchmark.")
