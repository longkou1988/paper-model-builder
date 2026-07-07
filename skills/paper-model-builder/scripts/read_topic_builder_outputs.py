#!/usr/bin/env python3
"""Build a lightweight index of paper-topic-builder output files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

EXPECTED = [
    "literature_matrix.xlsx",
    "variable_role_matrix.xlsx",
    "qualitative_mechanism_matrix.xlsx",
    "theory_gap_matrix.xlsx",
    "variable_network_summary.md",
    "topic_cards.md",
    "model_candidates.md",
    "final_research_story.md",
    "reviewer_evaluation.md",
]


def preview_text(path: Path, limit: int = 6000) -> str:
    if path.suffix.lower() not in {".md", ".txt", ".json", ".csv"}:
        return ""
    return path.read_text(encoding="utf-8", errors="replace")[:limit]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Folder containing paper-topic-builder outputs")
    parser.add_argument("--output", required=True, help="Path for source_index.json")
    args = parser.parse_args()

    input_dir = Path(args.input)
    files = []
    for name in EXPECTED:
        path = input_dir / name
        files.append({
            "name": name,
            "path": str(path),
            "exists": path.exists(),
            "type": path.suffix.lower().lstrip("."),
            "preview": preview_text(path) if path.exists() else "",
        })

    result = {
        "input_dir": str(input_dir),
        "files": files,
        "missing": [item["name"] for item in files if not item["exists"]],
    }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
