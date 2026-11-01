// Shared working area: freehand ink drawn over typed math lines, on a tall scrollable page.
// One finger (or pen) draws, two fingers scroll. work = { s: strokes, l: latex lines, m: 'draw' | 'type' }
// stroke = { c: colour index, w: width, p: [x, y, x, y, ...] } in surface coordinates.

const PEN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20l1-4L16.5 4.5a2 2 0 0 1 3 3L8 19z M14 7l3 3"/></svg>';
const ERASER = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 20h11M5 15l8-9a2 2 0 0 1 3 0l3 3a2 2 0 0 1 0 3l-6 6H9z"/></svg>';
const UNDO = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 7L4 12l5 5M4 12h10a6 6 0 0 1 0 12"/></svg>';
const TRASH = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 7h14M10 7V4h4v3M7 7l1 13h8l1-13"/></svg>';
const KEYS = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="6" width="18" height="12" rx="2"/><path d="M7 10h.01M11 10h.01M15 10h.01M7 14h10"/></svg>';
const PLUS = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>';

let mlPromise = null;
function loadMathLive() {
  mlPromise ||= import('/mathlive/mathlive.js').then((m) => {
    m.MathfieldElement.fontsDirectory = '/mathlive/fonts';
    m.MathfieldElement.soundsDirectory = null;
    return m;
  });
  return mlPromise;
}

const html = (s) => {
  const t = document.createElement('template');
  t.innerHTML = s.trim();
  return t.content.firstElementChild;
};

export function mountPad(work, { onChange }) {
  work.s ||= [];
  work.l ||= [''];
  work.m ||= 'draw';
  let tool = 'pen';
  let color = 0;
  let hist = [];
  let cur = null;
  let erasing = false;
  let built = false;
  const touches = new Map(); // pointerId -> last y, for two-finger scrolling
  let scrolling = false;

  const root = html(`<section class="work" data-mode="${work.m}">
    <div class="work-bar">
      <div class="seg" role="group" aria-label="Input mode">
        <button data-mode-btn="draw" aria-label="Draw" aria-pressed="${work.m === 'draw'}">${PEN}</button>
        <button data-mode-btn="type" aria-label="Type" aria-pressed="${work.m === 'type'}">${KEYS}</button>
      </div>
      <span class="vr"></span>
      <div class="tools" role="toolbar" aria-label="Pad tools">
        <button class="tool" data-tool="pen" aria-label="Pen" aria-pressed="true">${PEN}</button>
        <button class="tool" data-tool="eraser" aria-label="Eraser" aria-pressed="false">${ERASER}</button>
        <button class="dot" data-color="0" aria-label="Ink" aria-pressed="true"></button>
        <button class="dot" data-color="2" aria-label="Red ink" aria-pressed="false"></button>
        <span class="grow"></span>
        <button class="tool" data-act="undo" aria-label="Undo">${UNDO}</button>
        <button class="tool" data-act="clear" aria-label="Clear pad">${TRASH}</button>
      </div>
      <button class="tool sticky-tool" data-act="addline" aria-label="Add line">${PLUS}</button>
    </div>
    <div class="scroller"><div class="surface"><div class="lines"></div><canvas class="ink" aria-label="Scratch pad"></canvas></div></div>
  </section>`);
  const scroller = root.querySelector('.scroller');
  const surface = root.querySelector('.surface');
  const linesEl = root.querySelector('.lines');
  const canvas = root.querySelector('canvas');
  const ctx = canvas.getContext('2d');

  const emit = () => onChange(work);
  const colour = (i) => getComputedStyle(root).getPropertyValue(`--ink${i}`).trim() || '#1f2b52';

  // ---- drawing
  function paint(s) {
    const p = s.p;
    if (!p.length) return;
    ctx.strokeStyle = ctx.fillStyle = colour(s.c);
    ctx.lineWidth = s.w;
    ctx.lineCap = ctx.lineJoin = 'round';
    if (p.length <= 2) {
      ctx.beginPath();
      ctx.arc(p[0], p[1], s.w / 2, 0, Math.PI * 2);
      ctx.fill();
      return;
    }
    ctx.beginPath();
    ctx.moveTo(p[0], p[1]);
    for (let i = 2; i < p.length - 2; i += 2) ctx.quadraticCurveTo(p[i], p[i + 1], (p[i] + p[i + 2]) / 2, (p[i + 1] + p[i + 3]) / 2);
    ctx.lineTo(p[p.length - 2], p[p.length - 1]);
    ctx.stroke();
  }
  function redraw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    work.s.forEach(paint);
    if (cur) paint(cur);
  }
  function resize() {
    const r = surface.getBoundingClientRect();
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.max(1, Math.round(r.width * dpr));
    canvas.height = Math.max(1, Math.round(r.height * dpr));
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    redraw();
  }
  new ResizeObserver(resize).observe(surface);
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', redraw);

  const snap = () => {
    hist.push(work.s.slice());
    if (hist.length > 60) hist.shift();
  };
  const point = (e) => {
    const r = canvas.getBoundingClientRect();
    return [Math.round(e.clientX - r.left), Math.round(e.clientY - r.top)];
  };
  const eraseAt = (x, y) => {
    const keep = work.s.filter((s) => {
      for (let i = 0; i < s.p.length; i += 2) if (Math.hypot(s.p[i] - x, s.p[i + 1] - y) < 14) return false;
      return true;
    });
    if (keep.length !== work.s.length) {
      work.s = keep;
      redraw();
    }
  };
  const cancelStroke = () => {
    if (cur || erasing) {
      cur = null;
      erasing = false;
      redraw();
    }
  };

  canvas.addEventListener('pointerdown', (e) => {
    if (work.m !== 'draw') return;
    if (e.pointerType === 'touch') {
      touches.set(e.pointerId, e.clientY);
      if (touches.size >= 2) {
        scrolling = true;
        cancelStroke();
        return;
      }
      if (scrolling) return;
    }
    e.preventDefault();
    try {
      canvas.setPointerCapture(e.pointerId);
    } catch {}
    const [x, y] = point(e);
    if (tool === 'eraser') {
      snap();
      erasing = true;
      eraseAt(x, y);
    } else {
      const w = e.pointerType === 'pen' ? 1.8 + 2.6 * (e.pressure || 0.5) : 2.6;
      cur = { c: color, w: Math.round(w * 10) / 10, p: [x, y] };
      redraw();
    }
  });
  canvas.addEventListener('pointermove', (e) => {
    if (e.pointerType === 'touch' && touches.has(e.pointerId) && scrolling) {
      const dy = e.clientY - touches.get(e.pointerId);
      touches.set(e.pointerId, e.clientY);
      scroller.scrollTop -= dy / Math.max(1, touches.size);
      return;
    }
    if (!cur && !erasing) return;
    const evs = e.getCoalescedEvents ? e.getCoalescedEvents() : [e];
    for (const ev of evs.length ? evs : [e]) {
      const [x, y] = point(ev);
      if (erasing) eraseAt(x, y);
      else cur.p.push(x, y);
    }
    if (cur) redraw();
  });
  const end = (e) => {
    if (e.pointerType === 'touch') {
      touches.delete(e.pointerId);
      if (!touches.size) scrolling = false;
    }
    if (cur) {
      snap();
      work.s = [...work.s, cur];
      cur = null;
      redraw();
      emit();
    } else if (erasing) {
      erasing = false;
      emit();
    }
  };
  canvas.addEventListener('pointerup', end);
  canvas.addEventListener('pointercancel', end);

  // ---- typed lines (MathLive loads on first use)
  const fields = () => [...linesEl.querySelectorAll('math-field')];
  function makeLine(MathfieldElement, latex) {
    const mf = new MathfieldElement();
    mf.value = latex;
    mf.readOnly = work.m !== 'type';
    mf.setAttribute('aria-label', 'Line of working');
    mf.addEventListener('input', () => {
      work.l[fields().indexOf(mf)] = mf.value;
      emit();
    });
    mf.addEventListener('keydown', (e) => {
      const i = fields().indexOf(mf);
      if (e.key === 'Enter') {
        e.preventDefault();
        addAfter(MathfieldElement, i);
      } else if (e.key === 'Backspace' && mf.value === '' && fields().length > 1) {
        e.preventDefault();
        work.l.splice(i, 1);
        const prev = fields()[Math.max(0, i - 1)];
        mf.remove();
        prev?.focus();
        emit();
      }
    });
    return mf;
  }
  function addAfter(MathfieldElement, i) {
    const mf = makeLine(MathfieldElement, '');
    fields()[i].after(mf);
    work.l.splice(i + 1, 0, '');
    setTimeout(() => mf.focus(), 60);
    emit();
  }
  async function build() {
    if (built) return;
    built = true;
    const { MathfieldElement } = await loadMathLive();
    linesEl.replaceChildren(...work.l.map((v) => makeLine(MathfieldElement, v)));
    await customElements.whenDefined('math-field');
    await new Promise((r) => setTimeout(r, 120));
    linesEl.dataset.ready = '1';
  }
  root.querySelector('[data-act="addline"]').addEventListener('click', async () => {
    await build();
    const { MathfieldElement } = await loadMathLive();
    addAfter(MathfieldElement, fields().length - 1);
  });

  // ---- mode, tools
  function setMode(m, focus) {
    work.m = m;
    root.dataset.mode = m;
    root.querySelectorAll('[data-mode-btn]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.modeBtn === m)));
    if (m === 'type') {
      build().then(() => {
        fields().forEach((f) => (f.readOnly = false));
        if (focus) fields().at(-1)?.focus();
      });
    } else {
      fields().forEach((f) => ((f.readOnly = true), f.blur()));
    }
    emit();
  }
  root.querySelectorAll('[data-mode-btn]').forEach((b) => b.addEventListener('click', () => setMode(b.dataset.modeBtn, true)));
  root.querySelectorAll('[data-tool]').forEach((b) =>
    b.addEventListener('click', () => {
      tool = b.dataset.tool;
      root.querySelectorAll('[data-tool]').forEach((x) => x.setAttribute('aria-pressed', String(x === b)));
    }));
  root.querySelectorAll('[data-color]').forEach((b) =>
    b.addEventListener('click', () => {
      color = +b.dataset.color;
      tool = 'pen';
      root.querySelectorAll('[data-tool]').forEach((x) => x.setAttribute('aria-pressed', String(x.dataset.tool === 'pen')));
      root.querySelectorAll('[data-color]').forEach((x) => x.setAttribute('aria-pressed', String(x === b)));
    }));
  root.querySelector('[data-act="undo"]').addEventListener('click', () => {
    if (!hist.length) return;
    work.s = hist.pop();
    redraw();
    emit();
  });
  root.querySelector('[data-act="clear"]').addEventListener('click', () => {
    if (!work.s.length) return;
    snap();
    work.s = [];
    redraw();
    emit();
  });

  if (work.m === 'type' || work.l.some((l) => l)) setMode(work.m, false);
  return root;
}
