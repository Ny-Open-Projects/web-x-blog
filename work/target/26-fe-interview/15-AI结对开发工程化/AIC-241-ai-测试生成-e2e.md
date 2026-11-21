---
title: [AIC-241] 让 AI 生成 Playwright E2E 用例，与单测生成相比要多给哪些上下文？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-241：让 AI 生成 Playwright E2E 用例，与单测生成相比要多给哪些上下文？
**答**：
- 页面真实结构与可访问性快照（aria snapshot）——AI 没见过真实 DOM 会臆造 selector。
- 用户旅程描述（who/why/前后置条件），AI 才能选对关键路径而非随机点击。
- 环境约束：认证方式（storageState）、测试账号、数据准备与清理策略。
- 要求用 getByRole/getByLabel 语义定位，禁止脆弱的 CSS 选择器与固定 sleep。

```javascript
test('商品下单主流程', async ({ page }) => {
  await page.goto('/goods/1001');
  await page.getByRole('button', { name: '加入购物车' }).click();
  await expect(page.getByTestId('cart-badge')).toHaveText('1');
  await page.getByRole('link', { name: '去结算' }).click();
  await page.getByRole('button', { name: '提交订单' }).click();
  await expect(page.getByText('支付成功')).toBeVisible({ timeout: 10_000 }); // 轮询而非 sleep
});
r
```
