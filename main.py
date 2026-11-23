"""One-Line Laugh Sprint: write one original funny line to /output/entry.txt.

The line is a light, funny take on everyday life, 93 characters long,
well inside the competition's 200-character limit.
"""

from pathlib import Path

LINE = "My fridge light judges me at 2 a.m., so now I eat in the dark like a raccoon with a mortgage."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
