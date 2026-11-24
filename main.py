#!/usr/bin/env python3
"""Entry program for 'Last Text at One Percent'.

The whole submission is the last text a dying phone sends at one
percent battery: a farewell to its charger, a noble death by
buffering, a claim of being at 100 percent in spirit — and then the
message itself dies mid-sentence, cut off before it can finish saying
goodbye to the charger a second time.

The program writes that line to entry.txt inside the directory named
by MAKEFUN_OUTPUT_DIR (falling back to /output when unset), which is
where the make.fun harness looks for the artifact it scores.
"""

import os
from pathlib import Path

TEXT = (
    "Tell my charger I loved her. Tell the group chat I died doing what "
    "I loved: buffering a video nobody asked me to load. If anyone "
    "asks, I was at 100 percent in spirit. Goodbye. Tell my charger I—"
)

OUTPUT_NAME = "entry.txt"
CHAR_LIMIT = 200

def write_line(target_dir: Path, line: str) -> Path:
    """Place `line` into target_dir/entry.txt and return the file path.

    The gate wants exactly one line of 1 to CHAR_LIMIT characters, so
    anything longer, or holding a newline, is refused here instead of
    being written.
    """
    if "\n" in line or line != line.strip() or not 1 <= len(line) <= CHAR_LIMIT:
        raise ValueError("text must be one trimmed line of 1-200 characters")
    target_dir.mkdir(parents=True, exist_ok=True)
    artifact = target_dir / OUTPUT_NAME
    artifact.write_text(line, encoding="utf-8")
    return artifact


def run() -> None:
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    written = write_line(destination, TEXT)
    print(f"wrote {written}: {TEXT}")


if __name__ == "__main__":
    run()
