"""python3 -m tools.frequency_absorption [--out DIR]"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .generate import DEFAULT_OUT_DIR, generate


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Generate the frequency-versus-absorption table and plot from "
            "opened Gabriel 1996 parameters and opened product-band records. "
            "Not medical advice; not a regulatory determination."
        )
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=DEFAULT_OUT_DIR,
        help="Output directory (default: causes/radio-frequency/)",
    )
    args = parser.parse_args(argv)
    paths = generate(args.out)
    for kind, path in paths.items():
        print(f"{kind}: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
