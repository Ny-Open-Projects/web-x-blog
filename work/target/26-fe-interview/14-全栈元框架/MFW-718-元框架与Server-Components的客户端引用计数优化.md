---
title: [MFW-718] Client 引用计数优化
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-718：Client 引用计数优化

**答**:
- client 引用计数：1) **payload 的 client 引用分析**（Flight payload 的 I[] 引用——每个 client 组件的 chunk 加载次数）；2) **chunk 共享优化**（多个路由引用同一 client 组件 → chunk 共享（CDN 缓存命中——不重复下载）；3) **引用计数与 chunk 分割**（引用计数高的组件 → 独立 chunk（多路由共享——RBL-596 chunk 分割的 RSC 版）；引用低的组件 → 并入路由 chunk（按需加载——不被共享）。
- 引用计数的优化决策：高引用 = chunk 共享（缓存友好）；低引用 = 并入路由（传输少）；「引用计数的动态性」：路由集变化 → 引用计数变 → chunk 分割策略变（构建器自动调整）。
- 追问钩子：为什么「client 引用计数」影响 chunk 分割策略？——高引用组件（Button/Header）被 50 个路由 import → 独立 chunk = CDN 缓存一次下载 50 路由复用；低引用组件（特定页面专用）→ 并入路由 chunk = 一次请求全拿到（无额外 RTT）；「引用计数的经济学」：共享 chunk 的收益 = 引用数 × 缓存节省 − 额外请求成本（RBL-596 chunk 分割决策的 RSC 维度）。

```typescript
// client 引用计数分析
function analyzeClientRefs(routes: Record<string, string[]>) {
  // routes: { '/home': ['Button', 'Header', 'ProductCard'], ... }
  const refCount = new Map<string, number>();
  for (const components of Object.values(routes))
    for (const c of components)
      refCount.set(c, (refCount.get(c) ?? 0) + 1);
  return [...refCount.entries()].map(([name, count]) => ({
    name, count,
    strategy: count >= 5 ? 'shared-chunk' : 'inline-route',
    reason: count >= 5
      ? `${count} 路由引用——独立 chunk 复用 CDN 缓存`
      : '低引用——并入路由 chunk 减少请求',
  })).sort((a, b) => b.count - a.count);
}
// chunk 分割决策
const analysis = analyzeClientRefs({
  '/home': ['Button', 'Header', 'HeroBanner'],
  '/shop': ['Button', 'Header', 'ProductCard', 'FilterBar'],
  '/cart': ['Button', 'Header'],
});
// Button: 3 路由 → shared-chunk（高引用）
// HeroBanner: 1 路由 → inline-route（低引用）
```
