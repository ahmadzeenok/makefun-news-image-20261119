# 19 November 2026 — World News in One Image

Entry for the make.fun competition `news-image-20261119`: sum up the
world's news of Thursday 19 November 2026 in one image.

## The image

`entry.png` is a newspaper front page for 19 November 2026:

- **Lead story — Shenzhen summit:** Presidents Trump, Xi Jinping and
  Vladimir Putin meet in Shenzhen for rare trilateral talks.
- **Crimea:** the Crimean Bridge is struck; smoke rises after an
  explosion.
- **Strait of Hormuz:** warships and an oil tanker converge amid
  heightened Gulf tensions.
- **Tech & markets:** Anthropic debuts with a record $81 billion IPO;
  AI shares surge.
- **International justice:** the ICJ delivers its verdict in the
  Myanmar Rohingya genocide case.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the
bundled `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default
`/output`).

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
