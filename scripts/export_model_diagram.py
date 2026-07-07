#!/usr/bin/env python3
"""Export Graphviz DOT to SVG or PNG when Graphviz is installed."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def run_dot(dot_file: Path, output: Path, fmt: str) -> bool:
    try:
        subprocess.run(["dot", f"-T{fmt}", str(dot_file), "-o", str(output)], check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dot", required=True)
    parser.add_argument("--svg", required=False)
    parser.add_argument("--png", required=False)
    args = parser.parse_args()

    dot_file = Path(args.dot)
    if args.svg:
        run_dot(dot_file, Path(args.svg), "svg")
    if args.png:
        run_dot(dot_file, Path(args.png), "png")


if __name__ == "__main__":
    main()
