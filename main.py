#!/usr/bin/env python3
"""Deliver the 19 November 2026 news picture to the judging harness.

Everything the judge ever sees is the single file entry.png sitting in
this folder: a six-panel summary of the day the Shenzhen three-way
summit, the GTA VI launch, the Iran warning, the Myanmar genocide
ruling, the Crimea Bridge strike and the Arctic pact all shared. The
harness starts this program two times in a sealed sandbox and reads
whatever lands in the output folder, so the program's one task is to
place an exact copy of the picture there and prove the copy is whole.
"""

import hashlib
import os
import shutil
import sys

PICTURE_NAME = "entry.png"
MAX_BYTES = 1024 * 1024  # the gate refuses anything past one mebibyte


def picture_path() -> str:
    folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(folder, PICTURE_NAME)


def digest(path: str) -> str:
    hasher = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def looks_like_png(path: str) -> bool:
    with open(path, "rb") as handle:
        return handle.read(len(PNG_SIGNATURE)) == PNG_SIGNATURE


def deliver() -> int:
    source = picture_path()
    if os.path.getsize(source) > MAX_BYTES:
        print("entry.png exceeds the size gate", file=sys.stderr)
        return 1
    if not looks_like_png(source):
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    out_folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_folder, exist_ok=True)
    target = os.path.join(out_folder, PICTURE_NAME)
    shutil.copyfile(source, target)
    if digest(target) != digest(source):
        print("delivered copy failed its checksum", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(deliver())
