---
title: [TST-093] locator 与 elementHandle 有什么区别？为什么推荐 locator？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-093：locator 与 elementHandle 有什么区别？为什么推荐 locator？
**答**：
- 本质区别：locator 是「查找逻辑的描述」（惰性，每次操作重新查 DOM，自动重试）；elementHandle 是「某一刻元素的句柄」（即时求值，DOM 更新后指向已 detach 的旧节点，操作直接报 stale element）。
- 时序安全：SPA 重渲染频繁，handle 拿到后 React 一 diff 元素就换了；locator 每次现查，天然免疫重渲染，这也是 auto-wait 的载体。
- API 面差异：`page.$()` / `page.$eval()` / `elementHandle.click()` 属于旧式即时求值链路；`page.locator()` / `locator.filter()` / `locator.and_()` 属于推荐链路，可组合、可断言、可链式缩小范围（`locator('tr').filter({ hasText: 'iPhone' }).getByRole('button')`）。
- 唯一性保护：`locator.click()` 在命中多个元素时报 strict mode violation，逼你写精确选择器；`page.$()` 静默返回第一个，问题被藏起来。
- 追问钩子：什么时候真的用 handle？——需要传给底层 API（如 `page.exposeFunction` 场景外、拖拽的 DataTransfer、evaluate 里传 DOM 节点）时。

```javascript
test('locator 组合查询：表格行内按钮', async ({ page }) => {
  await page.goto('/orders');

  // 推荐：描述式组合，React 重渲染也不怕
  const row = page.getByRole('row').filter({ hasText: '订单 1001' });
  await row.getByRole('button', { name: '详情' }).click();
  await expect(page.getByText('订单详情')).toBeVisible();

  // 不推荐：handle 即时求值，列表刷新后 handle 失效
  // const stale = await page.$('.order-row');  // 一旦 DOM 更新 → detached
  // await stale.click();                        // 报错

  // 严格模式：命中多行会直接报错，防止点错元素
  // page.getByRole('button', { name: '详情' }).click();
  // → strict mode violation: resolved to 12 elements
});
```
