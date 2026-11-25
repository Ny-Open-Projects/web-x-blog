---
title: [ZSM-705] E2E 测试的状态断言层：为什么断言 store 比断言 DOM 更稳
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-705：E2E 测试的状态断言层：为什么断言 store 比断言 DOM 更稳

**答**：
- DOM 断言的脆弱性：文案改一个字、样式类名重构、虚拟滚动让元素不在可视区——断言就挂，但这些不是业务 bug。**状态断言**（store 内容）只挂业务真错。最佳实践是双层断言：关键业务结果断 store（`__stores.cart.getState().total === 4333`），关键 UX 断 DOM（按钮 disabled、toast 可见）。
- 接线方式（回顾 ZSM-567）：dev/test 构建暴露 `window.__stores`；`page.evaluate(() => __stores.cart.getState())`。框架路由（React Router/Next）不影响——状态断言绕过 UI 层。
- 等待状态而非等待元素：`waitFor(() => expect(evaluate('getState().phase')).toBe('done'))`——比 `waitForSelector` 稳定（phase 是数据事实，DOM 渲染可能有延迟/虚拟化）。
- 分层策略：E2E 少而精（关键链路：登录→下单→支付），状态断言下沉到**集成测试层**（jsdom + 真实 store + mock API，不启动浏览器）——90% 的状态逻辑用集成测，E2E 只验「拼装正确」。
- 追问钩子：状态断言的反面风险——绕过 UI 意味着「UI 没把状态正确渲染」测不到，所以 UX 关键点仍要 DOM 断言；两层不是替代关系是互补。

```javascript
// 双层断言的 Playwright 测试
test('下单链路：状态与 UX 双断言', async ({ page }) => {
  await page.goto('/checkout')
  await page.click('#pay')

  // 状态层：业务事实
  await page.waitForFunction(() => __stores.checkout.getState().phase === 'done')
  const order = await page.evaluate(() => __stores.checkout.getState().order)
  expect(order.total).toBe(4333)

  // UX 层：关键渲染结果
  await expect(page.locator('.toast--success')).toBeVisible()
  await expect(page).toHaveURL(new RegExp(`/orders/${order.id}`))
})

// 等待状态（比 waitForSelector 稳）
async function waitForState(page, predicate, timeout = 5000) {
  const ok = await page.waitForFunction((fn) => {
    return eval(fn)(window.__stores)
  }, String(predicate), { timeout })
  return ok
}

// 集成测试层（jsdom，不启浏览器）：状态逻辑主力
test('结算校验逻辑', () => {
  const store = createCheckoutStore()
  store.getState().addItem({ price: 1000, qty: 2 })
  store.getState().applyCoupon({ type: 'flat', amount: 500, threshold: 1000 })
  expect(store.getState().total).toBe(1500)   // 纯状态断言，无需渲染
})
```
