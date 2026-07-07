#!/usr/bin/env python3
"""Generate a simple model logic checklist from model_spec.json."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

CHECKS = [
    "研究问题是否清晰",
    "理论基础是否明确",
    "自变量是否有前因逻辑",
    "因变量是否回应管理学结果",
    "中介变量是否解释机制",
    "调节变量是否代表边界条件",
    "控制变量是否有方法理由",
    "模型是否过度复杂",
    "数据来源是否可获得",
    "是否存在共同方法偏差风险",
    "是否存在内生性风险",
    "是否存在构念重叠风险",
    "是否存在变量拼盘问题",
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    model = json.loads(Path(args.model).read_text(encoding="utf-8"))
    lines = ["# Model Logic Check", "", f"Selected topic: {model.get('selected_topic', '未指定')}", ""]
    lines.append("## Checklist")
    for item in CHECKS:
        lines.append(f"- [ ] {item}：待 Codex 基于来源证据判断")
    lines.append("")
    lines.append("## Low-Confidence Items")
    lines.append("- 请列出证据不足、路径逻辑较弱或审稿风险较高的变量和假设。")
    lines.append("")
    lines.append("## Revision Suggestions")
    lines.append("- 请给出压缩模型、替换变量、调整方法或补充数据的建议。")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
