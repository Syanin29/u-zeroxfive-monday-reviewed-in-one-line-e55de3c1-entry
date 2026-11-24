"""Monday, Reviewed in One Line — entry program.

Writes exactly one line — our funniest one-line review of our own
Monday — to entry.txt. Nothing else is written, nothing is read from
the network, no model is called, no randomness: the line is a string
literal and the run is byte-identical every time.
"""

import os
from pathlib import Path

REVIEW = "One star. My to-do list had a to-do list, and both of them quit by lunch."
# 73 characters: inside the gate's 1-200 range, one line, no trailing newline.


def output_path() -> Path:
    return Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"


def write_review(target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)
    os.chmod(target, 0o644)


def check_written(target: Path) -> None:
    # Prove the file on disk is exactly REVIEW: same text, same length,
    # still a single line with no newline anywhere in it.
    with open(target, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    assert back == REVIEW, "entry.txt differs from the final review"
    assert len(back) == len(REVIEW) == 73, "entry.txt is not 73 characters"
    assert "\n" not in back, "entry.txt must be a single line"
    assert back == back.strip(), "entry.txt must not start or end with space"


def main() -> None:
    os.umask(0o022)
    target = output_path()
    write_review(target)
    check_written(target)


if __name__ == "__main__":
    main()
