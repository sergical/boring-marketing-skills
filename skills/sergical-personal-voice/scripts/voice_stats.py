#!/usr/bin/env python3
"""voice_stats.py FILE... : countable voice habits per corpus file.

Each file is plain text with the source URL on line 1. Prints one row per file:
words, first-person and second-person rate per 1,000 words, median sentence length,
share of sentences of 4 words or fewer and 30 or more, and raw counts of
! ? ( em dashes, spaced slashes and ALL-CAPS words (3+ letters).
Tutorial files with code blocks skew the sentence numbers; read them with that in mind.
"""
import re
import statistics
import sys

FIRST = {"i", "me", "my", "i'm", "i've", "i'd", "i'll"}
SECOND = {"you", "your", "you're", "you'll", "you've"}


def row(path):
    text = open(path, encoding="utf-8").read().split("\n", 1)[-1]
    words = [w.lower().replace("\u2019", "'") for w in re.findall(r"[A-Za-z'\u2019]+", text)]
    n = max(len(words), 1)
    sents = [s for s in re.split(r"(?<=[.!?])\s+|\n+", text) if len(s.split()) > 1]
    lens = [len(s.split()) for s in sents] or [0]
    caps = re.findall(r"\b[A-Z]{3,}\b", text)
    return {
        "file": path.rsplit("/", 1)[-1],
        "words": n,
        "I/1k": round(1000 * sum(w in FIRST for w in words) / n),
        "you/1k": round(1000 * sum(w in SECOND for w in words) / n),
        "med_sent": statistics.median(lens),
        "short%": round(100 * sum(l <= 4 for l in lens) / len(lens)),
        "long%": round(100 * sum(l >= 30 for l in lens) / len(lens)),
        "!": text.count("!"),
        "?": text.count("?"),
        "(": text.count("("),
        "emdash": text.count("\u2014"),
        "sp_slash": len(re.findall(r"\w / \w", text)),
        "CAPS": len(caps),
    }


def main(paths):
    if not paths:
        print(__doc__)
        return 1
    rows = [row(p) for p in paths]
    cols = list(rows[0])
    print("| " + " | ".join(cols) + " |")
    print("|" + "---|" * len(cols))
    for r in rows:
        print("| " + " | ".join(str(r[c]) for c in cols) + " |")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
