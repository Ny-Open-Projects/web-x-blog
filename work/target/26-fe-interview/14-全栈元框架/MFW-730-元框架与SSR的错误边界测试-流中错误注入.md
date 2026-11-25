---
title: [MFW-730] 流中错误注入测试
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-730：流中错误注入测试

**答**:
- 流中错误的测试策略：1) **注入错误到特定段**（mock 组件的 fetch 抛错 → 该段 fallback 注入——其他段正常（错误隔离验证 RBL-652）；2) 注入超时（mock fetch 延迟 > timeout → 超时降级验证 RBL-655）；3) 全部失败（所有段失败——页面降级到 error.tsx RBL-536）；4) 「注入的时序」（部分段先成功后段失败——流中部分到达的断言：先到的内容正确显示 + 失败段的 fallback）。
- 测试的实现：MSW 的错误注入（mock handler 按 path 抛错/延迟——RBL-549 harness 的错误版）；「注入的精确性」：只 mock 特定 API（其他 API 正常——错误只影响一个段）。
- 断言的完整性：错误段的 fallback 存在 + 正确段的内容正确 + 错误段的 reset 按钮可点（恢复验证——RBL-536 错误恢复的 E2E）。
- 追问钩子：为什么「流中错误注入」比「单元测试 error boundary」更有价值？——error boundary 的单测只验证「边界渲染 fallback」（React 内部机制）；流中注入验证「错误在整个链路的行为」（server 抛错 → 流中 fallback 注入 → client 显示 → reset 恢复——端到端）；「注入的错误是端到端验证」：mock 错误发生在 server（fetch 层）——测试覆盖 server 错误到 client UI 的完整传播链（RBL-652 的行为验证版）。

```typescript
// 流中错误注入 E2E
test('error isolation in stream', async ({ page }) => {
  // MSW：只 mock reviews API 抛错
  server.use(
    rest.get('/api/reviews/:id', (req, res, ctx) =>
      res.networkError('Mocked network error')),         // 注入错误
    // 其他 API 正常（products 不 mock——正常）
  );
  await page.goto('/product/42');
  // 正确段：内容正常渲染
  await page.waitForSelector('[data-loaded="product"]');
  const title = await page.textContent('h1');
  expect(title).toBe('Test Product');
  // 错误段：fallback 显示
  await page.waitForSelector('[role="alert"]');
  const errorText = await page.textContent('[role="alert"]');
  expect(errorText).toContain('加载失败');
  // reset 恢复（移除错误注入后重试）
  server.use(rest.get('/api/reviews/:id', (req, res, ctx) =>
    res.json({ reviews: [{ text: 'good' }] })));         // 恢复正常
  await page.click('button:has-text("重试")');
  await page.waitForSelector('[data-loaded="reviews"]');
});
// 全部失败：error.tsx 兜底
test('all fail → global error', async ({ page }) => {
  server.use(rest.get('/api/*', (req) => res.networkError('all down')));
  await page.goto('/product/42');
  await page.waitForSelector('[data-global-error]');
});
```
