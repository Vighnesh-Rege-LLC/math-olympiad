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

test('problem flow: hints, rating, retire, persistence', async ({ page }) => {
  const errors = watch(page);
  await page.goto('/');
  await expect(page.locator('.statement')).toBeVisible();
  await expect(page.locator('.cue')).toHaveText(/paper/);
  await expect(page.locator('.statement .katex').first()).toBeVisible().catch(() => {});
  const first = await page.locator('.statement').innerText();

  // the card shows no technique or difficulty before hint 2
  await expect(page.locator('.statement a.tlink')).toHaveCount(0);
  await page.locator('[data-hint]').click();
  await expect(page.locator('.step h3').first()).toHaveText('What is being asked');
  await expect(page.locator('.cue')).toHaveCount(0);
  await page.locator('[data-hint]').click();
  await expect(page.locator('.step').nth(1).locator('.chips a').first()).toBeVisible();
  const href = await page.locator('.step').nth(1).locator('.chips a').first().getAttribute('href');
  expect(href).toMatch(/^#\/t\//);

  // reveal everything
  while (await page.locator('[data-hint]').count()) await page.locator('[data-hint]').click();
  await expect(page.locator('.step h3').last()).toHaveText('Full solution');
  await expect(page.locator('[data-rate]')).toHaveCount(3);
  await expect(page.locator('.katex-error')).toHaveCount(0);

  await page.locator('[data-rate="got"]').click();
  await expect(page.locator('.statement')).toBeVisible();
  const second = await page.locator('.statement').innerText();
  expect(second).not.toBe(first);

  // retired problem never returns after reload
  await page.reload();
  const state = await page.evaluate(() => JSON.parse(localStorage.getItem('olympiad-tutor:v1')));
  expect(Object.values(state.p).filter((p) => p.status === 'retired')).toHaveLength(1);
  expect(await page.locator('.statement').innerText()).toBe(second);
  expect(errors).toEqual([]);
});

test('rate without opening the solution; struggled comes back sooner than later', async ({ page }) => {
  const errors = watch(page);
  await page.goto('/');
  await page.locator('[data-done]').click();
  await page.locator('[data-rate="struggled"]').click();
  await page.locator('[data-done]').click();
  await page.locator('[data-rate="later"]').click();
  const s = await page.evaluate(() => JSON.parse(localStorage.getItem('olympiad-tutor:v1')));
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
  expect(errors).toEqual([]);
});

test('every technique page and problem renders (math, links) without errors', async ({ page }) => {
  test.setTimeout(240000);
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
    while (await page.locator('[data-hint]').count()) await page.locator('[data-hint]').click();
    expect(await page.locator('.katex-error').count(), p.id).toBe(0);
    expect(await page.locator('.step').count(), p.id).toBe(p.hints.length + 1);
    for (const href of await page.locator('a.tlink').evaluateAll((as) => as.map((a) => a.getAttribute('href')))) {
      expect(techs.some((t) => href === `#/t/${t.id}`), href).toBe(true);
    }
  }
  expect(errors).toEqual([]);
});

test('works offline after first load; layout fits; dark mode', async ({ page, context, browser }, info) => {
  const errors = watch(page);
  await page.goto('/');
  await page.evaluate(() => navigator.serviceWorker.ready);
  await page.reload(); // now controlled by the service worker
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
  await page.locator('[data-done]').click();
  await page.locator('[data-rate="got"]').click();
  await page.locator('[data-done]').click();
  await page.locator('[data-rate="struggled"]').click();
  await page.getByRole('link', { name: 'History' }).click();
  await expect(page.locator('h1')).toHaveText('History');
  await expect(page.locator('.hist li')).toHaveCount(2);
  await expect(page.getByRole('heading', { name: 'Today' }).or(page.locator('.gh', { hasText: 'Today' }))).toBeVisible();
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
