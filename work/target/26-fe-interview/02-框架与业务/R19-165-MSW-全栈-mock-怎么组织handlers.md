---
title: [R19-165] MSW 全栈 mock 怎么组织？handlers 在开发、测试与 Node 脚本间如何复用？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-165：MSW 全栈 mock 怎么组织？handlers 在开发、测试与 Node 脚本间如何复用？
**答**：
- 组织结构：`mocks/handlers/` 按领域拆（user.ts/order.ts），`handlers.ts` 聚合；一个 handlers 数组同时服务浏览器 worker、Vitest node 环境、Storybook。
- 三环境接入：`mockServiceWorker.js` + `setupWorker`（浏览器 dev 联调）、`setupServer`（单测，beforeAll/afterAll 统一启停）、Node 脚本直接 `server.use`。
- 层级覆盖：默认 handlers 是"正确基线"，单个测试里 `server.use(...)` 覆盖特定场景（错误、慢响应），测试结束 `server.resetHandlers()` 还原。
- 数据工厂：`factory.ts` 提供 `makeUser(overrides)`，让 mock 数据带类型且默认值合理，避免每个测试手写全量字段。

```typescript
// mocks/handlers/user.ts —— 按领域拆分
import { http, HttpResponse, delay } from 'msw';
import { makeUser } from '../factory';

export const userHandlers = [
  http.get('/api/users', async ({ request }) => {
    await delay(100);                                    // 模拟真实延迟
    const q = new URL(request.url).searchParams.get('q') ?? '';
    const list = [makeUser({ name: 'Wang Lei' }), makeUser({ id: 2, name: 'Li Na' })]
      .filter(u => u.name.toLowerCase().includes(q.toLowerCase()));
    return HttpResponse.json({ data: list });
  }),
  http.post('/api/users', async ({ request }) => {
    const body = await request.json();
    if (!body.name) {
      return HttpResponse.json({ message: 'name required' }, { status: 400 });
    }
    return HttpResponse.json({ data: makeUser(body) }, { status: 201 });
  }),
];

// mocks/handlers.ts —— 聚合
import { userHandlers } from './handlers/user';
export const handlers = [...userHandlers];

// mocks/server.ts —— 测试环境（node）
import { setupServer } from 'msw/node';
import { handlers } from './handlers';
export const server = setupServer(...handlers);

// mocks/browser.ts —— 开发环境（浏览器）
import { setupWorker } from 'msw/browser';
export const worker = setupWorker(...handlers);
// main.tsx: if (import.meta.env.DEV && import.meta.env.VITE_USE_MOCK) await worker.start()

// test-setup.ts —— vitest 全局接线
import { server } from './mocks/server';
beforeAll(() => server.listen({ onUnhandledRequest: 'error' })); // 未覆盖的请求直接报错
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

// user-search.test.ts —— 场景级覆盖
import { http, HttpResponse } from 'msw';
it('接口 500 时展示错误', async () => {
  server.use( // 只覆盖本测试，结束自动还原
    http.get('/api/users', () => HttpResponse.json({ message: 'boom' }, { status: 500 })),
  );
  renderWithProviders(<UserSearch />);
  expect(await screen.findByRole('alert')).toBeInTheDocument();
});

// mocks/factory.ts —— 类型化数据工厂
export function makeUser(overrides: Partial<User> = {}): User {
  return { id: 1, name: '张三', email: 'z@acme.com', role: 'admin', ...overrides };
}
```
