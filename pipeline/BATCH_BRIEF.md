# Batch brief for problem writers

You write problems for "Math Olympiad", a flashcard app. A wrong solution is the worst failure: be rigorous, check with code, and drop any problem you cannot make airtight.

## Files
- Read `data/techniques.json` (ids and names). Technique tags MUST be ids from it.
- Read `data/problems/pilot-original-a.md` and `pilot-mathnet-a.md` for the exact format, tone and hint style. Match them.
- Write ONLY to your assigned output file (below) and your assigned check script `pipeline/checks/<batch>_<name>.py`. Do not edit anything else. Do NOT run `build_problems.py` (the lead does that; concurrent runs would collide).
- Check scripts run with `/Users/vighneshrege/Projects/math-olympiad/.venv/bin/python -I <script>` (sympy available). Put in one script a check for every computable claim: answers, counts, identities, small-case brute force, extremal values. Run it, fix problems, and make sure it ends with a printed "N checks passed". Proof-only problems still get sanity checks where possible (small cases).

## Entry format (one per problem, separated by a blank line)
```
### <id>
source: original            (or: source: mathnet, plus mathnet_id:, country:, competition: lines)
type: proof | answer
difficulty: 1-10
techniques: id1, id2        (first = primary; 1-3 ids)
statement:
...
asked:
...
technique:
...
hint:
...
hint:
...
solution:
...
```
- Math in `$...$`. Final numeric answers in `\boxed{}` in the solution for `answer` problems.
- `statement`: self-contained, unambiguous, no technique names or hints. No figures: skip problems that need a diagram.
- `asked`: restate what must be found or proved in plain words. It must NOT name the technique.
- `technique`: one or two sentences. It names no "This is a ... problem" (the app already shows the technique as a chip). Say how the technique applies without giving the key idea. Use `[[id]]` links for other technique mentions if natural.
- 1 to 3 `hint:` blocks after `technique:`, progressive: first the key idea, then next steps. Hard problems get 3. Never give the full solution in a hint. Hints must be correct.
- `solution`: complete and rigorous to olympiad grading standard, every step justified, all cases handled. Written in your own words. Not a paraphrase with gaps.
- Difficulty scale: 1-2 warm-up, 3-4 school contest, 5-6 national olympiad early rounds / AIME-like, 7-8 national olympiad finals, 9-10 IMO-level.

## Coverage
Spread problems across the techniques assigned to you, and across difficulty within your band. No duplicates of each other or of the pilot problems (check pilot statements).

## Report
When done, reply with a short list: ids written, ids dropped and why, and anything you are unsure about. Terse.

## Lessons from batch 1 (critics flagged these repeatedly; avoid them)
- The `technique:` text must not give away the key idea or the proof plan. Say what kind of tool applies, nothing more. Hints carry the plan.
- Only tag a technique that the solution actually uses. No decorative secondary tags.
- Do not reuse the worked examples in `data/techniques/*.md`, and do not duplicate any existing problem: `pipeline/cache/existing.txt` lists every existing id, primary technique and the start of its statement. Read it first.
- Geometry: state every orientation/convexity assumption you use, and handle degenerate positions.
- Where a statement needs a fix (missing assumption, false for trivial cases), change it minimally and say so in your report.
- Candidate pool: `pipeline/cache/candidates.json` (6,078 English, image-free MathNet rows; fields id, country, competition, type, topics, problem, solution, answer). Skip competitions that are HMMT, Harvard-MIT, Berkeley, "February"/"November" contests, or other non-national sources. Skip ids already used (grep `mathnet_id:` in `data/problems/*.md`).
- Official solutions are terse or flawed. Write your own complete solution.
