---
title: [908] TanStack Query 的 SSR 水合在大型应用怎么做
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, TanStack Query, SSR]
type: 面试题
---

## 908：TanStack Query 的 SSR 水合在大型应用怎么做

**答**：
- 标准流程：服务端 loader 里 ensureQueryData（预取）-> dehydrate 序列化缓存 -> HTML 注入 -> 客户端 hydrate——水合后首屏直接命中缓存零请求。
- 大型应用的坑：dehydrate 全量缓存体积爆炸——用 shouldDehydrateQuery 过滤（只水合首屏关键 query）；水合数据的新鲜度——dehydrate 带 updatedAt，客户端 staleTime 判断是否立即 refetch。
- 双渲染一致性：SSR 与 CSR 的 queryFn 必须同一实现（抽到共享层）且 Key 一致——不一致导致水合后立即 refetch（数据闪变）或错配。
- 追问钩子：为什么水合后还会 refetch？——staleTime 默认 0：水合数据立即过期；SSR 场景全局默认 staleTime 必须显式设置（>0），否则水合优化等于没做。

```ts
// server: loader 预取 + 注入
await qc.ensureQueryData({ queryKey: userKeys.detail(id), queryFn });
const state = dehydrate(qc, { shouldDehydrateQuery: q =>
  q.queryKey[0] === 'user' });                   // 只水合首屏域
// client: 入口水合
const qc = new QueryClient({ defaultOptions: { queries: { staleTime: 60_000 } } });
hydrate(qc, window.__QUERY_STATE__);
```

