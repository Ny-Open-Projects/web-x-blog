---
title: [TST-112] MSW 怎么模拟异常、延迟、分页等复杂场景？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-112：MSW 怎么模拟异常、延迟、分页等复杂场景？
**答**：
- 状态化 mock：handler 里读请求参数（path params、query、body）动态返回——分页按 `page` 算、搜索按 `q` 过滤，mock 有了「行为」而不只是「固定 JSON」。更复杂的状态用模块级 store（Map）存会话状态，POST 写入 GET 读出，模拟真后端。
- 异常场景：`HttpResponse.json({msg}, { status: 500 })`、`HttpResponse.error()`（网络层失败）、`await delay(3000)` 慢接口、`http.post(..., () => new HttpResponse(null, { status: 429 }))` 限流。
- 按用例覆盖 handler：`server.use(...)` 临时插队（LIFO），`once` handler 只生效一次；afterEach 里 `server.resetHandlers()` 恢复——实现「全局兜底 + 用例特化」。
- 场景化 handler 分层：把「成功态、空态、错误态」封装成 handler 工厂（`goodsListHandlers({ mode: 'error' })`），用例一行开启场景，避免每个用例手写 `server.use`。
- 追问钩子：怎么断言「前端发的请求参数对不对」？——MSW 的 `server.events.on('request:end')` 记录请求，或 handler 内把 body 存到数组，用例里 `expect(captured[0]).toEqual({...})`。

```javascript
import { http, HttpResponse, delay } from 'msw';

// 状态化：模拟一个 mini 后端
const db = { orders: new Map() };
export const orderHandlers = [
  http.post('/api/orders', async ({ request }) => {
    const body = await request.json();
    const id = `ORD-${Date.now()}`;
    db.orders.set(id, body);
    return HttpResponse.json({ id }, { status: 201 });
  }),
  http.get('/api/orders/:id', ({ params }) => {
    const order = db.orders.get(params.id);
    if (!order) return HttpResponse.json({ msg: 'not found' }, { status: 404 });
    return HttpResponse.json(order);
  }),
  http.get('/api/goods', async () => {
    await delay(2000);                       // 慢接口 → 测 loading
    return HttpResponse.error();             // 或：网络失败 → 测重试
  }),
];

// 用例内特化：只 mock 一次失败
test('下单失败重试', async () => {
  server.use(http.post('/api/orders', () => HttpResponse.json({}, { status: 500 }), { once: true }));
  // ... 第一次失败，第二次走全局成功 handler
});
```
