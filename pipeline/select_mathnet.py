#!/usr/bin/env python3
"""Filter cached MathNet shards to English, image-free, short-solution candidates."""
import ast, json, re, sys
from pathlib import Path
import pyarrow.parquet as pq

ROOT = Path(__file__).resolve().parent.parent
cache = ROOT / "pipeline" / "cache" / "mathnet"
out = []
for f in sorted(cache.glob("s*.parquet")):
    pf = pq.ParquetFile(f)
    cols = [c for c in pf.schema_arrow.names if c != "images"]
    for r in pq.read_table(f, columns=cols).to_pylist():
        p = r["problem_markdown"] or ""
        try:
            sols = ast.literal_eval(r["solutions_markdown"]) if isinstance(r["solutions_markdown"], str) else r["solutions_markdown"]
        except Exception:
            continue
        if not sols or r["language"] not in ("English", "None", None):
            continue
        if re.search(r"[^\x00-\x7f‐-―‘-”]", p) or "![" in p or "![" in sols[0]:
            continue
        if not (80 < len(p) < 700) or not (150 < len(sols[0]) < 2200):
            continue
        topics = list(r["topics_flat"] or [])
        out.append({"id": r["id"], "country": r["country"], "competition": r["competition"], "type": r["problem_type"],
                    "topics": topics, "problem": p, "solution": sols[0], "answer": r["final_answer"]})
(ROOT / "pipeline" / "cache" / "candidates.json").write_text(json.dumps(out, indent=1))
print(len(out), "candidates")
