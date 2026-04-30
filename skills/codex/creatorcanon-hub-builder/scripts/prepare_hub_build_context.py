#!/usr/bin/env python3
"""Resolve CreatorCanon hub build inputs and write a filled build prompt."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


DEFAULT_ROOT = Path(r"C:\Users\mario\Desktop\Creator Canon Hub builder")
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
AUDIT_PATTERNS = (
    "*VIDEO_AUDIT.md",
    "creator-audit.md",
    "*creator*audit*.md",
    "*video*audit*.md",
    "*audit*.md",
)


def find_audit_candidates(project: Path) -> list[Path]:
    seen: set[Path] = set()
    candidates: list[Path] = []
    for pattern in AUDIT_PATTERNS:
        for path in sorted(project.glob(pattern), key=lambda item: item.name.lower()):
            if path.is_file() and path not in seen:
                seen.add(path)
                candidates.append(path)
    return candidates


def find_project(start: Path) -> Path:
    start = start.resolve()
    if find_audit_candidates(start):
        return start

    candidates: list[Path] = []
    for child in start.iterdir():
        if child.is_dir() and find_audit_candidates(child):
            candidates.append(child)
    unique = sorted(set(candidates), key=lambda path: str(path).lower())
    if len(unique) == 1:
        return unique[0]
    if len(unique) > 1:
        joined = "\n".join(str(path) for path in unique)
        raise SystemExit(f"Multiple creator folders found. Pass --project explicitly:\n{joined}")

    raise SystemExit(f"No *VIDEO_AUDIT.md found in {start} or its immediate child folders.")


def find_audit(project: Path) -> Path:
    audits = find_audit_candidates(project)
    if audits:
        return audits[0]
    raise SystemExit(f"No creator video audit found in {project}.")


def find_mockup(project: Path, allow_missing: bool = False) -> Path | None:
    mockups_dir = project / "mockups"
    images = []
    if mockups_dir.exists():
        images.extend(path for path in mockups_dir.rglob("*") if path.suffix.lower() in IMAGE_EXTENSIONS)
    images.extend(path for path in project.glob("*") if path.suffix.lower() in IMAGE_EXTENSIONS)
    images = [path for path in images if path.is_file()]
    if images:
        return max(images, key=lambda path: path.stat().st_mtime)
    if allow_missing:
        return None
    raise SystemExit(f"No mockup image found in {mockups_dir}. Generate mockups first.")


def fill_prompt(template: str, audit: str) -> str:
    pattern = r"PASTE YOUR FULL AUDIT MARKDOWN/JSON HERE.*\Z"
    filled = re.sub(pattern, audit, template, count=1, flags=re.DOTALL)
    if filled != template:
        return filled
    raise SystemExit("Could not find audit placeholder in hub build prompt reference.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare CreatorCanon hub build context.")
    parser.add_argument("--project", default=str(DEFAULT_ROOT), help="Creator folder or root containing creator folders.")
    parser.add_argument("--allow-missing-mockup", action="store_true", help="Write context even if no mockup image exists.")
    args = parser.parse_args()

    project = find_project(Path(args.project).expanduser())
    audit_file = find_audit(project)
    mockup_file = find_mockup(project, allow_missing=args.allow_missing_mockup)
    audit = audit_file.read_text(encoding="utf-8")

    skill_dir = Path(__file__).resolve().parents[1]
    prompt_template = (skill_dir / "references" / "hub-build-prompt.md").read_text(encoding="utf-8")
    filled_prompt_file = project / "hub-build-prompt-filled.md"
    filled_prompt_file.write_text(fill_prompt(prompt_template, audit), encoding="utf-8")

    context_file = project / "hub-build-context.json"
    context = {
        "project_dir": str(project),
        "audit_file": str(audit_file),
        "mockup_file": str(mockup_file) if mockup_file else None,
        "filled_prompt_file": str(filled_prompt_file),
    }
    context_file.write_text(json.dumps(context, indent=2), encoding="utf-8")

    print(f"project_dir={project}")
    print(f"audit_file={audit_file}")
    print(f"mockup_file={mockup_file if mockup_file else ''}")
    print(f"filled_prompt_file={filled_prompt_file}")
    print(f"context_file={context_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
