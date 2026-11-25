#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry program.

Writes a single fixed, original one-line office joke to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic: no clock, no randomness, no network, no file reads.
The output is byte-identical on every run.
"""

import os

JOKE = (
    "I told my boss I was burned out, so he put it on my performance review "
    "\u2014 I now exceed expectations quarterly."
)
# 109 characters: inside the gate's 1-200 character range, single line,
# no trailing newline so the file holds exactly the joke.


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
