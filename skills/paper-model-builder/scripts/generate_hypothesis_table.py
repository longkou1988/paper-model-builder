#!/usr/bin/env python3
"""Generate Markdown and optional XLSX hypothesis tables from model_spec.json."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def rows_from_model(model: dict) -> list[dict]:
    rows = []
    for index, path in enumerate(model.get("paths", []), start=1):
        rows.append({
            "Hypothesis_ID": path.get("id", f"H{index}"),
            "Path_Type": path.get("type", "未指定"),
            "Source": path.get("source", "未指定"),
            "Target": path.get("target", "未指定"),
            "Expected_Direction": path.get("direction", "未指定"),
            "Chinese_Text": path.get("hypothesis_cn", "待补充"),
            "English_Text": path.get("hypothesis_en", "To be completed"),
            "Theory_Rationale": path.get("rationale", "待补充"),
            "Evidence_Source": path.get("evidence", "未确认"),
            "Confidence": path.get("confidence", "低置信度"),
            "Reviewer_Risk": path.get("reviewer_risk", "待评估"),
        })
    return rows


def write_markdown(rows: list[dict], output: Path) -> None:
    headers = list(rows[0].keys()) if rows else ["Hypothesis_ID", "Path_Type", "Source", "Target", "Confidence"]
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(header, "")).replace("|", "/") for header in headers) + " |")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_xlsx(rows: list[dict], output: Path) -> None:
    try:
        from openpyxl import Workbook
    except ImportError:
        return
    headers = list(rows[0].keys()) if rows else ["Hypothesis_ID", "Path_Type", "Source", "Target", "Confidence"]
    wb = Workbook()
    ws = wb.active
    ws.title = "hypotheses"
    ws.append(headers)
    for row in rows:
        ws.append([row.get(header, "") for header in headers])
    output.parent.mkdir(parents=True, exist_ok=True)
    wb.save(output)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--output-md", required=True)
    parser.add_argument("--output-xlsx", required=False)
    args = parser.parse_args()

    model = json.loads(Path(args.model).read_text(encoding="utf-8"))
    rows = rows_from_model(model)
    write_markdown(rows, Path(args.output_md))
    if args.output_xlsx:
        write_xlsx(rows, Path(args.output_xlsx))


if __name__ == "__main__":
    main()
