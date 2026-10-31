#!/usr/bin/env python3
"""Parse data/techniques/*.md into data/techniques.json and validate links."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "techniques"
OUT = ROOT / "data" / "techniques.json"
LINK = re.compile(r"\[\[([a-z-]+)(?:\|[^\]]*)?\]\]")


def parse(path):
    text = path.read_text()
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    meta = {}
    for line in m.group(1).splitlines():
        k, v = line.split(":", 1)
        v = v.strip()
        meta[k.strip()] = [s.strip() for s in v[1:-1].split(",") if s.strip()] if v.startswith("[") else v
    sections = re.split(r"^## ", m.group(2), flags=re.M)[1:]
    t = {**meta, "examples": []}
    for sec in sections:
        head, _, body = sec.partition("\n")
        body = body.strip()
        bullets = [re.sub(r"^- ", "", b).strip() for b in re.split(r"\n(?=- )", body)] if body.startswith("- ") else None
        if head == "What it is":
            t["what"] = body
        elif head == "Recognize":
            t["recognize"] = bullets
        elif head == "Mistakes":
            t["mistakes"] = bullets
        elif head == "Variations":
            t["variations"] = bullets
        elif head.startswith("Example: "):
            pm = re.search(r"\*\*Problem\.\*\*(.*?)\n(?=\d+\. )", body, re.S)
            steps = [re.sub(r"^\d+\. ", "", s).strip() for s in re.split(r"\n(?=\d+\. )", body[pm.end():].split("\n\n")[0].strip())]
            note = body[pm.end():].split("\n\n", 1)[1].strip() if "\n\n" in body[pm.end():] else None
            ex = {"title": head[9:], "problem": pm.group(1).strip(), "steps": steps}
            if note:
                ex["note"] = note
            t["examples"].append(ex)
        else:
            sys.exit(f"{path.name}: unknown section {head!r}")
    return t


def main():
    techs = [parse(p) for p in sorted(SRC.glob("*.md"))]
    ids = {t["id"] for t in techs}
    errs = []
    for t in techs:
        blob = json.dumps(t)
        for ref in set(LINK.findall(blob)) | set(t.get("related", [])):
            if ref not in ids:
                errs.append(f"{t['id']}: unknown link {ref}")
        for k in ("what", "recognize", "mistakes", "variations"):
            if not t.get(k):
                errs.append(f"{t['id']}: missing {k}")
        if not 2 <= len(t["examples"]) <= 3:
            errs.append(f"{t['id']}: {len(t['examples'])} examples")
    if errs:
        sys.exit("\n".join(errs))
    OUT.write_text(json.dumps(techs, ensure_ascii=False, indent=1))
    print(f"{len(techs)} techniques ok")


main()
