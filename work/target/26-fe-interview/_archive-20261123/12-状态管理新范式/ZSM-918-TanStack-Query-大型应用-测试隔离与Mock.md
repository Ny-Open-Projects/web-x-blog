---
title: [918] TanStack Query 在测试里怎么隔离与 mock
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, TanStack Query, 测试]
type: 面试题
---

## 918：TanStack Query 在测试里怎么隔离与 mock

**答**：
- 测试三原则：每用例新建 QueryClient（防缓存串扰——单例是测试大忌）、msw 拦网络（mock 在网络层而非 mock queryFn——queryFn 真实执行测真实链路）、渲染包 Provider（测试 client + 禁 retry 加速用例）。
- 竞态用例：模拟慢响应 A + 快响应 B——msw 延迟控制，断言最终渲染 B；乐观更新回滚用例（mock 失败断言缓存还原）。
- 缓存行为断言：getQueryState 断言状态机（fetching/success/stale）——测「失效后是否 refetch」用 fetch 计数 spy 而非盲等。
- 追问钩子：为什么不 mock 掉 useQuery？——mock 掉测不到缓存/竞态/重试这些「库的行为」，测试价值归零；mock 网络层保留库行为是被测对象的正确边界。

```ts
const makeWrapper = () => {
  const qc = new QueryClient({ defaultOptions: {
    queries: { retry: false }, mutations: { retry: false } } });
  return ({ children }) => (
    <QueryClientProvider client={qc}>{children}</QueryClientProvider>);
};
// msw: http.get('/api/user/1', () => HttpResponse.json(mockUser))
```

