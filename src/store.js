const KEY = 'olympiad-tutor:v1';

const fresh = () => ({ v: 1, seq: 0, level: 3.5, knob: 1, p: {}, t: {}, cur: null, cue: true });

let mem = null;

export function load() {
  try {
    const s = JSON.parse(localStorage.getItem(KEY));
    if (s && s.v === 1) return (mem = s);
  } catch {}
  return (mem = mem || fresh());
}

export function save(s) {
  mem = s;
  try {
    localStorage.setItem(KEY, JSON.stringify(s));
  } catch {}
}
