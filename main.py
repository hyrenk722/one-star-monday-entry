"""One Star for Monday — make.fun entry.

Writes a single-line one-star review of Monday, written as if Monday
were a restaurant, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os

ENTRY = "Monday served my weekend cold, spilled my coffee on the to-do list, and the waiter shrugged: 'Kitchen's closed till Friday.'"

# Gate from the competition rules: UTF-8 text, 1 to 180 characters,
# a single line of at most 25 words, plain text, no explanation.
assert 1 <= len(ENTRY) <= 180, f"entry length {len(ENTRY)} outside 1..180"
assert len(ENTRY.split()) <= 25, f"entry has {len(ENTRY.split())} words, over 25"
assert "\n" not in ENTRY, "entry must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
