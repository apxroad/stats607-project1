#!/usr/bin/env python3
"""
Run the complete analysis with sensible defaults.
"""
from __future__ import annotations
import sys

DEFAULT_ARGS = [
    "--data", "data/credit-card-holder-data.csv",
    "--k-min", "2",
    "--k-max", "10",
    "--k", "6",
    "--random-state", "42",
    "--out", "artifacts",
]

def main() -> None:
    # If user passes no flags, use defaults; otherwise pass through.
    if len(sys.argv) == 1:
        argv = [sys.argv[0]] + DEFAULT_ARGS
    else:
        argv = sys.argv
    # Defer import so argparse in the pipeline sees our argv
    from segmentation.run_pipeline import main as pipeline_main
    sys.argv = argv
    pipeline_main()

if __name__ == "__main__":
    main()
