---
title: [R19-111] Playwright 与 React 项目集成有哪些要点？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-111：Playwright 与 React 项目集成有哪些要点？
**答**：
- 配置 webServer 让 Playwright 自动起本地服务，CI 上可复现，本地 reuseExistingServer 复用 dev server。
- 元素锚定优先 getByRole/getByLabel，data-testid 作为最后兜底；选择器要与 RTL 用同一套语义。
- 登录态复用：登录一次后 storageState 存 cookie/localStorage，后续用例免重复登录，提速明显。
- 断言用 web-first 的 expect.toHaveURL/toContainText，自带重试，不要 sleep。

```typescript
// playwright.config.ts —— webServer 自动起本地服务，CI 可复现
import { defineConfig } from '@playwright/test';

export default defineConfig({
  webServer: { command: 'npm run dev', port: 3000, reuseExistingServer: true },
  use: { baseURL: 'http://localhost:3000' },
});

// e2e/login.spec.ts —— 与 RTL 同一套语义选择器
import { test, expect } from '@playwright/test';

test('登录后进入工作台', async ({ page }) => {
  await page.goto('/login');
  await page.getByTestId('username-input').fill('wang');
  await page.getByTestId('password-input').fill('secret');
  await page.getByRole('button', { name: '登录' }).click();

  await expect(page).toHaveURL(/dashboard/);            // web-first 断言自带重试
  await expect(page.getByTestId('welcome')).toContainText('wang');
});

// 登录态复用：storageState 存 cookie，后续用例免重复登录
test.use({ storageState: 'e2e/.auth/state.json' });
```
