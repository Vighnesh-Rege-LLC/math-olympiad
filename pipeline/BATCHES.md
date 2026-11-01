# Batch log and how to resume

Content is authored as Markdown in `data/problems/<batch>-<name>.md` and `data/techniques/*.md`. Everything else is generated.

## Process for one batch (what was done for batches 1 and 2)
1. **Pool.** `python3 -I pipeline/fetch_mathnet.py FIRST LAST` downloads MathNet shards (0 to 55; 0-24 are cached locally, `pipeline/cache/` is git-ignored). `.venv/bin/python -I pipeline/select_mathnet.py` filters them to `pipeline/cache/candidates.json` (English, no images, bounded length). Regenerate `pipeline/cache/existing.txt` (id, primary technique, first 110 chars of every existing statement) so writers avoid duplicates.
2. **Writers.** Four subagents in parallel (two hard MathNet adaptations, two originals), each given `pipeline/BATCH_BRIEF.md`, a unique id range and a technique/difficulty focus. Each writes one `data/problems/batchN-*.md` and one `pipeline/checks/batchN_*.py` (sympy/brute-force checks, must print "N checks passed").
3. **Critics.** One independent opus subagent per file tries to find gaps (answers, rigor, hints, tags, difficulty). Fixes are applied by hand. Problems that repeat a technique chapter's worked example are dropped.
4. **Merge and ship.** `python3 -I pipeline/build_problems.py` (validates ids and links), run every `pipeline/checks/*.py` and `pipeline/verify_problems.py` with `.venv/bin/python -I`, `python3 -I pipeline/make_review.py` (new random 40 for `REVIEW.md`), `npx playwright test`, then commit and push `main`. Cloudflare redeploys automatically.

Rules that matter: a wrong solution is the worst failure; the `technique:` field must not give away the key idea; official MathNet solutions are not copied (they were flawed in about a quarter of the cases checked).

## Batches
| Batch | Files | Problems | Notes |
|---|---|---|---|
| Pilot | `pilot-*.md` | 60 (24 MathNet, 36 original) | Hand-written in the main session. `pipeline/verify_problems.py` holds its checks. |
| 1 | `batch1-*.md` | +93 (49 MathNet hard, 44 original; 7 dropped as duplicates of chapter examples) | Live. Critic fixes applied. Total 153. |
| 2 | `batch2-*.md` | +59 (30 MathNet hard, 29 original; o107 dropped as a near-duplicate of a chapter line) | Live. Total 212. Hard files c/d (difficulty 7-8, thin techniques), original files c/d (difficulty 1-2 and 5-6). Run as 15-problem agents, two at a time, because four opus agents at once hit the usage limit twice. |

IDs: originals `o01...`, MathNet `m01...`. Batch 1 used o37-o86 and m25-m74. Batch 2 used o87-o116 (o107 dropped) and m75-m89, m100-m114 (m90-m99 unused). Next free: `o117`, `m115`.

## Known thin spots
- Very hardest (9-10) is sparse; difficulty 8 is thin; 1-2 are about 25 problems.
- Probability and expectation: few national-olympiad candidates in MathNet (one hard one, m103, tagged recursion); expectation is mostly originals (about 8).
- Several MathNet problems come from US and international contests (USAMO, USA TST, IMO Shortlist), the ones most likely to be on the maintainer's copyright list.
- Only 24 of 56 MathNet shards downloaded (`pipeline/fetch_mathnet.py 25 55` fetches the rest).
- Usage tip: keep writer agents to about 15 problems each and run two at a time; ask them to save every problem as it is finished.

## Open items
- **MathNet copyright list.** Emailed shaden@mit.edu on 2026-10-31 asking which contests assert copyright (v0 parquet lacks `booklet_source`). When answered, drop those contests' problems (`grep -l` the competition in `data/problems/`) and rebuild. Until then the app is for personal use only; see `LICENSES.md`.
- **Local model.** Planned: when the M3/M4 16 GB Mac arrives, benchmark Qwen 3.5 9B, Qwen3 8B and DeepSeek-R1-Distill-14B (MLX) on the 60 pilot problems, whose solutions are verified. Use a local model only for tagging, hint drafts from checked solutions and easy first drafts that code verifies. Never for unverified proofs.
- **Cloudflare.** Worker `math-olympiad` via Workers Builds from GitHub `Vighnesh-Rege-LLC/math-olympiad`, custom domain `math.olympiad.apps.vighneshrege.com` (see `wrangler.jsonc`).
