---
title: [TST-092] Playwright 的自动等待（auto-waiting）机制是怎么工作的？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-092：Playwright 的自动等待（auto-waiting）机制是怎么工作的？
**答**：
- 结论：actionability 检查——每次 locator 操作前，Playwright 在协议层持续检查元素是否满足四件事：Visible（非 display:none/visibility:hidden/零尺寸）、Stable（连续两帧位置不变，动画结束）、Enabled（非 disabled）、Receives Events（不被遮挡，命中测试打到自己或子元素）。
- 等待实现：不是 sleep，而是浏览器侧的轮询循环（requestAnimationFrame 级别），条件满足立即执行，默认 30s 超时抛 TimeoutError，错误信息直接告诉你卡在哪一步（如 "element is not visible"）。
- locator 是惰性的：`page.getByRole(...)` 不查找元素，只是描述，每次操作时重新解析 DOM——所以自动重试、不怕元素重渲染，这是它比 elementHandle（一次性快照，元素换掉就 stale）强的根本原因。
- 网络侧：`waitForResponse` / `waitForURL` / `expect(...).toBeVisible()` 同样是条件等待；只有 `waitForTimeout` 是死等，面试要明确说它是反模式、仅用于无法观测的动画兜底。
- 追问钩子：数据未加载就断言怎么办？——`expect(locator).toBeVisible()` 内部会重试，天然覆盖异步渲染，不需要手写 waitFor。

```javascript
test('auto-wait 全链路演示', async ({ page }) => {
  await page.goto('/login');
  // 点击前自动等：可见 + 动画结束 + 未被 loading 遮罩盖住
  await page.getByLabel('用户名').fill('admin');
  await page.getByRole('button', { name: '登录' }).click(); // actionability 检查

  // 反应式断言：轮询重试直到出现或超时，不用 sleep
  await expect(page.getByText('欢迎回来')).toBeVisible({ timeout: 5000 });

  // 网络条件等待：等特定响应而不是等 UI（更稳）
  const goodsResp = page.waitForResponse('**/api/goods?page=1');
  await page.getByRole('link', { name: '商品' }).click();
  await goodsResp;
});
```
