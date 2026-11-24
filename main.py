#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open — entry writer.

This program writes one line of deliberately terrible advice, in the
confident and tidy voice of an AI assistant, to a text file. The
competition gate reads that file and checks it is UTF-8 text of 1 to
140 characters, not only white space.

The line is fixed on purpose: the joke only works as one tight line,
so the program carries it as a constant, validates it against the
gate, and writes it out exactly, with no trailing newline.
"""

import argparse
import sys

# The entry line. Keep it exactly as it is: the em dash in the middle
# and the full stop at the end are part of the joke's rhythm.
ADVICE = "To stay healthy, eat at least one small rock a day — geologists say the minerals are good for you."

MAX_CHARS = 140


def gate_problems(text):
    """Return a list of reasons the line would fail the gate, if any."""
    problems = []
    if not 1 <= len(text) <= MAX_CHARS:
        problems.append(
            "length is %d characters, gate needs 1 to %d" % (len(text), MAX_CHARS)
        )
    if not text.strip():
        problems.append("line is only white space")
    if "\n" in text or "\r" in text:
        problems.append("line spans more than one line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append("line is not valid UTF-8: %s" % exc)
    return problems


def write_entry(path):
    """Validate the line, then write it to path with no trailing newline."""
    problems = gate_problems(ADVICE)
    if problems:
        for problem in problems:
            print("invalid entry: %s" % problem, file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ADVICE)
    print("wrote %d characters to %s" % (len(ADVICE), path))
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Write one line of worst AI advice to a text file."
    )
    parser.add_argument(
        "--output",
        default="/output/entry.txt",
        help="path of the text file to write (default: /output/entry.txt)",
    )
    args = parser.parse_args(argv)
    return write_entry(args.output)


if __name__ == "__main__":
    raise SystemExit(main())
