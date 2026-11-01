import { test, expect } from '@playwright/test';
import { readFileSync } from 'node:fs';

const data = JSON.parse(readFileSync('data/problems.json', 'utf8'));
const techs = JSON.parse(readFileSync('data/techniques.json', 'utf8'));

function watch(page) {
  const errors = [];
  page.on('console', (m) => m.type() === 'error' && errors.push(m.text()));
  page.on('pageerror', (e) => errors.push(String(e)));
  return errors;
}
const stored = (page) => page.evaluate(() => JSON.parse(localStorage.getItem('olympiad-tutor:v1')));
const currentWork = async (page) => {
  const s = await stored(page);
  return s?.w?.[s.cur.id];
};
const openHints = async (page) => {
  if (await page.locator('.hintpop').isHidden()) await page.locator('[data-act="hint"]').click();
  await expect(page.locator('.hintpop')).toBeVisible();
};
const rate = async (page, key) => {
  await page.locator('[data-act="done"]').click();
  await page.locator(`.donemenu [data-rate="${key}"]`).click();
};
async function stroke(page, dx = 90, dy = 50) {
  const box = await page.locator('canvas.ink').boundingBox();
  await page.mouse.move(box.x + 30, box.y + 30);
  await page.mouse.down();
  await page.mouse.move(box.x + 30 + dx / 2, box.y + 30 + dy, { steps: 4 });
  await page.mouse.move(box.x + 30 + dx, box.y + 30, { steps: 4 });
  await page.mouse.up();
}

test('problem flow: hints overlay, rating, retire, persistence', async ({ page }) => {
  const errors = watch(page);
  await page.goto('/');
  await expect(page.locator('.statement')).toBeVisible();
  await expect(page.locator('.cue')).toHaveText(/paper/);
  const first = await page.locator('.statement').innerText();

  // nothing about technique or difficulty before the hints
  await expect(page.locator('.statement a')).toHaveCount(0);
  await page.locator('[data-act="hint"]').click();
  await expect(page.locator('.hintpop .step h3').first()).toHaveText('What is being asked');
  await expect(page.locator('.cue')).toHaveCount(0);
  await expect(page.locator('.hintpop .count')).toContainText('1 of');
  await page.locator('[data-more]').click();
  await expect(page.locator('.hintpop .step').nth(1).locator('.chips a').first()).toBeVisible();
  const href = await page.locator('.hintpop .step').nth(1).locator('.chips a').first().getAttribute('href');
  expect(href).toMatch(/^#\/t\//);

  // reveal everything, close by tapping the bulb again
  while (await page.locator('[data-more]').isVisible()) await page.locator('[data-more]').click();
  await expect(page.locator('.hintpop .step h3').last()).toHaveText('Full solution');
  await expect(page.locator('.katex-error')).toHaveCount(0);
  await page.locator('[data-act="hint"]').click();
  await expect(page.locator('.hintpop')).toBeHidden();

  await page.locator('[data-act="done"]').click();
  await expect(page.locator('.donemenu [data-rate]')).toHaveCount(3);
  await page.locator('.donemenu [data-rate="got"]').click();
  await expect(page.locator('.statement')).toBeVisible();
  const second = await page.locator('.statement').innerText();
  expect(second).not.toBe(first);

  await page.reload();
  const state = await stored(page);
  expect(Object.values(state.p).filter((p) => p.status === 'retired')).toHaveLength(1);
  expect(await page.locator('.statement').innerText()).toBe(second);
  expect(errors).toEqual([]);
});

test('overlays close when anything outside them is tapped; one at a time', async ({ page }) => {
  const errors = watch(page);
  await page.goto('/');
  await page.locator('[data-act="hint"]').click();
  await expect(page.locator('.hintpop')).toBeVisible();
  await page.locator('.scrim').click({ position: { x: 20, y: 500 } });
  await expect(page.locator('.hintpop')).toBeHidden();

  await page.locator('[data-act="done"]').click();
  await expect(page.locator('.donemenu')).toBeVisible();
  await page.locator('[data-act="hint"]').click(); // opening another closes the first
  await expect(page.locator('.donemenu')).toBeHidden();
  await expect(page.locator('.hintpop')).toBeVisible();
  await page.keyboard.press('Escape');
  await expect(page.locator('.hintpop')).toBeHidden();

  await page.locator('[data-knob]').click();
  await expect(page.locator('.dialpop')).toBeVisible();
  await page.locator('.scrim').click({ position: { x: 20, y: 500 } });
  await expect(page.locator('.dialpop')).toHaveCount(0);
  expect(errors).toEqual([]);
});

test('rate without opening the hints; struggled comes back sooner than later', async ({ page }) => {
  const errors = watch(page);
  await page.goto('/');
  await rate(page, 'struggled');
  await expect(page.locator('.statement')).toBeVisible();
  await rate(page, 'later');
  const s = await stored(page);
  const [a, b] = Object.values(s.p);
  expect(a.status).toBe('struggled');
  expect(b.status).toBe('later');
  expect(a.due - 1).toBeLessThan(b.due - 2);
  expect(errors).toEqual([]);
});

test('techniques: list, page, stepped examples, links, back', async ({ page }) => {
  const errors = watch(page);
  await page.goto('/');
  await page.getByRole('link', { name: 'Techniques' }).click();
  await expect(page.locator('.tile')).toHaveCount(techs.length);
  await expect(page.locator('.ring')).toHaveCount(0); // hidden until 5 problems seen
  await page.getByRole('link', { name: 'Pigeonhole' }).click();
  await expect(page.locator('h1')).toHaveText('Pigeonhole principle');
  const ex = page.locator('.ex').first();
  await expect(ex.locator('li')).toHaveCount(0);
  await ex.locator('[data-next]').click();
  await expect(ex.locator('li')).toHaveCount(1);
  while (await ex.locator('[data-next]').count()) await ex.locator('[data-next]').click();
  await expect(ex.locator('li').last()).toBeVisible();
  await page.locator('.chips a').first().click();
  await expect(page.locator('h1')).not.toHaveText('Pigeonhole principle');
  await page.locator('.back').click();
  await expect(page.locator('h1')).toHaveText('Pigeonhole principle');
  await page.locator('.back').click();
  await expect(page.locator('h1')).toHaveText('Techniques');
  expect(errors).toEqual([]);
});

test('mastery appears after 5 problems on a technique; retired shows on its page', async ({ page }) => {
  const errors = watch(page);
  const ids = data.filter((p) => p.techniques.includes('modular-arithmetic')).slice(0, 5).map((p) => p.id);
  expect(ids.length).toBe(5);
  await page.addInitScript((ids) => {
    if (localStorage.getItem('olympiad-tutor:v1')) return;
    const p = Object.fromEntries(ids.map((id, i) => [id, { seen: 1, status: i < 3 ? 'retired' : 'struggled', due: i < 3 ? null : 99 }]));
    localStorage.setItem('olympiad-tutor:v1', JSON.stringify({ v: 1, seq: 5, level: 3, p, t: { 'modular-arithmetic': { skill: 0.7, seen: ids, last: 4 } }, cur: null, cue: false }));
  }, ids);
  await page.goto('/#/techniques');
  await expect(page.locator('.ring')).toHaveCount(1);
  await page.getByRole('link', { name: 'Modular arithmetic' }).click();
  await expect(page.locator('.hist li')).toHaveCount(5);
  await expect(page.locator('.st.retired')).toHaveCount(3);
  await page.locator('.hist a').first().click();
  await expect(page.locator('.statement')).toBeVisible();
  await expect(page.locator('[data-rate]')).toHaveCount(0);
  await expect(page.locator('[data-act="done"]')).toHaveCount(0);
  expect(errors).toEqual([]);
});

test('every technique page and problem renders (math, links) without errors', async ({ page }) => {
  test.setTimeout(300000);
  const errors = watch(page);
  await page.goto('/');
  for (const t of techs) {
    await page.goto(`/#/t/${t.id}`);
    await expect(page.locator('h1')).toHaveText(t.name);
    for (const b of await page.locator('[data-next]').all()) while (await b.isVisible().catch(() => false)) await b.click();
    expect(await page.locator('.katex-error').count(), t.id).toBe(0);
    expect(await page.locator('.sec a.tlink, .chips a').count(), t.id).toBeGreaterThan(0);
  }
  for (const p of data) {
    await page.goto(`/#/p/${p.id}`);
    await page.locator('[data-act="hint"]').click();
    while (await page.locator('[data-more]').isVisible()) await page.locator('[data-more]').click();
    expect(await page.locator('.katex-error').count(), p.id).toBe(0);
    expect(await page.locator('.hintpop .step').count(), p.id).toBe(p.hints.length + 1);
    for (const href of await page.locator('.hintpop a').evaluateAll((as) => as.map((a) => a.getAttribute('href')))) {
      expect(techs.some((t) => href === `#/t/${t.id}`), href).toBe(true);
    }
  }
  expect(errors).toEqual([]);
});

test('works offline after first load; layout fits; dark mode', async ({ page, context }) => {
  const errors = watch(page);
  await page.goto('/');
  await page.evaluate(() => navigator.serviceWorker.ready);
  await page.reload();
  await context.setOffline(true);
  await page.reload();
  await expect(page.locator('.statement')).toBeVisible();
  await page.getByRole('link', { name: 'Techniques' }).click();
  await expect(page.locator('.tile').first()).toBeVisible();
  await context.setOffline(false);
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth);
  expect(overflow).toBe(false);
  await page.emulateMedia({ colorScheme: 'dark' });
  const bg = await page.evaluate(() => getComputedStyle(document.body).backgroundColor);
  expect(bg).toBe('rgb(20, 22, 31)');
  expect(errors).toEqual([]);
});

test('difficulty dial: named levels, persists, shifts the next problem', async ({ page }) => {
  const errors = watch(page);
  await page.addInitScript(() => {
    if (!localStorage.getItem('olympiad-tutor:v1')) localStorage.setItem('olympiad-tutor:v1', JSON.stringify({ v: 1, seq: 0, level: 3.5, knob: 3, p: {}, t: {}, cur: null, cue: false }));
  });
  await page.goto('/');
  await expect(page.locator('.statement')).toBeVisible();
  const id = await page.evaluate(() => JSON.parse(localStorage.getItem('olympiad-tutor:v1')).cur.id);
  expect(data.find((p) => p.id === id).difficulty).toBeGreaterThanOrEqual(6);
  const pill = page.locator('[data-knob]');
  await expect(pill).toHaveText('Olympiad');
  await pill.click();
  await expect(page.locator('.dialpop [role=radio]')).toHaveText(['Warm-up', 'Adaptive', 'Challenging', 'Olympiad']);
  await page.locator('.dialpop [role=radio]').first().click();
  await expect(pill).toHaveText('Warm-up');
  await expect(page.locator('.dialpop')).toHaveCount(0);
  expect(await page.evaluate(() => JSON.parse(localStorage.getItem('olympiad-tutor:v1')).knob)).toBe(0);
  await page.reload();
  await expect(page.locator('[data-knob]')).toHaveText('Warm-up');
  expect(errors).toEqual([]);
});

test('history: lists rated problems, filters, opens a problem, back', async ({ page }) => {
  const errors = watch(page);
  await page.goto('/');
  await rate(page, 'got');
  await expect(page.locator('.statement')).toBeVisible();
  await rate(page, 'struggled');
  await page.getByRole('link', { name: 'History' }).click();
  await expect(page.locator('h1')).toHaveText('History');
  await expect(page.locator('.hist li')).toHaveCount(2);
  await expect(page.locator('.gh', { hasText: 'Today' })).toBeVisible();
  await page.locator('[data-filter="retired"]').click();
  await expect(page.locator('.hist li')).toHaveCount(1);
  await page.locator('[data-filter="back"]').click();
  await expect(page.locator('.hist li .st.struggled')).toHaveCount(1);
  await page.locator('.hist a').first().click();
  await expect(page.locator('.statement')).toBeVisible();
  await page.locator('.back').click();
  await expect(page.locator('h1')).toHaveText('History');
  await page.locator('.back').click();
  await expect(page.locator('[data-knob]')).toBeVisible();
  expect(errors).toEqual([]);
});

test('working area: draw, undo, clear, type math, persists across reload', async ({ page }) => {
  const errors = watch(page);
  await page.goto('/');
  await expect(page.locator('canvas.ink')).toBeVisible();

  await stroke(page);
  await expect.poll(async () => (await currentWork(page))?.s.length).toBe(1);
  await page.getByRole('button', { name: 'Undo' }).click();
  await expect.poll(async () => (await currentWork(page))?.s.length).toBe(0);
  await stroke(page);
  await page.getByRole('button', { name: 'Clear pad' }).click();
  await expect.poll(async () => (await currentWork(page))?.s.length).toBe(0);
  await stroke(page, 120, 40);
  await expect.poll(async () => (await currentWork(page))?.s.length).toBe(1);

  await page.locator('[data-mode-btn="type"]').click();
  await expect(page.locator('.lines[data-ready]')).toHaveCount(1);
  const first = page.locator('math-field').first();
  await expect(first).toBeVisible();
  await first.evaluate((el) => el.focus());
  await page.waitForFunction(() => document.querySelector('math-field').shadowRoot?.activeElement);
  await page.keyboard.type('x^2+1');
  await expect.poll(async () => (await currentWork(page))?.l[0]).toContain('x^2');
  await page.keyboard.press('Enter');
  await expect(page.locator('math-field')).toHaveCount(2);
  await page.waitForFunction(() => document.querySelectorAll('math-field')[1]?.shadowRoot?.activeElement);
  await page.keyboard.type('y');
  await expect.poll(async () => (await currentWork(page))?.l).toEqual(expect.arrayContaining([expect.stringContaining('x^2')]));

  await page.reload();
  await expect(page.locator('math-field')).toHaveCount(2);
  const w = await currentWork(page);
  expect(w.s).toHaveLength(1);
  expect(w.m).toBe('type');
  expect(errors.filter((e) => !/virtual keyboard|ResizeObserver/i.test(e))).toEqual([]);
});

test('pad fills the space under the toolbar and the question compacts when the pad scrolls', async ({ page }) => {
  const errors = watch(page);
  await page.goto('/');
  const sc = page.locator('.scroller');
  await expect(sc).toBeVisible();
  const vh = page.viewportSize().height;
  const box = await sc.boundingBox();
  const tabs = await page.locator('#tabs').boundingBox();
  expect(box.y + box.height).toBeGreaterThan(tabs.y - 40); // pad runs down to the tab bar
  expect(box.height).toBeGreaterThan(vh * 0.28);

  const q = page.locator('.qwrap');
  await expect(q).toHaveAttribute('data-state', 'full');
  const before = (await q.boundingBox()).height;
  await sc.evaluate((el) => (el.scrollTop = 200));
  await expect(q).toHaveAttribute('data-state', 'compact');
  await expect.poll(async () => (await q.boundingBox()).height).toBeLessThan(80);
  await expect.poll(async () => (await sc.boundingBox()).height).toBeGreaterThan(box.height - 1);
  await sc.evaluate((el) => (el.scrollTop = 0));
  await expect(q).toHaveAttribute('data-state', 'full');
  await expect.poll(async () => (await q.boundingBox()).height).toBeGreaterThanOrEqual(before - 1);
  expect(errors).toEqual([]);
});

test('two fingers scroll the pad and do not draw; one finger draws', async ({ page }) => {
  const errors = watch(page);
  await page.goto('/');
  await expect(page.locator('canvas.ink')).toBeVisible();
  const result = await page.evaluate(() => {
    const canvas = document.querySelector('canvas.ink');
    const sc = document.querySelector('.scroller');
    const r = canvas.getBoundingClientRect();
    const ev = (type, id, x, y) =>
      canvas.dispatchEvent(new PointerEvent(type, { pointerId: id, pointerType: 'touch', clientX: x, clientY: y, bubbles: true, isPrimary: id === 1 }));
    const x = r.left + 80;
    const y = r.top + 120;
    ev('pointerdown', 1, x, y);
    ev('pointerdown', 2, x + 40, y);
    ev('pointermove', 1, x, y - 60);
    ev('pointermove', 2, x + 40, y - 60);
    ev('pointerup', 1, x, y - 60);
    ev('pointerup', 2, x + 40, y - 60);
    const scrolled = sc.scrollTop;
    // now one finger
    ev('pointerdown', 3, x, y);
    ev('pointermove', 3, x + 30, y + 20);
    ev('pointermove', 3, x + 60, y);
    ev('pointerup', 3, x + 60, y);
    return { scrolled };
  });
  expect(result.scrolled).toBeGreaterThan(20);
  await expect.poll(async () => (await currentWork(page))?.s.length).toBe(1);
  expect(errors).toEqual([]);
});

test('typing works offline after the first visit', async ({ page, context }) => {
  const errors = watch(page);
  await page.goto('/');
  await page.evaluate(() => navigator.serviceWorker.ready);
  await page.reload();
  await context.setOffline(true);
  await page.reload();
  await page.locator('[data-mode-btn="type"]').click();
  await expect(page.locator('.lines[data-ready]')).toHaveCount(1);
  const f = page.locator('math-field').first();
  await expect(f).toBeVisible();
  await f.evaluate((el) => el.focus());
  await page.waitForFunction(() => document.querySelector('math-field').shadowRoot?.activeElement);
  await page.keyboard.type('a+b');
  await expect.poll(async () => (await currentWork(page))?.l[0]).toContain('a+b');
  await context.setOffline(false);
  expect(errors.filter((e) => !/virtual keyboard|ResizeObserver/i.test(e))).toEqual([]);
});
