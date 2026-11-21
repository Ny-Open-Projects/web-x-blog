---
title: [R19-166] E2E 测试如何选关键路径？Playwright 与 React 集成的要点是什么？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-166：E2E 测试如何选关键路径？Playwright 与 React 集成的要点是什么？
**答**：
- 关键路径 = "这个页面坏了业务就没法活"的 3-8 条：登录、核心下单流、支付、关键搜索；不要追求全 UI 覆盖（金字塔顶贵且脆）。
- 稳定性三招：`getByRole/getByTestId` 定位器而非 CSS 选择器链、`expect` 自带重试的 web-first 断言、网络等待用 `waitForResponse` 而非 sleep。
- 环境隔离：`webServer` 配置自动起 dev server，`storageState` 复用登录态避免每条用例走登录，MSW 或 route 拦截隔离第三方。
- CI 并行：workers 分片 + trace/screenshot/ video 在失败时保留，定位效率倍增。

```typescript
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  use: {
    baseURL: 'http://localhost:5173',
    trace: 'retain-on-failure',   // 失败保留 trace：时间线+网络+DOM 快照
    screenshot: 'only-on-failure',
  },
  webServer: {                    // CI 自动拉起应用
    command: 'pnpm dev',
    url: 'http://localhost:5173',
    reuseExistingServer: !process.env.CI,
  },
  workers: process.env.CI ? 4 : 2,
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'mobile', use: { ...devices['iPhone 14'] } },
  ],
});

// tests/checkout.spec.ts —— 核心下单流
import { test, expect } from '@playwright/test';

test.use({ storageState: 'tests/.auth/user.json' }); // 复用登录态

test('加购到下单成功', async ({ page }) => {
  await page.goto('/products/1');
  await page.getByRole('button', { name: '加入购物车' }).click();
  await expect(page.getByRole('status')).toContainText('已加入');

  await page.goto('/cart');
  const responsePromise = page.waitForResponse('/api/orders'); // 等网络而非 sleep
  await page.getByRole('button', { name: '提交订单' }).click();
  const res = await responsePromise;
  expect(res.status()).toBe(201);

  await expect(page.getByRole('heading', { name: '下单成功' })).toBeVisible();
});

test('库存不足时提示', async ({ page }) => {
  await page.route('/api/products/2', r =>
    r.fulfill({ json: { id: 2, stock: 0 } }));   // route 拦截造边界数据
  await page.goto('/products/2');
  await expect(page.getByRole('button', { name: '加入购物车' })).toBeDisabled();
});
```
