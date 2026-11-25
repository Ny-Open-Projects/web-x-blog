---
title: [TST-278] 选择性水合时「用户提前交互」的行为测试？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-278：选择性水合时「用户提前交互」的行为测试？
**答**：
- 水合前点击：事件在水合完成后重放或被捕获（React 的选择性水合行为）——断言最终状态一致。
- 断言无「点击丢失」：交互意图不因未水合而消失（或显式提示）。
- 性能配合：交互优先水合该区域（而非全页）——打点验证水合顺序。
- 极端场景：水合中导航走（卸载）——无报错无泄漏。

```javascript
test('水合前点击不丢失', async ({ page }) => {
  await page.goto('/slow-hydrate');
  await page.getByRole('button', { name: '加购' }).click();   // 未水合完成即点
  await page.waitForSelector('[data-hydrated="true"]');
  await expect(page.getByTestId('cart-badge')).toHaveText('1'); // 意图保留
});
r
```
