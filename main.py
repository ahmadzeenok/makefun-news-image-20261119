#!/usr/bin/env python3
"""Write the 19 November 2026 world-news image to the output directory.

This program is the entry for the make.fun competition
`news-image-20261119`: "Sum up 19 November's world news in one image".

The bundled entry.png is a newspaper front page for Thursday
19 November 2026, covering the day's five biggest stories:

  1. Lead story -- Trump, Xi Jinping and Vladimir Putin meet in
     Shenzhen for rare trilateral talks.
  2. The Crimean Bridge is struck; smoke rises after an explosion.
  3. Warships and an oil tanker converge in the Strait of Hormuz
     amid heightened Gulf tensions.
  4. Anthropic debuts with a record $81 billion IPO; AI shares surge.
  5. The ICJ delivers its verdict in the Myanmar Rohingya
     genocide case.

The program copies entry.png to $MAKEFUN_OUTPUT_DIR/entry.png
(default /output). Python 3.13, standard library only, no network.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))


if __name__ == "__main__":
    main()
