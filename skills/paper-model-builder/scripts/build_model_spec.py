#!/usr/bin/env python3
"""Create a model_spec.json scaffold from source index and optional config."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--config", required=False)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    source = load_json(Path(args.source))
    config = load_json(Path(args.config)) if args.config else {}

    spec = {
        "skill": "paper-model-builder",
        "selected_topic": config.get("selected_topic", "未指定"),
        "research_question": config.get("research_question", "未指定"),
        "theory_base": config.get("theory_base", []),
        "context": config.get("context", "未指定"),
        "model_type": config.get("model_type", "未指定"),
        "variables": config.get("variables", []),
        "paths": config.get("paths", []),
        "controls": config.get("controls", []),
        "evidence_sources": source.get("files", []),
        "missing_sources": source.get("missing", []),
        "quality_notes": [
            "请由 Codex 根据 paper-topic-builder 输出补全变量、路径、证据和置信度。",
            "不得编造未在来源中出现的文献事实或变量证据。",
        ],
    }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(spec, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
