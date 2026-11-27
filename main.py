#!/usr/bin/env python3
"""THE WHOLE WORLD - Friday 27 November 2026 (make.fun news-image-20261127).

This repository holds one newspaper front page as a single 1024x1024
image: entry.png, carrying 42 wire stories that happened, or were first
reported, on Friday 27 November 2026. Each story was checked against
Reuters, AP, BBC, Al Jazeera, Radio Dabanga or PANA on the day itself;
the three big Thursday stories are named in the page's DATE CHECK strip
rather than passed off as Friday news.

Running this program republishes that page. The PNG travels with the
repository, and a run simply delivers a byte-identical copy of it to
the chosen destination, so the output never drifts between runs.

Where the copy lands, in order: the path given as the first argument;
otherwise $MAKEFUN_OUTPUT_DIR/entry.png - the harness mounts the
repository read-only and names a writable folder through that variable;
otherwise out/entry.png beside this file.
"""

import os
import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"


def destination(argv):
    if len(argv) > 1:
        return Path(argv[1])
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if folder:
        return Path(folder) / "entry.png"
    return SOURCE.parent / "out" / "entry.png"


def main(argv):
    out = destination(argv)
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out)
    print("entry.png delivered to {} ({} bytes)".format(out, out.stat().st_size))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
