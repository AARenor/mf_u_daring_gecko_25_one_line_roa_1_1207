#!/usr/bin/env python3
"""Write one short roast line for make.fun's gadget bounty."""

import os
import pathlib
import sys

TEXT = "My watch congratulated me on a twelve-hour stand goal I hit standing at the fridge."


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, "entry text must be between 1 and 280 characters"

    target = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    out_dir = pathlib.Path(target)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(text.encode("utf-8"))

    print(len(text), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
