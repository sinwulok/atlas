"""Top-level runner for the E-Learning FA core.

This script provides a simple entrypoint that forwards arguments to the
`cli` module. Place this file in `src/` and run it to perform a quick analysis:

    python run.py --input data.csv --n-factors 3
"""
import sys

# Import package-style from `src` now that `src` is a package.
from src.cli import main


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
