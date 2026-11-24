#!/usr/bin/env python3
"""Render Divine Register record headers with real hashes, and the checksum page.

The printed header's HASH is the actual SHA3-256 of the record's canonical text,
so a reader can verify it. Block counts and the checksum page's parity bytes are
real Reed-Solomon RS(255,223) output. LINEAGE copies, the parent hash and the
corrected-symbol counts are in-world values: the parent hash is derived
deterministically so it never changes between builds, and corrected counts are
supplied by the author (or derived deterministically if omitted).

Canonical payload (what the hash covers):
  * the record's body text only, without its header block;
  * Unicode NFC; UTF-8 without a byte order mark;
  * LF line endings; trailing whitespace stripped from each line;
  * exactly one trailing newline.

Usage (from the repository root):

  python3 studio/production/tools/register_header.py header RECORD_FILE \
      --record 0b00000000 --entry 1 --label 2028-04-16 --addr 0x0000fjfA \
      --copy 4096 --witness "the house" [--corrected 61] [--uncorrectable 0]

  python3 studio/production/tools/register_header.py checksum RECORD_FILE [...]

  python3 studio/production/tools/register_header.py verify RECORD_FILE HASH

Standard library only.
"""

import argparse
import hashlib
import unicodedata
from pathlib import Path

# --- Canonical payload -------------------------------------------------------

def canonical_bytes(text):
    text = unicodedata.normalize("NFC", text.replace("\r\n", "\n").replace("\r", "\n"))
    lines = [line.rstrip() for line in text.split("\n")]
    body = "\n".join(lines).strip("\n") + "\n"
    return body.encode("utf-8")


def record_hash(data):
    return hashlib.sha3_256(data).hexdigest()


def short(h, head=6, tail=6):
    return f"{h[:head]}…{h[-tail:]}"


# --- Reed-Solomon RS(255,223) over GF(2^8), primitive polynomial 0x11D ---------

PRIM = 0x11D
NSYM = 32          # parity symbols per block
K = 255 - NSYM     # 223 data bytes per block

EXP = [0] * 512
LOG = [0] * 256
_x = 1
for _i in range(255):
    EXP[_i] = _x
    LOG[_x] = _i
    _x <<= 1
    if _x & 0x100:
        _x ^= PRIM
for _i in range(255, 512):
    EXP[_i] = EXP[_i - 255]


def gf_mul(a, b):
    if a == 0 or b == 0:
        return 0
    return EXP[LOG[a] + LOG[b]]


def generator_poly(nsym=NSYM):
    g = [1]
    for i in range(nsym):
        nxt = [0] * (len(g) + 1)
        for j, coef in enumerate(g):
            nxt[j] ^= coef
            nxt[j + 1] ^= gf_mul(coef, EXP[i])
        g = nxt
    return g


GEN = generator_poly()


def rs_parity(block):
    """Systematic RS encoding: return the 32 parity bytes for up to 223 data bytes."""
    data = list(block) + [0] * (K - len(block))
    msg = data + [0] * NSYM
    for i in range(K):
        coef = msg[i]
        if coef:
            for j in range(1, len(GEN)):
                msg[i + j] ^= gf_mul(GEN[j], coef)
    return bytes(msg[K:])


def blocks(data):
    return [data[i:i + K] for i in range(0, len(data), K)]


# --- In-world values -----------------------------------------------------------

def parent_hash(h, copy):
    """Deterministic, self-consistent parent link for the rendered lineage."""
    return hashlib.sha3_256(f"lineage:{h}:{copy - 1}".encode()).hexdigest()


def derived_corrected(h, nblocks):
    """Deterministic stand-in for corrected symbols when the author gives none."""
    return int(h[:4], 16) % max(1, nblocks // 2 + 1)


ORDINALS = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth"]


def render_header(args, data):
    h = record_hash(data)
    n = len(blocks(data))
    corrected = args.corrected if args.corrected is not None else derived_corrected(h, n)
    record_index = int(args.record, 2) if args.record.startswith("0b") else 0
    ordinal = ORDINALS[record_index] if record_index < len(ORDINALS) else f"#{record_index + 1}"
    gloss_subject = args.gloss_subject or f"the {ordinal} record"
    lines = [
        f">> RECORD     {args.record}",
        f">> ENTRY      {args.entry:03d}",
        f">> HASH       sha3-256:{short(h)}",
        f">> LINEAGE    copy {args.copy:,} ← {short(parent_hash(h, args.copy))} · {args.chain}",
        f">> ECC        RS(255,223) · {n} blocks · {corrected} symbols corrected · "
        f"{args.uncorrectable} uncorrectable",
        f">> LABEL      {args.label}",
        f">> ADDR       {args.addr}",
        f">> CHECK      {args.check}",
        "",
        f"Here is entered {gloss_subject},",
        "received from the copy before it, as that copy received it,",
        f"kept as it was kept. Witnessed by {args.witness}.",
    ]
    return "\n".join(lines), h


def render_checksum(data, rows=4):
    """Hex view of the first block with its real RS parity bytes."""
    first = blocks(data)[0]
    parity = rs_parity(first)
    out = [f">> BLOCK 0001 · data {len(first)} bytes · parity {len(parity)} bytes",
           f">> sha3-256 {record_hash(data)}"]
    for r in range(rows):
        chunk = first[r * 16:(r + 1) * 16]
        out.append(f"{r * 16:04x}  " + " ".join(f"{b:02x}" for b in chunk))
    out.append("....  " + "·· " * 15 + "··")
    for r in range(0, len(parity), 16):
        chunk = parity[r:r + 16]
        out.append(f"P{r:03x}  " + " ".join(f"{b:02x}" for b in chunk))
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    hp = sub.add_parser("header")
    hp.add_argument("file")
    hp.add_argument("--record", required=True)
    hp.add_argument("--entry", type=int, required=True)
    hp.add_argument("--label", required=True)
    hp.add_argument("--addr", required=True)
    hp.add_argument("--copy", type=int, default=4096)
    hp.add_argument("--chain", default="chain verified")
    hp.add_argument("--corrected", type=int)
    hp.add_argument("--uncorrectable", type=int, default=0)
    hp.add_argument("--check", default="verified")
    hp.add_argument("--witness", default="the house")
    hp.add_argument("--gloss-subject", help='e.g. "the first record of the household"')

    cp = sub.add_parser("checksum")
    cp.add_argument("file")
    cp.add_argument("--rows", type=int, default=4)

    vp = sub.add_parser("verify")
    vp.add_argument("file")
    vp.add_argument("hash")

    args = ap.parse_args()
    data = canonical_bytes(Path(args.file).read_text(encoding="utf-8"))
    if args.cmd == "header":
        text, h = render_header(args, data)
        print(text)
        print(f"\n[full sha3-256: {h}]")
    elif args.cmd == "checksum":
        print(render_checksum(data, args.rows))
    else:
        h = record_hash(data)
        ok = h.startswith(args.hash.lower().replace("sha3-256:", "").split("…")[0])
        print(f"{h}\n{'MATCH' if ok else 'NO MATCH'}")


if __name__ == "__main__":
    main()
