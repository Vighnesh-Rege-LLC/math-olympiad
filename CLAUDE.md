# Math Olympiad

Mobile-first static web app: math-olympiad flashcards + built-in technique textbook. Modeled on the user's chess tactics tutor. Free, non-commercial. Deploy: Cloudflare Workers static assets, math.olympiad.apps.vighneshrege.com, repo Vighnesh-Rege-LLC/math-olympiad.

## Working style
- Terse. No step-by-step narration. No feature bloat. No UI strings that explain features; orientation cues and one-time first-run cues only.
- Claude is UI/UX designer: decide, don't ask.
- A wrong solution is the worst failure.

## Product
- Two tabs only (bottom bar): Problems, Techniques.
- **Problems**: home loads the best next problem. Card shows no technique, no difficulty. User thinks on paper, optionally opens hint ladder: 1 What is asked, 2 The technique (name, links to its page), then 1–3 variable hints (key idea / next steps), then Full solution. Hint count varies per problem. No answer entry, checking, or timers.
- Self-rating after solution (or whenever): **Got it** (retired forever), **Show again later**, **Struggled** (back sooner). A problem may have several techniques. Every technique name anywhere links to its page.
- **Adaptive selection (hidden)**: per-technique skill from ratings + hint depth. Choose by need (weak/stale techniques) at difficulty near user level, stepping up as problems are retired. Never show retired. Returning problems resurface after N other problems (N_later > N_struggled).
- **Techniques**: textbook. List with mastery indicator per technique, hidden until 5 problems seen on it. Page: what/why it works, how to recognize, 2–3 worked examples stepped one step at a time, mistakes & variations, related techniques, then user's retired and still-struggling problems.
- Technique coverage: pigeonhole, invariants, induction, extremal principle, parity & modular arithmetic, casework, symmetry, AM-GM & inequalities, telescoping & generating functions, constructive arguments, double counting, coordinates, complex numbers & trig in geometry, etc.
- State in localStorage (always try/catch). Light/dark. Safe-area padding. Offline (service worker). Back navigation everywhere. KaTeX bundled locally.

## Data
- ~1,500 problems, easy → olympiad, proof or answer. One JSON data file holds all generated text. No runtime LLM.
- ~800 hard: MathNet (ShadenA/MathNet, CC BY 4.0 except where a country/organization asserts copyright — check `booklet_source`/`country`/`competition`; exclude asserted ones; keep attribution; credits page).
- ~700 ramp (easy→mid): originals written by Claude, no copied text.
- NOT used: MATH, NuminaMath (AoPS/MAA provenance), OTIS (all rights reserved), any AoPS/MAA scraping.
- Per problem: technique tags (multi), hidden difficulty, hints, full solution.
- Verification: every solution gets an independent critic subagent pass that tries to find a gap; run sympy/python wherever a claim is checkable; drop failures. REVIEW.md = random 40 for the user.
- Generation runs in-session (Claude Code subscription, no API key). Pilot ~60 first, report drop rate + sample, then scale.
- Licenses documented in LICENSES.md.

## Engineering
- Static site; pipeline scripts in /pipeline: resumable, quiet.
- Playwright tests: full flow on touch + desktop, no console errors.
- Cloudflare: wrangler static assets config; deploy handled at final stage.

## Stages
1. CLAUDE.md, scaffold, LICENSES.md
2. Technique textbook content
3. Pipeline + 60-problem pilot
4. App
5. Scale to 1,500 + REVIEW.md
6. Playwright tests
7. Cloudflare config/deploy

## Commands
- `python3 -I pipeline/build_techniques.py` and `build_problems.py`: parse `data/**/*.md` into JSON (validates links).
- `.venv/bin/python -I pipeline/check_techniques.py` / `verify_problems.py`: code checks of worked examples and answers.
- `npm run build` (assembles `dist/`), `npm run serve` (http://localhost:4173), `npx playwright test`.
- Content is authored as Markdown in `data/techniques/*.md` and `data/problems/*.md`; `data/*.json` are generated.

## Status (resume here)
- Live at https://math.olympiad.apps.vighneshrege.com (Cloudflare Workers, auto-deploys on push to `main`). Personal use for now.
- Content: 28 technique chapters, problems in batches. Batch log, the batch procedure and open items are in `pipeline/BATCHES.md`. Writer instructions are in `pipeline/BATCH_BRIEF.md`.
- UI (decided): dotted-notebook theme, grouped technique tiles with sticky-note pills, speedometer difficulty (Warm-up / Adaptive / Challenging / Olympiad), History from the clock icon, iPhone safe areas handled in `src/style.css`. Problem screen: header = title, difficulty pill, History, Hint bulb (overlay with the hint ladder, tap outside or the bulb to close), Done check (menu: Got it / Show again later / Struggled). The question is height-capped and compacts when the pad scrolls. Working area (`src/pad.js`) fills the rest: Draw | Type icons plus a one-line toolbar; one finger or pen draws, two fingers scroll a tall page; typed math lines via MathLive (lazy-loaded from `/mathlive/`, pull-up math keyboard). Work is saved per problem in localStorage (`S.w`).
- Pending: reply from the MathNet maintainer about copyright-asserting contests; local-model benchmark when the new Mac arrives.
- Final scale target changed: the plan was 1,500 problems; after batch 2 (212 problems live) the user chose to stop large batches. Add more later with `pipeline/BATCHES.md`.


## Status file

Keep `STATUS.md` at the repo root current. At the end of every task that changes this repo, update it in the same commit:
- Updated: today's date
- Done: what's finished, newest first (keep about 5 lines; drop the oldest)
- In progress: what's underway right now
- Next: the next 2-3 steps

Keep it under 25 lines, plain language, no narration.
