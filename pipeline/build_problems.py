#!/usr/bin/env python3
"""Parse data/problems/*.md into data/problems.json and validate against techniques."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "problems"
LINK = re.compile(r"\[\[([a-z-]+)(?:\|[^\]]*)?\]\]")
BLOCKS = ("statement", "asked", "technique", "hint", "solution")


def parse_file(path):
    out = []
    for chunk in re.split(r"^### ", path.read_text(), flags=re.M)[1:]:
        pid, _, body = chunk.partition("\n")
        meta, hints, cur, buf = {}, [], None, []
        blocks = {}

        def flush():
            if cur is None:
                return
            text = "\n".join(buf).strip()
            if cur == "hint":
                hints.append(text)
            else:
                blocks[cur] = text

        for line in body.splitlines():
            key = line[:-1] if line.endswith(":") else None
            if key in BLOCKS:
                flush()
                cur, buf = key, []
            elif cur is None:
                k, _, v = line.partition(":")
                if k.strip():
                    meta[k.strip()] = v.strip()
            else:
                buf.append(line)
        flush()
        p = {"id": pid.strip(), "type": meta["type"], "difficulty": int(meta["difficulty"]),
             "techniques": [t.strip() for t in meta["techniques"].split(",")],
             "statement": blocks["statement"],
             "hints": [blocks["asked"], blocks["technique"], *hints],
             "solution": blocks["solution"]}
        src = {"kind": meta["source"]}
        for k in ("country", "competition", "mathnet_id"):
            if k in meta:
                src[k] = meta[k]
        p["source"] = src
        out.append(p)
    return out


def main():
    probs = [p for f in sorted(SRC.glob("*.md")) for p in parse_file(f)]
    tech = {t["id"] for t in json.loads((ROOT / "data" / "techniques.json").read_text())}
    errs, seen = [], set()
    for p in probs:
        if p["id"] in seen:
            errs.append(f"dup {p['id']}")
        seen.add(p["id"])
        for t in p["techniques"]:
            if t not in tech:
                errs.append(f"{p['id']}: unknown technique {t}")
        for ref in LINK.findall(json.dumps(p)):
            if ref not in tech:
                errs.append(f"{p['id']}: unknown link {ref}")
        if not 2 <= len(p["hints"]) - 1 <= 4:
            errs.append(f"{p['id']}: {len(p['hints'])} hints")
        if p["type"] not in ("proof", "answer"):
            errs.append(f"{p['id']}: type {p['type']}")
    if errs:
        sys.exit("\n".join(errs))
    (ROOT / "data" / "problems.json").write_text(json.dumps(probs, ensure_ascii=False, indent=1))
    print(len(probs), "problems ok")


main()
