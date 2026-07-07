#!/usr/bin/env python3
"""Generate a Mermaid model diagram from model_spec.json."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def node_id(index: int) -> str:
    return f"N{index}"


def clean_label(text: str) -> str:
    return re.sub(r"[\r\n]+", " ", text).replace('"', "'")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    model = json.loads(Path(args.model).read_text(encoding="utf-8"))
    variables = model.get("variables", [])
    paths = model.get("paths", [])

    labels = {}
    lines = ["flowchart LR"]
    for index, item in enumerate(variables, start=1):
        name = item.get("name", "未命名变量")
        role = item.get("role", "")
        nid = node_id(index)
        labels[name] = nid
        lines.append(f'  {nid}["{clean_label(name)}<br/>{clean_label(role)}"]')

    next_index = len(labels) + 1
    for path in paths:
        source = path.get("source", "")
        target = path.get("target", "")
        if not source or not target:
            continue
        if source not in labels:
            labels[source] = node_id(next_index)
            lines.append(f'  {labels[source]}["{clean_label(source)}"]')
            next_index += 1
        if target not in labels:
            labels[target] = node_id(next_index)
            lines.append(f'  {labels[target]}["{clean_label(target)}"]')
            next_index += 1
        arrow = "-.->" if path.get("type") in {"moderation", "control"} else "-->"
        label = clean_label(path.get("id", ""))
        lines.append(f"  {labels[source]} {arrow}|{label}| {labels[target]}")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
