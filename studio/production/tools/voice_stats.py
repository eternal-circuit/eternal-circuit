#!/usr/bin/env python3
"""Voice statistics for generated prose.

Measures rhythm and common machine-prose habits so variants can be compared
with each other and with Proto Draft 2's baseline. The numbers are a guide
for the author's judgment, never a substitute for it.

    python3 studio/production/tools/voice_stats.py FILE [FILE ...]
    python3 studio/production/tools/voice_stats.py --baseline FILE ...

Standard library only. Sentence splitting is approximate; dialogue lines count
as sentences.
"""

import argparse
import re
import statistics as st
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
BASELINE = REPO / "stories" / "the-divine-register" / "genesis-protocol.md"

# Gestures Proto Draft 2 overused. Counts are reported per 1,000 words.
TICS = [r"\blooked at\b", r"\bI know\.", r"\bfor a moment\b", r"\bdidn't say\b",
        r"\bread it (?:twice|again)\b", r"\bneither of them\b"]

# Common signatures of default machine prose. Any hit is worth a second look.
SIGNATURES = [
    r"\btestament to\b", r"\btapestry\b", r"\bdelve", r"\bin the heart of\b",
    r"\bsomething shifted\b", r"\bthe weight of\b", r"\ba beat\b",
    r"breath (?:she|he|they) didn't know", r"\bcouldn't help but\b",
    r"\bthe air (?:was )?thick with\b", r"\ba flicker of\b", r"\bfor a long moment\b",
    r"\bthe silence stretched\b", r"\bpalpable\b", r"\bunspoken\b", r"\bin that moment\b",
    r"\bbarely above a whisper\b", r"\bsteeled (?:her|him)self\b", r"\bverdant\b",
    r"\bnestled\b", r"\bit wasn't [^.?!]{1,40}, it was\b", r"\bnot because [^.?!]{1,40}, but because\b",
    r"\ba reminder that\b", r"\bsomehow\b", r"\bthe hum of\b",
]


def sentences(text):
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"^#.*$|^\*\*\*$|^Date:.*$|^---$", " ", text, flags=re.M)
    parts = re.split(r"(?<=[.!?”\"])\s+", text)
    return [p for p in parts if p.split()]


def stats(text):
    ss = sentences(text)
    lengths = [len(s.split()) for s in ss] or [0]
    words = max(1, len(text.split()))
    dialogue = sum(len(m.split()) for m in re.findall(r"[“\"]([^”\"]*)[”\"]", text))
    name_starts = sum(1 for s in ss if re.match(r"^[“\"]?(She|He|Rachel|Daniel|They|I)\b", s))
    paragraphs = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    first_words = [p.split()[0].strip("“\"") for p in paragraphs if p.split()]
    return {
        "words": len(text.split()),
        "sentences": len(ss),
        "mean": st.mean(lengths),
        "stdev": st.pstdev(lengths),
        "short%": 100 * sum(l <= 8 for l in lengths) / len(lengths),
        "long%": 100 * sum(l >= 25 for l in lengths) / len(lengths),
        "max": max(lengths),
        "dialogue%": 100 * dialogue / words,
        "name_start%": 100 * name_starts / max(1, len(ss)),
        "dashes/1k": 1000 * text.count("—") / words,
        "tics/1k": 1000 * sum(len(re.findall(p, text, re.I)) for p in TICS) / words,
        "signatures": [m.group(0) for p in SIGNATURES for m in re.finditer(p, text, re.I)],
        "para_openers": len(set(first_words)) / max(1, len(first_words)),
    }


COLUMNS = [("words", "{:>6}"), ("mean", "{:>5.1f}"), ("stdev", "{:>5.1f}"), ("short%", "{:>6.0f}"),
           ("long%", "{:>5.0f}"), ("max", "{:>4}"), ("dialogue%", "{:>9.0f}"),
           ("name_start%", "{:>11.0f}"), ("dashes/1k", "{:>9.1f}"), ("tics/1k", "{:>7.1f}"),
           ("para_openers", "{:>12.2f}")]


def row(label, s):
    cells = " ".join(fmt.format(s[k]) for k, fmt in COLUMNS)
    return f"{label[:34]:<34} {cells}"


def header():
    return f"{'text':<34} " + " ".join(f"{k:>{len(fmt.format(0)) if 'f' not in fmt else int(re.search(r'>(\d+)', fmt).group(1))}}"
                                         for k, fmt in COLUMNS)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--baseline", action="store_true", help="include Proto Draft 2 by chapter")
    args = ap.parse_args()

    print(header())
    if args.baseline:
        text = BASELINE.read_text(encoding="utf-8")
        for i, ch in enumerate(re.split(r"^### Chapter \d+: ", text, flags=re.M)[1:], 1):
            print(row(f"Proto 2, chapter {i}", stats(ch)))
    flagged = {}
    for f in args.files:
        s = stats(Path(f).read_text(encoding="utf-8"))
        print(row(Path(f).name, s))
        if s["signatures"]:
            flagged[Path(f).name] = s["signatures"]
    if flagged:
        print("\nMachine-prose signatures found:")
        for name, hits in flagged.items():
            print(f"  {name}: " + "; ".join(sorted(set(hits))))
    print("\nshort% = sentences of 8 words or fewer; long% = 25 words or more; "
          "para_openers = share of distinct first words across paragraphs (higher is more varied).")


if __name__ == "__main__":
    main()
