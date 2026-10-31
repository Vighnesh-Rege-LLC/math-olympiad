#!/usr/bin/env python3
"""Write REVIEW.md: a seeded random sample of problems for manual reading."""
import json, random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
probs = json.loads((ROOT / "data" / "problems.json").read_text())
names = {t["id"]: t["name"] for t in json.loads((ROOT / "data" / "techniques.json").read_text())}
random.seed(40)
sample = random.sample(probs, min(40, len(probs)))
out = ["# Review sample", "", f"{len(sample)} problems drawn at random (seed 40) from {len(probs)}. Check the statement, the hints, and above all the solution.", ""]
for p in sample:
    src = p["source"]
    origin = "original" if src["kind"] == "original" else f"{src['competition']} ({src['country']}), MathNet {src['mathnet_id']}"
    out += [f"## {p['id']} · difficulty {p['difficulty']} · {', '.join(names[t] for t in p['techniques'])}", f"*{origin}*", "", "**Statement**", "", p["statement"], ""]
    labels = ["What is being asked", "The technique", "The key idea", "The next step", "The next step"]
    for i, h in enumerate(p["hints"]):
        out += [f"**Hint {i + 1}: {labels[min(i, 4)]}**", "", h, ""]
    out += ["**Solution**", "", p["solution"], "", "---", ""]
(ROOT / "REVIEW.md").write_text("\n".join(out))
print(len(sample), "problems in REVIEW.md")
