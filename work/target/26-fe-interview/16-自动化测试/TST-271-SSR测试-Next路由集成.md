---
title: [TST-271] Next.js 应用的路由级集成测试怎么做（App Router）？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-271：Next.js 应用的路由级集成测试怎么做（App Router）？
**答**：
- 用 next 的测试工具（next/test 或直接起 dev server + fetch）验证路由渲染结果。
- Server Component 输出断言：HTML 含服务端取到的数据（fetch mock 层控制）。
- 路由切换行为：客户端导航后 RSC payload 更新正确（loading.tsx 显示/替换）。
- 错误路由：not-found.tsx / error.tsx 的触发与恢复（retry）断言。

```javascript
test('App Router 页面渲染', async () => {
  mockFetch('/api/goods/1', goodsMock);
  const html = await renderPage('/goods/1');         // dev server or render helper
  expect(html).toContain(goodsMock.title);           // RSC 数据到达
});
r
```
