---
title: [MFW-145] TanStack Start、RRv7、Next 三者的定位差异？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-145：TanStack Start、RRv7、Next 三者的定位差异？
**答**：
- 一句话定位：Next = RSC 生态主航道的「全家桶」；RRv7 = Remix 血统的「web 标准 + 可控 Vite 栈」；TanStack Start = 「类型安全 + Query 缓存统一」的新锐。
- 数据与缓存：Next 自建缓存体系（四层）；RRv7 loader 即缓存边界（简单但要自己接缓存库）；Start 把 TanStack Query 作为一等公民——缓存、失效、乐观更新复用一套成熟心智，SPA 与 SSR 一致。
- 类型安全：Start > RRv7（typegen）> Next（App Router 类型化较弱，search params 基本裸奔）。
- 渲染模型：Next 有 RSC（服务端组件不出 bundle）；RRv7/Start 全量客户端水合（bundle 更大但模型单一）。
- 部署：Start 与 RRv7 基于 Vite/Nitro 多目标；Next 自托管需 standalone/OpenNext。
- 选型直觉：重类型与缓存一致性、从 SPA 演进来的团队 → Start；Remix 用户与 web 标准癖好 → RRv7；最大生态与招聘面 → Next。

```ts
// 「同一次筛选查询」三框架的缓存心智

// ===== Next：框架缓存栈 =====
// fetch(url, { next: { tags: ['products'], revalidate: 60 } })  // Data Cache

// ===== RRv7：loader + 自己接缓存 =====
// export const loader = () => ({ data: await queryClient.fetchQuery(['products'], () => api.list()) });

// ===== TanStack Start：Query 一等公民 =====
// export const Route = createFileRoute('/products')({
//   loader: () => queryClient.ensureQueryData({ queryKey: ['products'], queryFn: api.list }),
// });
// // useQuery(['products']) 直接命中：SSR prefetch 与客户端缓存同一套
```
