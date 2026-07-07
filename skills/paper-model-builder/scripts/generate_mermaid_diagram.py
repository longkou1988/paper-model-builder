#!/usr/bin/env python3
"""Generate a Mermaid model diagram from model_spec.json."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def node_id(name: str) -> str:
    return "N" + str(abs(hash(name)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    model = json.loads(Path(args.model).read_text(encoding="utf-8"))
    variables = model.get("variables", [])
    paths = model.get("paths", [])

    labels = {item.get("name", "未命名变量"): node_id(item.get("name", "未命名变量")) for item in variables}
    lines = ["flowchart LR"]
    for name, nid in labels.items():
        role = next((item.get("role", "") for item in variables if item.get("name") == name), "")
        lines.append(f'  {nid}["{name}<br/>{role}"]')
    for path in paths:
        source = path.get("source", "")
        target = path.get("target", "")
        if not source or not target:
            continue
        sid = labels.setdefault(source, node_id(source))
        tid = labels.setdefault(target, node_id(target))
        arrow = "-.->" if path.get("type") in {"moderation", "control"} else "-->"
        label = path.get("id", "")
        lines.append(f"  {sid} {arrow}|{label}| {tid}")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
