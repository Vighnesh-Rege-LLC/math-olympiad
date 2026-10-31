// Assemble dist/: app sources, KaTeX (local), merged data.json, service worker.
import { cpSync, mkdirSync, readFileSync, readdirSync, rmSync, writeFileSync, statSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { join, relative } from 'node:path';

const out = 'dist';
rmSync(out, { recursive: true, force: true });
mkdirSync(join(out, 'katex/fonts'), { recursive: true });

cpSync('src', out, { recursive: true, filter: (p) => !p.endsWith('sw.template.js') });
const kd = 'node_modules/katex/dist';
cpSync(join(kd, 'katex.min.js'), join(out, 'katex/katex.min.js'));
let css = readFileSync(join(kd, 'katex.min.css'), 'utf8');
// keep only woff2 sources; every supported browser takes the first one anyway
css = css.replace(/,url\(fonts\/[^)]+\.woff\) format\("woff"\),url\(fonts\/[^)]+\.ttf\) format\("truetype"\)/g, '');
writeFileSync(join(out, 'katex/katex.min.css'), css);
for (const f of readdirSync(join(kd, 'fonts'))) if (f.endsWith('.woff2')) cpSync(join(kd, 'fonts', f), join(out, 'katex/fonts', f));

mkdirSync(join(out, 'fonts'), { recursive: true });
for (const [pkg, files] of Object.entries({
  newsreader: ['400-normal', '400-italic', '600-normal'],
  caveat: ['600-normal', '700-normal'],
  inter: ['500-normal', '600-normal', '700-normal'],
})) for (const f of files) cpSync(`node_modules/@fontsource/${pkg}/files/${pkg}-latin-${f}.woff2`, join(out, `fonts/${pkg}-${f}.woff2`));

const techniques = JSON.parse(readFileSync('data/techniques.json', 'utf8'));
const problems = JSON.parse(readFileSync('data/problems.json', 'utf8'));
writeFileSync(join(out, 'data.json'), JSON.stringify({ techniques, problems }));

const files = [];
(function walk(d) {
  for (const f of readdirSync(d)) {
    const p = join(d, f);
    statSync(p).isDirectory() ? walk(p) : files.push('/' + relative(out, p));
  }
})(out);
const hash = createHash('sha1');
for (const f of files.sort()) hash.update(readFileSync(join(out, f)));
const version = hash.digest('hex').slice(0, 10);
const sw = readFileSync('src/sw.template.js', 'utf8')
  .replace('__VERSION__', version)
  .replace('__FILES__', JSON.stringify(['/', ...files]));
writeFileSync(join(out, 'sw.js'), sw);
console.log(`built ${problems.length} problems, ${techniques.length} techniques, ${files.length} files, v${version}`);
