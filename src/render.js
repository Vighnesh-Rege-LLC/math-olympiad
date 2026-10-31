// Tiny markdown + KaTeX renderer for the data file's text.
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

export function rich(text, names) {
  const math = [];
  let s = text.replace(/\$\$([\s\S]+?)\$\$|\$([^$\n]+?)\$/g, (m, d, i) => {
    math.push({ src: d ?? i, display: d != null });
    return `\u0000${math.length - 1}\u0000`;
  });
  s = esc(s).replace(/\[\[([a-z-]+)(?:\|([^\]]*))?\]\]/g, (m, id, label) =>
    `<a class="tlink" href="#/t/${id}">${label || names?.[id] || id}</a>`);

  const inline = (x) => x.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>').replace(/(^|[^*\w])\*([^*\s][^*]*?)\*(?!\w)/g, '$1<em>$2</em>');

  const out = [];
  let para = [];
  let list = null;
  const flushPara = () => {
    if (para.length) out.push(`<p>${inline(para.join(' '))}</p>`);
    para = [];
  };
  const flushList = () => {
    if (list) out.push(`<${list.tag}>${list.items.map((i) => `<li>${inline(i)}</li>`).join('')}</${list.tag}>`);
    list = null;
  };
  const lines = s.split('\n');
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    let m;
    if (!line.trim()) {
      flushPara();
      flushList();
    } else if (line.startsWith('|')) {
      flushPara();
      flushList();
      const rows = [];
      while (i < lines.length && lines[i].startsWith('|')) rows.push(lines[i++]);
      i--;
      const cells = (r) => r.replace(/^\||\|$/g, '').split('|').map((c) => c.trim());
      const body = rows.filter((r) => !/^\|[\s|:-]+\|$/.test(r));
      out.push(`<div class="tablewrap"><table>${body.map((r, k) => `<tr>${cells(r).map((c) => `<${k ? 'td' : 'th'}>${inline(c)}</${k ? 'td' : 'th'}>`).join('')}</tr>`).join('')}</table></div>`);
    } else if ((m = line.match(/^- (.*)/))) {
      flushPara();
      if (list?.tag !== 'ul') {
        flushList();
        list = { tag: 'ul', items: [] };
      }
      list.items.push(m[1]);
    } else if ((m = line.match(/^\d+\. (.*)/))) {
      flushPara();
      if (list?.tag !== 'ol') {
        flushList();
        list = { tag: 'ol', items: [] };
      }
      list.items.push(m[1]);
    } else if (list && /^\s+/.test(line)) {
      list.items[list.items.length - 1] += ' ' + line.trim();
    } else {
      flushList();
      para.push(line.trim());
    }
  }
  flushPara();
  flushList();

  return out.join('').replace(/\u0000(\d+)\u0000/g, (m, n) => {
    const { src, display } = math[+n];
    try {
      return window.katex.renderToString(src, { displayMode: display, throwOnError: false, strict: 'ignore' });
    } catch {
      return esc(src);
    }
  });
}
