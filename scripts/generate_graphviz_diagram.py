#!/usr/bin/env python3
"""Generate a Graphviz DOT model diagram from model_spec.json."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def esc(text: str) -> str:
    return text.replace('"', '\\"')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    model = json.loads(Path(args.model).read_text(encoding="utf-8"))
    lines = ["digraph ResearchModel {", "  rankdir=LR;", "  node [shape=box, style=rounded];"]
    for variable in model.get("variables", []):
        name = variable.get("name", "未命名变量")
        role = variable.get("role", "")
        lines.append(f'  "{esc(name)}" [label="{esc(name)}\\n{esc(role)}"];')
    for path in model.get("paths", []):
        source = path.get("source", "")
        target = path.get("target", "")
        if not source or not target:
            continue
        style = "dashed" if path.get("type") in {"moderation", "control"} else "solid"
        label = path.get("id", "")
        lines.append(f'  "{esc(source)}" -> "{esc(target)}" [label="{esc(label)}", style={style}];')
    lines.append("}")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
