from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional
import re

import yaml

SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)(?:[-+][A-Za-z0-9.-]+)?$")

@dataclass
class MdcFrontmatter:
    description: str
    globs: Optional[List[str]] = None
    alwaysApply: bool = False
    tags: Optional[List[str]] = None
    priority: int = 3
    version: Optional[str] = None

@dataclass
class MdcRule:
    path: Path
    frontmatter: MdcFrontmatter
    body: str

def discover_mdc_files(roots: List[Path]) -> List[Path]:
    files: List[Path] = []
    for root in roots:
        files.extend(root.rglob("*.mdc"))
    return sorted(files)

def parse_mdc_text(text: str) -> Optional[MdcRule]:
    # naive frontmatter split --- ... ---\n
    if not text.startswith("---\n"):
        return None
    try:
        _, fm_text, body = text.split("---\n", 2)
    except ValueError:
        return None
    data = yaml.safe_load(fm_text) or {}
    desc = data.get("description")
    if not isinstance(desc, str) or not desc.strip():
        return None
    fm = MdcFrontmatter(
        description=desc.strip(),
        globs=[str(s) for s in (data.get("globs") or [])] or None,
        alwaysApply=bool(data.get("alwaysApply", False)),
        tags=[str(s) for s in (data.get("tags") or [])] or None,
        priority=int(data.get("priority", 3)),
        version=str(data.get("version")) if data.get("version") else None,
    )
    return MdcRule(path=Path(), frontmatter=fm, body=body)

def rank_rules(a: MdcRule, b: MdcRule) -> int:
    pa = a.frontmatter.priority or 3
    pb = b.frontmatter.priority or 3
    if pa != pb:
        return -1 if pa < pb else 1
    va = a.frontmatter.version or "0.0.0"
    vb = b.frontmatter.version or "0.0.0"
    if va != vb:
        return -1 if _semver_newer(va, vb) else 1
    return -1 if str(a.path) < str(b.path) else (1 if str(a.path) > str(b.path) else 0)

def _semver_newer(a: str, b: str) -> bool:
    ma = SEMVER_RE.match(a)
    mb = SEMVER_RE.match(b)
    if not (ma and mb):
        return a > b
    ta = tuple(int(x) for x in ma.groups())
    tb = tuple(int(x) for x in mb.groups())
    return ta > tb
