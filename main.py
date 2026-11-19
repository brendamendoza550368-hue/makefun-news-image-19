#!/usr/bin/env python3
"""News-image entry: copy the day's picture to the output directory.

The picture itself (entry.png, kept beside this file) sums up the world
news of Thursday 19 November 2026. The judging harness runs this
program twice in a sandbox with no network and reads only
/output/entry.png, so the whole job is a byte-exact copy: same input,
same output, every run.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    # Verify the copy before reporting success: the judge reads exactly
    # these bytes, so a short or corrupt copy must fail loudly here
    # rather than score as an invalid image.
    with open(SOURCE, "rb") as fh:
        expected = fh.read()
    with open(target, "rb") as fh:
        written = fh.read()
    if written != expected:
        print("copy mismatch: output differs from entry.png", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
