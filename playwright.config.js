import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: 'tests',
  fullyParallel: true,
  expect: { timeout: 15000 },
  reporter: 'list',
  webServer: { command: 'node build.mjs && node scripts/serve.mjs', url: 'http://localhost:4173', reuseExistingServer: false },
  use: { baseURL: 'http://localhost:4173' },
  projects: [
    { name: 'desktop', use: { ...devices['Desktop Chrome'] } },
    { name: 'touch', use: { ...devices['Pixel 7'] } },
  ],
});
