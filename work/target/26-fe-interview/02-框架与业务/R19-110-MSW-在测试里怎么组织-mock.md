---
title: [R19-110] MSW 在测试里怎么组织 mock？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-110：MSW 在测试里怎么组织 mock？
**答**：
- MSW 拦截网络层而非模块层：组件代码完全不改，单测、Storybook、E2E 复用同一套 handlers。
- handlers 按资源组织成数组，setupServer 注册；用例级 override 用 server.use，afterEach resetHandlers。
- listen 时开 `onUnhandledRequest: 'error'`，漏 mock 的请求直接报错而不是静默放行。
- 可以在 handler 里读 request、返回动态响应，覆盖错误码、慢响应等异常分支。

```typescript
// msw/handlers.ts —— 拦截网络层，单测 / Storybook / E2E 共用一套
import { http, HttpResponse } from 'msw';

export const handlers = [
  http.get('/api/users/:id', ({ params }) =>
    HttpResponse.json({ id: params.id, name: 'Wang' })),
  http.post('/api/users', async ({ request }) => {
    const body = await request.json();
    if (!body.name) return HttpResponse.json({ message: 'name required' }, { status: 400 });
    return HttpResponse.json({ id: 1, ...body }, { status: 201 });
  }),
];

// test/setup.ts
import { setupServer } from 'msw/node';
import { handlers } from './msw/handlers';

export const server = setupServer(...handlers);

beforeAll(() => server.listen({ onUnhandledRequest: 'error' }));  // 漏 mock 直接报错
afterEach(() => server.resetHandlers());   // 用例级覆写的 handler 用后重置
afterAll(() => server.close());
```
