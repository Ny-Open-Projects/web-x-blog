---
title: [TST-111] MSW 是什么？为什么说它比 mock axios / adapter 更优雅？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-111：MSW 是什么？为什么说它比 mock axios / adapter 更优雅？
**答**：
- MSW（Mock Service Worker）：用一个注册的 Service Worker 在**网络层**拦截请求，按 handler 返回响应。请求根本到不了 HTTP 栈之外，应用代码毫无感知。
- 相比 mock axios 的优势：① 无侵入——不改业务代码、不依赖 axios 实现，换 fetch/axios/原生请求都一样拦；② 语义真实——应用真的发出请求、真的等待响应、真的走拦截器/取消逻辑；③ 一处定义多处复用——同一份 handlers 在 Jest/Vitest 单测、Storybook、浏览器调试、E2E 里通用。
- 对比 page.route：page.route 拦在浏览器外部（Playwright 工具层），MSW 拦在应用运行时内部——MSW 的 handler 能在 Node（jsdom）环境单测里工作（Node adapter），这是它打通单测/E2E 的关键。
- 工作流：`setupServer(...handlers)` 用于单测（`server.listen/resetHandlers/close` 三件套放 setupFiles/afterEach）；`setupWorker` 用于浏览器调试与 E2E。
- 追问钩子：SSR/Node 端请求怎么拦？——`setupServer` 走 Node 的 http 拦截，同样生效。

```javascript
// src/mocks/handlers.js —— 一处定义
import { http, HttpResponse, delay } from 'msw';
export const handlers = [
  http.get('/api/goods', async ({ request }) => {
    const page = Number(new URL(request.url).searchParams.get('page') ?? 1);
    await delay(100); // 模拟网络延迟，测 loading 态
    return HttpResponse.json({ list: [{ id: page, name: `商品${page}` }] });
  }),
  http.post('/api/cart', ({ request }) => HttpResponse.json({ ok: true })),
];

// 单测 setup（Vitest）
// setupFiles: import { server } from './mocks/server';
// server.listen({ onUnhandledRequest: 'error' })  ← 未匹配请求直接报错，防漏 mock
// afterEach: server.resetHandlers()

test('购物车提交', async () => {
  render(<AddToCart skuId="SKU-001" />);
  await userEvent.click(screen.getByRole('button', { name: '加入购物车' }));
  await screen.findByText('已加入'); // 真实网络语义，应用零侵入
});
```
