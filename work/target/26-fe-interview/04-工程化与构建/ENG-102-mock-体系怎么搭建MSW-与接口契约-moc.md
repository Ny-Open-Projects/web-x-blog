---
title: [ENG-102] mock 体系怎么搭建？MSW 与接口契约 mock 的优势在哪？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-102：mock 体系怎么搭建？MSW 与接口契约 mock 的优势在哪？
**答**：
- MSW 用 Service Worker/Node 拦截器在网络层 mock，组件代码无感知；单测与 Storybook 可复用同一套 handlers。
- 按 API 契约（OpenAPI/类型定义）编写 handlers，mock 即文档；接口变了 TS 类型先报错。
- onUnhandledRequest: 'error' 让漏 mock 的请求直接暴露，避免"mock 掉了不知道"的假绿测试。
- 边界场景（错误码、超时、空数据）用 server.use 临时覆盖 handlers，测异常路径。

```typescript
// src/mocks/handlers.ts：MSW 按接口契约编写的 mock 层
import { http, HttpResponse } from 'msw';
import { setupServer } from 'msw/node';

export const server = setupServer(
  http.get('/api/user/:id', ({ params }) =>
    HttpResponse.json({ id: params.id, name: '张三', role: 'admin' })
  ),
  http.post('/api/login', async ({ request }) => {
    const body = await request.json();
    if (!body?.password) {
      return HttpResponse.json({ msg: '密码必填' }, { status: 400 });
    }
    return HttpResponse.json({ token: 'mock-token' });
  })
);

// 测试基建中统一启停
// beforeAll(() => server.listen({ onUnhandledRequest: 'error' }));
// afterEach(() => server.resetHandlers());
// afterAll(() => server.close());
```
