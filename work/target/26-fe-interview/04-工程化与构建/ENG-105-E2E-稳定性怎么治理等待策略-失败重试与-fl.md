---
title: [ENG-105] E2E 稳定性怎么治理？等待策略、失败重试与 flaky 隔离？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-105：E2E 稳定性怎么治理？等待策略、失败重试与 flaky 隔离？
**答**：
- 等待策略：用 Playwright locator 的自动等待与 expect().toBeVisible()，禁止硬编码 sleep（慢且仍偶发）。
- flaky 治理流程：CI 开 retries 记录重试成功率，连续失败的用例 quarantine（跳过+开 issue 修复），不让它持续污染主干。
- 隔离原则：用例之间不共享状态（每个用例独立 seed 数据），fullyParallel + workers 并行且互不干扰。
- 失败留证：trace retain-on-failure，事后用 playwright show-trace 完整回放，代替"猜"。

```typescript
// playwright.config.ts：稳定性核心配置
export default defineConfig({
  retries: process.env.CI ? 2 : 0,      // CI 重试两次并记录 flaky
  workers: 4,
  fullyParallel: true,                   // 并行隔离，用例间不共享状态
  trace: 'retain-on-failure',            // 失败留完整 trace 供回放
  reporter: [['html'], ['junit', { outputFile: 'e2e-results.xml' }]],
});

test('下单流程', async ({ page }) => {
  await page.goto('/products');
  await page.getByRole('button', { name: '加入购物车' }).click();  // locator 自动等待
  await expect(page.getByText('已加入购物车')).toBeVisible();      // 断言自带轮询
});
```

---

## 第二十三章 Monorepo 深化（ENG-106 ~ ENG-111）
