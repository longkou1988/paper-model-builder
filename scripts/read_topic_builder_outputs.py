#!/usr/bin/env python3
"""Read paper-topic-builder outputs and create a compact source inventory."""

from __future__ import annotations

import json
from pathlib import Path

EXPECTED_FILES = [
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


def main() -> None:
    source_dir = Path("input/topic_builder_outputs")
    output_dir = Path("output")
    output_dir.mkdir(parents=True, exist_ok=True)

    inventory = []
    for name in EXPECTED_FILES:
        path = source_dir / name
        item = {
            "file": name,
            "available": path.exists(),
            "path": str(path),
            "size_bytes": path.stat().st_size if path.exists() else None,
        }
        inventory.append(item)

    (output_dir / "source_inventory.json").write_text(
        json.dumps(inventory, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    lines = ["# Source Inventory", ""]
    for item in inventory:
        status = "available" if item["available"] else "missing"
        lines.append(f"- {item['file']}: {status}")
    (output_dir / "source_inventory.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
