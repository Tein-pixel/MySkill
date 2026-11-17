#!/usr/bin/env python3
from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
paths=sorted((root/"skills").glob("**/SKILL.md"))
errors=[]; seen=set()
for p in paths:
    text=p.read_text(encoding="utf-8")
    if not text.startswith("---\n") or text.count("---")<2:
        errors.append(f"{p}: missing/malformed frontmatter"); continue
    fm=text.split("---",2)[1]
    n=re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$",fm)
    d=re.search(r"(?m)^description:\s*(.+)$",fm)
    if not n: errors.append(f"{p}: invalid name"); continue
    if not d: errors.append(f"{p}: missing description")
    if n.group(1)!=p.parent.name: errors.append(f"{p}: folder/name mismatch")
    if len(n.group(1))>64: errors.append(f"{p}: name too long")
    if d and len(d.group(1))>1024: errors.append(f"{p}: description too long")
    if n.group(1) in seen: errors.append(f"{p}: duplicate name")
    seen.add(n.group(1))
    if not text.split("---",2)[2].strip(): errors.append(f"{p}: empty body")
print(f"Checked {len(paths)} SKILL.md files.")
if errors: print("\n".join(errors)); sys.exit(1)
print("PASS: basic metadata checks (not a full conformance or behavior benchmark).")
