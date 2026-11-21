---
title: [NODE-302] Node 22 的 AbortSignal 在 SSR 数据层的应用？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-302：Node 22 的 AbortSignal 在 SSR 数据层的应用？
**答**:
- SSR 数据预取与请求生命周期绑定：客户端断开/超时 → signal abort → 所有在途下游请求取消——SSR 内存（在途请求缓冲）立刻释放。
- 组合：页面预算（timeout 2s）+ 请求取消（req close）+ 组件级预算（慢块独立 timeout，Suspense 分段）三层 signal 嵌套。
- Next.js 的 request abort：request.signal 内建——loader 里必须传给 fetch（很多泄漏就是没传）。
- 验证：压测中拔连接（aborted connections）观察下游 QPS 是否同步下降（没有则取消链断了）。

```javascript
// 三层 signal 嵌套
export default async function Page({ request }: { request: Request }) {
  const pageBudget = AbortSignal.any([
    request.signal,                             // 1) 客户端断开
    AbortSignal.timeout(2000),                  // 2) 页面预算
  ]);
  const [hot, rec, user] = await Promise.allSettled([
    fetch('/api/hot', { signal: pageBudget }),
    fetch('/api/rec', { signal: AbortSignal.any([pageBudget, AbortSignal.timeout(800)]) }),  // 3) 慢块独立预算
    fetch('/api/user', { signal: pageBudget }),
  ]);
}
// 验证：autocannon --connections 中途断开 → 下游 mock 服务 QPS 应同步回落
```
