---
title: [TST-233] 跨浏览器渲染差异（字体/抗锯齿）如何不淹没真实回归？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-233：跨浏览器渲染差异（字体/抗锯齿）如何不淹没真实回归？
**答**：
- 分浏览器维护基线（snapshot 后缀自动区分），不跨浏览器比像素。
- 浏览器间只比「DOM 结构与关键元素可见性」（语义断言），像素只同浏览器比。
- 字体渲染差异大的环境（Linux 无字体）统一装字体包，从源头减少差异。
- 矩阵精简：像素级视觉只跑 Chromium（代表主流），其他浏览器跑语义断言。

```javascript
test('跨浏览器语义一致', async ({ page }) => {
  await page.goto('/price');
  // 语义断言：结构存在与可见，不做像素比较
  await expect(page.getByTestId('price-main')).toBeVisible();
  await expect(page.getByTestId('price-main')).toHaveText(/^¥\d+/);
});
r
```
