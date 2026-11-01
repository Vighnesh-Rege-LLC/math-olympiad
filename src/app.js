import { load, save } from './store.js';
import { pickNext, applyRating, mastery } from './select.js';
import { rich } from './render.js';
import { mountPad } from './pad.js';

const app = document.getElementById('app');
const GROUPS = ['Proof methods', 'Combinatorics', 'Number theory', 'Algebra', 'Inequalities', 'Geometry'];
const LEVELS = ['Warm-up', 'Adaptive', 'Challenging', 'Olympiad'];
const LABELS = ['What is being asked', 'The technique', 'The key idea', 'The next step'];
const BACK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>';
const CLOCK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3.5 12a8.5 8.5 0 1 0 2.6-6.1M3.5 4.5v4h4M12 7.5V12l3 2"/></svg>';
const BULB = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/></svg>';
const CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7"/></svg>';
const WARN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l9 16H3zM12 10v4M12 17h.01"/></svg>';
const LATER = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 6v6l4 2M4 12a8 8 0 1 0 2.3-5.7"/></svg>';
const CHEVRON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>';

// glyph and short name shown on technique tiles
const GLYPH = {
  pigeonhole: 'n+1', invariants: 'Δ=0', induction: 'P(n)', extremal: 'max', descent: '↓', parity: '2k+1',
  'modular-arithmetic': 'mod', casework: 'a|b', coloring: '▦', symmetry: '⇋', constructive: '∃', 'double-counting': '⇄',
  recursion: 'aₙ', 'graph-theory': '•–•', telescoping: '∑', 'generating-functions': 'f(x)', 'am-gm': '≥', 'cauchy-schwarz': '⟨·,·⟩',
  'functional-equations': 'f(f)', polynomials: 'xⁿ', divisibility: 'gcd', diophantine: 'ax+by', expectation: 'E[X]',
  coordinates: '(x,y)', 'complex-numbers': 'ℂ', trigonometry: 'sin', 'angle-chasing': '∠', 'similar-triangles': '△',
};
const SHORT = {
  invariants: 'Invariants', 'am-gm': 'AM-GM', 'cauchy-schwarz': 'Cauchy–Schwarz', descent: 'Descent',
  'angle-chasing': 'Angle chasing', 'similar-triangles': 'Similar triangles', expectation: 'Expectation', divisibility: 'Divisibility',
  symmetry: 'Symmetry', polynomials: 'Polynomials', trigonometry: 'Trigonometry', 'complex-numbers': 'Complex numbers',
  coordinates: 'Coordinates', 'graph-theory': 'Graph theory', constructive: 'Constructive', coloring: 'Coloring',
};

let data;
let S;
let cleanup = null;
const byId = {};
const tech = {};
const names = {};

const $ = (html) => {
  const t = document.createElement('template');
  t.innerHTML = html.trim();
  return t.content.firstElementChild;
};
const R = (text) => rich(text, names);
const shortName = (id) => SHORT[id] || names[id];

function head(title, back, right = '') {
  const h = $(`<header class="head">${back ? `<button class="back" aria-label="Back">${BACK}</button>` : ''}<h1>${title}</h1>${right}</header>`);
  h.querySelector('.back')?.addEventListener('click', () => {
    if (history.length > 1) history.back();
    else location.hash = back;
  });
  return h;
}

const label = (i, total) => (i === total - 1 ? 'Full solution' : LABELS[Math.min(i, 3)]);

function source(p) {
  if (p.source.kind !== 'mathnet') return '';
  const { competition: c, country: k } = p.source;
  return `<div class="src">${[c, k].filter((x, i, a) => a.indexOf(x) === i).join(' · ')}</div>`;
}

function workFor(pid) {
  S.w ||= {};
  return (S.w[pid] ||= { s: [], l: [''], m: 'draw' });
}
let saveTimer = null;
const saveSoon = () => {
  clearTimeout(saveTimer);
  saveTimer = setTimeout(() => save(S), 300);
};
window.addEventListener('pagehide', () => save(S));

function stepEl(p, steps, i) {
  const total = steps.length;
  const last = i === total - 1;
  const chips = i === 1 ? `<div class="chips">${p.techniques.map((id) => `<a href="#/t/${id}">${shortName(id)}</a>`).join('')}</div>` : '';
  const body = last ? `<div class="body">${R(steps[i])}</div>${source(p)}` : `<div class="hint">${chips}${R(steps[i])}</div>`;
  return $(`<div class="step ${last ? 'solution' : ''}"><h3>${label(i, total)}</h3>${body}</div>`);
}

// the problem screen: header with popovers, collapsible question, then the working area filling the rest
function viewWork(p, { play, rev, onRev, onRate }) {
  const frag = document.createDocumentFragment();
  const steps = [...p.hints, p.solution];
  const total = steps.length;

  const right = (play ? `<a class="iconbtn" href="#/history" aria-label="History">${CLOCK}</a>` : '')
    + `<button class="iconbtn" data-act="hint" aria-label="Hint" aria-expanded="false">${BULB}</button>`
    + (play ? `<button class="iconbtn solid" data-act="done" aria-label="Done" aria-expanded="false">${CHECK}</button>` : '');
  const wrap = $('<div class="headwrap"></div>');
  wrap.append(head('Problem', play ? null : '#/history', right));
  const scrim = $('<div class="scrim" hidden></div>');
  const hb = wrap.querySelector('[data-act="hint"]');
  const db = wrap.querySelector('[data-act="done"]');

  let dialPop = null;
  let pill = null;
  const hintPop = $('<div class="pop hintpop" role="dialog" aria-label="Hints" hidden><div class="pop-body"><div class="steps"></div></div><div class="pop-foot"><span class="count"></span><button class="sticky" data-more type="button">More hints</button></div></div>');
  const donePop = play ? $(`<div class="pop donemenu" role="menu" aria-label="How did it go" hidden>
    <button role="menuitem" class="got" data-rate="got">${CHECK}Got it</button>
    <button role="menuitem" data-rate="later">${LATER}Show again later</button>
    <button role="menuitem" data-rate="struggled">${WARN}Struggled</button></div>`) : null;
  wrap.append(hintPop);
  if (donePop) wrap.append(donePop);

  const closeAll = () => {
    hintPop.hidden = true;
    if (donePop) donePop.hidden = true;
    dialPop?.remove();
    dialPop = null;
    scrim.hidden = true;
    hb.setAttribute('aria-expanded', 'false');
    hb.classList.remove('on');
    db?.setAttribute('aria-expanded', 'false');
    pill?.setAttribute('aria-expanded', 'false');
  };
  scrim.onclick = closeAll;
  const onKey = (e) => e.key === 'Escape' && closeAll();
  document.addEventListener('keydown', onKey);
  cleanup = () => document.removeEventListener('keydown', onKey);

  // difficulty pill and speedometer (play only)
  if (play) {
    const k = S.knob ?? 1;
    pill = $(`<button class="sticky" data-knob="${k}" aria-haspopup="dialog" aria-expanded="false" aria-label="Difficulty: ${LEVELS[k]}">${LEVELS[k]}${CHEVRON}</button>`);
    wrap.querySelector('h1').after(pill);
    const pick = (i) => {
      S.knob = i;
      save(S);
      pill.dataset.knob = i;
      pill.setAttribute('aria-label', `Difficulty: ${LEVELS[i]}`);
      pill.firstChild.textContent = LEVELS[i];
      const next = dial(i, pick);
      dialPop.replaceWith(next);
      dialPop = next;
      setTimeout(closeAll, 350);
    };
    pill.onclick = () => {
      if (dialPop) return closeAll();
      closeAll();
      dialPop = dial(S.knob ?? 1, pick);
      wrap.append(dialPop);
      scrim.hidden = false;
      pill.setAttribute('aria-expanded', 'true');
    };
  }

  // hints overlay
  const stepsEl = hintPop.querySelector('.steps');
  const more = hintPop.querySelector('[data-more]');
  const count = hintPop.querySelector('.count');
  let cue = null;
  const foot = () => {
    count.textContent = `${rev} of ${total}`;
    more.hidden = rev >= total;
    more.textContent = rev === total - 1 ? 'Full solution' : 'More hints';
  };
  hb.onclick = () => {
    if (!hintPop.hidden) return closeAll();
    closeAll();
    if (rev === 0) {
      rev = 1;
      onRev(rev);
      cue?.remove();
    }
    stepsEl.replaceChildren(...Array.from({ length: rev }, (_, i) => stepEl(p, steps, i)));
    foot();
    hintPop.hidden = false;
    scrim.hidden = false;
    hb.setAttribute('aria-expanded', 'true');
    hb.classList.add('on');
  };
  more.onclick = () => {
    const el = stepEl(p, steps, rev);
    stepsEl.append(el);
    rev += 1;
    onRev(rev);
    foot();
    el.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
  };

  // done menu
  if (db) {
    db.onclick = () => {
      if (!donePop.hidden) return closeAll();
      closeAll();
      donePop.hidden = false;
      scrim.hidden = false;
      db.setAttribute('aria-expanded', 'true');
    };
    donePop.querySelectorAll('[data-rate]').forEach((b) => (b.onclick = () => onRate(b.dataset.rate, rev, total)));
  }

  // the question: capped height, compacts when the pad scrolls
  const q = $(`<div class="qwrap" data-state="full"><div class="statement">${R(p.statement)}</div><button class="qtoggle" type="button" aria-label="Expand question" hidden>${CHEVRON}</button></div>`);
  const qt = q.querySelector('.qtoggle');
  const fit = () => {
    const clipped = q.scrollHeight > q.clientHeight + 2;
    q.classList.toggle('clipped', clipped);
    qt.hidden = !clipped && q.dataset.state !== 'open';
  };
  qt.onclick = () => {
    q.dataset.state = q.dataset.state === 'open' ? 'full' : 'open';
    setTimeout(fit, 220);
  };

  const pad = mountPad(workFor(p.id), {
    onChange: (w) => {
      w.at = Date.now();
      cue?.remove();
      saveSoon();
    },
  });
  const sc = pad.querySelector('.scroller');
  sc.addEventListener('scroll', () => {
    if (sc.scrollTop > 40 && q.dataset.state !== 'compact') {
      q.dataset.state = 'compact';
      setTimeout(fit, 220);
    } else if (sc.scrollTop < 4 && q.dataset.state === 'compact') {
      q.dataset.state = 'full';
      setTimeout(fit, 220);
    }
  }, { passive: true });
  if (play && S.cue && rev === 0) {
    cue = $('<div class="cue">Work it out on paper first.</div>');
    pad.querySelector('.surface').append(cue);
  }
  setTimeout(fit, 60);
  window.addEventListener('resize', fit);

  frag.append(scrim, wrap, q, pad);
  return frag;
}

// speedometer: four arcs across a half circle, needle on the active one
function dial(k, onPick) {
  const cx = 136, cy = 132;
  const pt = (r, deg) => [cx - r * Math.cos((deg * Math.PI) / 180), cy - r * Math.sin((deg * Math.PI) / 180)];
  const fill = ['#bfd6ff', 'var(--c1)', 'var(--c4)', 'var(--c3)'];
  const arcs = LEVELS.map((n, i) => {
    const [x0, y0] = pt(110, i * 45 + 2.5);
    const [x1, y1] = pt(110, (i + 1) * 45 - 2.5);
    return `<path class="seg" data-level="${i}" d="M${x0.toFixed(1)} ${y0.toFixed(1)}A110 110 0 0 1 ${x1.toFixed(1)} ${y1.toFixed(1)}" style="stroke:${fill[i]};opacity:${i === k ? 1 : 0.45}"></path>`;
  }).join('');
  const [nx, ny] = pt(78, k * 45 + 22.5);
  const box = $(`<div class="dialpop" role="dialog" aria-label="Difficulty">
    <svg viewBox="0 0 272 150" aria-hidden="true">${arcs}<line class="needle" x1="${cx}" y1="${cy}" x2="${nx.toFixed(1)}" y2="${ny.toFixed(1)}"></line><circle class="hub" cx="${cx}" cy="${cy}" r="9"></circle></svg>
    <div class="names" role="radiogroup" aria-label="Difficulty">${LEVELS.map((n, i) => `<button role="radio" aria-checked="${i === k}" data-level="${i}">${n}</button>`).join('')}</div>
  </div>`);
  box.querySelectorAll('[data-level]').forEach((el) => el.addEventListener('click', () => onPick(+el.dataset.level)));
  return box;
}

function viewProblems() {
  let p = S.cur && byId[S.cur.id] && S.p[S.cur.id]?.status !== 'retired' ? byId[S.cur.id] : null;
  if (!p) {
    p = pickNext(data.problems, S);
    if (!p) {
      const frag = document.createDocumentFragment();
      frag.append(head('Problem'), $('<p class="empty">Every problem is retired.<br><a href="#/techniques">Review techniques</a></p>'));
      return frag;
    }
    S.cur = { id: p.id, rev: 0 };
    save(S);
  }
  return viewWork(p, {
    play: true,
    rev: S.cur.rev,
    onRev: (n) => {
      S.cur.rev = n;
      S.cue = false;
      save(S);
    },
    onRate: (rating, depth, total) => {
      applyRating(data.problems, S, p, rating, depth, total);
      S.cur = null;
      save(S);
      render();
    },
  });
}

function viewReview(id) {
  const p = byId[id];
  if (!p) {
    const frag = document.createDocumentFragment();
    frag.append(head('Problem', '#/history'), $('<p class="empty">Not found.</p>'));
    return frag;
  }
  return viewWork(p, { play: false, rev: 0, onRev() {}, onRate() {} });
}

const dayLabel = (t) => {
  if (!t) return 'Earlier';
  const d = new Date(t);
  const now = new Date();
  const day = (x) => new Date(x.getFullYear(), x.getMonth(), x.getDate()).getTime();
  const diff = Math.round((day(now) - day(d)) / 86400000);
  return diff <= 0 ? 'Today' : diff === 1 ? 'Yesterday' : 'Earlier';
};

function histItem(p, rec) {
  const name = { retired: 'Retired', later: 'Later', struggled: 'Struggled' }[rec.status] + (rec.seen > 1 ? ` · ${rec.seen}×` : '');
  return $(`<li><a href="#/p/${p.id}"><div class="meta"><span class="st ${rec.status}">${name}</span><span class="tn">${shortName(p.techniques[0])}</span></div><div class="txt">${R(p.statement)}</div></a></li>`);
}

function viewHistory() {
  const frag = document.createDocumentFragment();
  frag.append(head('History', '#/'));
  const all = Object.entries(S.p).filter(([id]) => byId[id]).map(([id, rec]) => ({ p: byId[id], rec })).sort((a, b) => (b.rec.at || 0) - (a.rec.at || 0));
  const counts = { all: all.length, retired: all.filter((x) => x.rec.status === 'retired').length };
  counts.back = counts.all - counts.retired;
  let filter = 'all';
  const filters = $(`<div class="filters" role="group" aria-label="Filter"></div>`);
  const list = $('<div></div>');
  const draw = () => {
    filters.replaceChildren(...[['all', 'All'], ['retired', 'Retired'], ['back', 'Coming back']].map(([key, text]) => {
      const b = $(`<button data-filter="${key}" aria-pressed="${filter === key}">${text} ${counts[key]}</button>`);
      b.onclick = () => ((filter = key), draw());
      return b;
    }));
    list.replaceChildren();
    const rows = all.filter((x) => filter === 'all' || (filter === 'retired') === (x.rec.status === 'retired'));
    if (!rows.length) return list.append($('<p class="empty">Nothing here yet.</p>'));
    let ul = null;
    let last = null;
    for (const { p, rec } of rows) {
      const g = dayLabel(rec.at);
      if (g !== last) {
        list.append($(`<div class="gh">${g}</div>`));
        ul = $('<ul class="hist"></ul>');
        list.append(ul);
        last = g;
      }
      ul.append(histItem(p, rec));
    }
  };
  draw();
  frag.append(filters, list);
  return frag;
}

function viewTechniques() {
  const frag = document.createDocumentFragment();
  frag.append(head('Techniques'));
  frag.append($(`<p class="sub">${data.techniques.length} chapters</p>`));
  for (const g of GROUPS) {
    const items = data.techniques.filter((t) => t.group === g);
    if (!items.length) continue;
    frag.append($(`<div class="gh">${g}</div>`));
    const grid = $('<div class="tiles"></div>');
    items.forEach((t, i) => {
      const m = mastery(S, t.id);
      const ring = m == null ? '' : `<span class="ring" style="--p:${Math.max(8, Math.round(m * 100))}" role="img" aria-label="Mastery ${Math.round(m * 100)} percent"></span>`;
      grid.append($(`<a class="tile k${(i % 4) + 1}" href="#/t/${t.id}"><span class="glyph" aria-hidden="true">${GLYPH[t.id] || '∑'}</span>${ring}<span class="pill">${shortName(t.id)}</span></a>`));
    });
    frag.append(grid);
  }
  frag.append($('<a class="footer-link" href="#/credits">Credits</a>'));
  return frag;
}

function viewTechnique(id) {
  const t = tech[id];
  const frag = document.createDocumentFragment();
  frag.append(head(t ? t.name : 'Technique', '#/techniques'));
  if (!t) return frag.append($('<p class="empty">Not found.</p>')), frag;

  const sec = (title, inner) => $(`<section class="sec"><h2>${title}</h2>${inner}</section>`);
  const list = (items) => `<ul>${items.map((x) => `<li>${R(x).replace(/^<p>|<\/p>$/g, '')}</li>`).join('')}</ul>`;

  frag.append(sec('What it is', `<div class="prose">${R(t.what)}</div>`));
  frag.append(sec('Recognize it', `<div class="prose">${list(t.recognize)}</div>`));

  const ex = sec('Worked examples', '');
  for (const e of t.examples) {
    const box = $(`<div class="ex"><h3>${e.title}</h3><div class="prob">${R('**Problem.** ' + e.problem)}</div><ol></ol></div>`);
    const ol = box.querySelector('ol');
    let n = 0;
    const btn = $(`<button class="btn" data-next>Next step</button>`);
    btn.onclick = () => {
      const li = $(`<li>${R(e.steps[n++])}</li>`);
      ol.append(li);
      li.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      if (n === e.steps.length) {
        btn.remove();
        if (e.note) box.append($(`<div class="prose">${R(e.note)}</div>`));
      }
    };
    box.append(btn);
    ex.append(box);
  }
  frag.append(ex);
  frag.append(sec('Common mistakes', `<div class="prose">${list(t.mistakes)}</div>`));
  frag.append(sec('Variations', `<div class="prose">${list(t.variations)}</div>`));
  frag.append(sec('Related', `<div class="chips">${t.related.map((r) => `<a href="#/t/${r}">${shortName(r)}</a>`).join('')}</div>`));

  const mine = data.problems.filter((p) => p.techniques.includes(id) && ['retired', 'struggled'].includes(S.p[p.id]?.status));
  if (mine.length) {
    const ul = $('<ul class="hist"></ul>');
    for (const p of mine) ul.append(histItem(p, S.p[p.id]));
    const mineSec = sec('Your problems', '');
    mineSec.append(ul);
    frag.append(mineSec);
  }
  return frag;
}

function viewCredits() {
  const frag = document.createDocumentFragment();
  frag.append(head('Credits', '#/techniques'));
  const seen = new Map();
  for (const p of data.problems) if (p.source.kind === 'mathnet') seen.set(p.source.competition, p.source.country);
  frag.append($(`<div class="prose"><p>Olympiad problems and solutions from national and regional contests are adapted from <a href="https://mathnet.mit.edu">MathNet</a> (Alshammari et al., ICLR 2026, CC BY 4.0). Rights asserted by national teams or contest organizers remain with them. Hints and rewritten solutions are by this project. Other problems are original.</p><ul>${[...seen].map(([c, k]) => `<li>${[c, k].filter((x, i, a) => a.indexOf(x) === i).join(', ')}</li>`).join('')}</ul></div>`));
  return frag;
}

function render() {
  cleanup?.();
  cleanup = null;
  const hash = location.hash.replace(/^#/, '') || '/';
  const [, a, b] = hash.split('/');
  let view;
  let tab = 'techniques';
  if (a === '' || a === undefined) (view = viewProblems()), (tab = 'problems');
  else if (a === 'techniques') view = viewTechniques();
  else if (a === 't') view = viewTechnique(b);
  else if (a === 'p') (view = viewReview(b)), (tab = 'problems');
  else if (a === 'history') (view = viewHistory()), (tab = 'problems');
  else if (a === 'credits') view = viewCredits();
  else (view = viewProblems()), (tab = 'problems');
  app.classList.toggle('fit', tab === 'problems' && a !== 'history');
  app.replaceChildren(view);
  document.querySelectorAll('#tabs a').forEach((el) => {
    if (el.dataset.tab === tab) el.setAttribute('aria-current', 'page');
    else el.removeAttribute('aria-current');
  });
  window.scrollTo(0, 0);
}

async function boot() {
  S = load();
  for (const [id, w] of Object.entries(S.w || {})) if (!w.s?.length && !(w.l || []).some((x) => x)) delete S.w[id];
  data = await (await fetch('/data.json')).json();
  for (const t of data.techniques) {
    tech[t.id] = t;
    names[t.id] = t.name;
  }
  for (const p of data.problems) byId[p.id] = p;
  window.addEventListener('hashchange', render);
  render();
  if ('serviceWorker' in navigator) navigator.serviceWorker.register('/sw.js').catch(() => {});
}

boot();
