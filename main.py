#!/usr/bin/env python3
"""Five Seconds to Explain the Glass -- entry program (stdlib only).

Reads the single-sentence cat excuse from entry.txt (bundled beside this
file), writes it byte-for-byte to /output/entry.txt, and prints it to
stdout exactly as stored. Deterministic: same input, same output.

Usage:
    python3 main.py            # write /output/entry.txt and print the text
    python3 main.py --check    # validate the entry against the gate, exit 0/1
"""

import os
import sys

ENTRY_FILENAME = "entry.txt"
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200
SENTENCE_ENDERS = ".!?"


def entry_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), ENTRY_FILENAME)


def load_entry():
    with open(entry_path(), "r", encoding="utf-8") as handle:
        return handle.read()


def check_entry(text):
    """Return a list of gate violations (empty means the entry passes)."""
    problems = []
    if not text:
        problems.append("entry is empty")
    if len(text) > MAX_CHARS:
        problems.append("entry is %d characters, over the 200 limit" % len(text))
    if text.strip() == "":
        problems.append("entry is only whitespace")
    if text != text.strip():
        problems.append("entry has leading or trailing whitespace (wasted characters)")
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    enders = sum(1 for ch in text if ch in SENTENCE_ENDERS)
    if enders != 1:
        problems.append(
            "entry must be exactly one sentence (found %d sentence enders)" % enders
        )
    if enders == 1 and text[-1] not in SENTENCE_ENDERS:
        problems.append("the single sentence must end with its sentence terminator")
    return problems


def main(argv):
    if "--check" in argv:
        text = load_entry()
        problems = check_entry(text)
        if problems:
            for problem in problems:
                print("FAIL: " + problem, file=sys.stderr)
            return 1
        print("PASS: %d characters, one sentence, one line" % len(text))
        return 0
    text = load_entry()
    problems = check_entry(text)
    if problems:
        for problem in problems:
            print("ERROR: " + problem, file=sys.stderr)
        return 1
    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        if handle.read() != text:
            print("ERROR: /output/entry.txt did not round-trip byte-for-byte",
                  file=sys.stderr)
            return 1
    sys.stdout.write(text)
    sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
