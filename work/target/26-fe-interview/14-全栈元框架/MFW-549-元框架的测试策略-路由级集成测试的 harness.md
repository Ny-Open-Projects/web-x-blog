---
title: [MFW-549] 元框架测试策略：路由级集成测试的 harness 设计
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-549：路由级集成测试 harness

**答**:
- 元框架路由测试的三层：1) **组件级**（RSC 组件渲染测试——renderToString 对 async 组件的 await 链）；2) **路由级集成**（真实 next dev/build server + Playwright——RSC/流式/水合全链路 RBL-540）；3) **单元 mock 层**（mock fetch/Data Cache——路由逻辑测试不依赖真实后端）。
- harness 的核心组件：1) **测试服务器生命周期**（beforeAll 启动 dev server——端口分配/构建缓存复用 RBL-616 预构建）；2) **数据 fixture**（MSW mock API——SSR fetch 也被 mock（server fetch 走 node fetch——MSW node 拦截）；3) **状态注入**（cookie/session 的测试身份）。
- 流式断言：SSE/流式页面的断言（waitForSelector 分阶段——骨架出现 → 内容到达：流式时序断言 RBL-540 双渲染）。
- 追问钩子：为什么「路由级集成测试」是元框架测试的主力而不是组件单测？——RSC 架构的关键行为都在路由级（缓存语义/流式时序/边界水合/Action 链路）——组件单测测不到这些（async 组件的渲染结果依赖框架运行时）；「测试层级 = 架构价值层」：RSC 的价值主张（流式/缓存）只有在集成层才成立——测试金字塔的形状由架构特性决定（RBL-655 金字塔的元框架特化）。

```javascript
// 路由级 harness（Playwright + MSW）
import { setupServer } from 'msw/node';
const server = setupServer(...handlers);                 // mock API：SSR fetch 拦截
beforeAll(() => { server.listen(); server.use(rest.get('/api/products/:id', mockProduct)); });
// 启动测试 server（复用构建缓存）
test.beforeAll(async () => { await startNextDev({ port: 3001 }); });
test('product page streams', async ({ page }) => {
  await page.goto('/product/42');
  await page.waitForSelector('[data-skeleton]');         // 骨架先现（流式时序）
  await page.waitForSelector('[data-loaded="true"]');    // 数据后到
  const title = await page.textContent('h1');
  expect(title).toBe(mockProduct.name);
});
// Action 链路测试（渐进增强）
test('form works without JS', async ({ browser }) => {
  const ctx = await browser.newContext({ javaScriptEnabled: false });
  const page = await ctx.newPage();
  await page.goto('/order');
  await page.fill('[name=sku]', 'A1');
  await page.click('button[type=submit]');               // 原生提交（RBL-512）
  await page.waitForURL('/orders');
});
```
