#!/usr/bin/env python3
"""Download MathNet parquet shards into pipeline/cache/mathnet (resumable, quiet).
Usage: fetch_mathnet.py FIRST LAST   (shard numbers 0..55, inclusive)"""
import sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
out = ROOT / "pipeline" / "cache" / "mathnet"
out.mkdir(parents=True, exist_ok=True)
first, last = int(sys.argv[1]), int(sys.argv[2])
for i in range(first, last + 1):
    dest = out / f"s{i:02d}.parquet"
    if dest.exists() and dest.stat().st_size > 0:
        continue
    url = f"https://huggingface.co/datasets/ShadenA/MathNet/resolve/main/data/all/train-{i:05d}-of-00056.parquet"
    tmp = dest.with_suffix(".part")
    urllib.request.urlretrieve(url, tmp)
    tmp.rename(dest)
print("shards present:", len(list(out.glob("s*.parquet"))))
