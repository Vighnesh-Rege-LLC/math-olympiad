// Hidden adaptive selection. State lives in store.js; nothing here is shown to the user.

const PRIOR = 0.35;
const clamp = (x, lo, hi) => Math.max(lo, Math.min(hi, x));

export const KNOB = [-2, 0, 2, 4]; // Easier, Auto, Harder, Hardest

export const gaps = (n) => ({
  later: clamp(Math.round(n * 0.1), 8, 40),
  struggled: clamp(Math.round(n * 0.03), 3, 12),
});

const tech = (s, id) => (s.t[id] ||= { skill: PRIOR, seen: [], last: null });

export function pickNext(problems, s, rand = Math.random) {
  const open = problems.filter((p) => s.p[p.id]?.status !== 'retired');
  if (!open.length) return null;

  const due = open
    .filter((p) => s.p[p.id] && s.p[p.id].due <= s.seq)
    .sort((a, b) => s.p[a.id].due - s.p[b.id].due);
  if (due.length) return due[0];

  const fresh = open.filter((p) => !s.p[p.id]);
  if (!fresh.length) return open.sort((a, b) => s.p[a.id].due - s.p[b.id].due)[0];

  let best = null;
  let bestScore = -Infinity;
  for (const p of fresh) {
    let need = 0;
    let w = 0;
    p.techniques.forEach((id, i) => {
      const t = s.t[id];
      const skill = t ? t.skill : PRIOR;
      const stale = t && t.last != null ? Math.min(15, s.seq - t.last) * 0.04 : 0.2;
      const weight = i === 0 ? 1 : 0.5;
      need += weight * (1 - skill + stale);
      w += weight;
    });
    const target = s.level + 0.5 + KNOB[s.knob ?? 1];
    const score = need / w - 0.3 * Math.abs(p.difficulty - target) + rand() * 0.05;
    if (score > bestScore) {
      bestScore = score;
      best = p;
    }
  }
  return best;
}

// depth = number of ladder steps revealed (hints and solution), total = steps available
export function applyRating(problems, s, p, rating, depth, total) {
  const frac = depth / total;
  const outcome = { got: 1 - 0.7 * frac, later: 0.5 - 0.3 * frac, struggled: 0.1 }[rating];
  for (const id of p.techniques) {
    const t = tech(s, id);
    t.skill += 0.35 * (outcome - t.skill);
    if (!t.seen.includes(p.id)) t.seen.push(p.id);
    t.last = s.seq;
  }
  if (rating === 'got') s.level += 0.5 * (p.difficulty >= s.level - 1 ? 1 : 0.4) * (frac < 0.5 ? 1 : 0.6);
  if (rating === 'struggled') s.level -= 0.3 * (p.difficulty <= s.level + 1 ? 1 : 0.4);
  s.level = clamp(s.level, 1, 10);

  s.seq += 1;
  const g = gaps(problems.length);
  const prev = s.p[p.id] || { seen: 0 };
  s.p[p.id] = {
    seen: prev.seen + 1,
    status: rating === 'got' ? 'retired' : rating === 'later' ? 'later' : 'struggled',
    at: Date.now(),
    due: rating === 'got' ? null : s.seq + (rating === 'later' ? g.later : g.struggled),
  };
}

// null until at least 5 problems have been seen on the technique
export function mastery(s, id) {
  const t = s.t[id];
  return t && t.seen.length >= 5 ? t.skill : null;
}
