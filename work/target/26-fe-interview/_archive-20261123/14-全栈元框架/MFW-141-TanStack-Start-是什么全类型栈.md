---
title: [MFW-141] TanStack Start 是什么？它凭什么和 Next/RRv7 竞争？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-141：TanStack Start 是什么？它凭什么和 Next/RRv7 竞争？
**答**：
- TanStack Start 是 TanStack 团队的全栈框架：**TanStack Router（类型安全路由）+ SSR + server functions**，构建层基于 Vite 与 Nitro（部署多目标）——可以理解为「类型安全版的 Remix」。
- 三大卖点：① 全链路端到端类型安全（路由、search params、loader 数据、server function 入参出参）；② 文件路由 + 代码化路由双支持，router 是独立可用库；③ 与 TanStack Query 无缝集成（缓存/失效心智统一）。
- 与 RRv7 的区别：类型推导深度（search params 校验内建 zod 风格 schema）、Query 集成；与 Next 区别：没有 RSC，保持客户端 React 心智 + 显式 server functions。
- 定位判断：TS 重度团队、重视路由类型与 Query 缓存的 SPA→SSR 渐进项目；生态成熟度与岗位数量目前不如 Next/RRv7，选型要看团队。

```ts
// app/routes/products.$id.tsx —— TanStack Start 文件路由
import { createFileRoute } from '@tanstack/react-router';
import { getProduct } from '../../server/products';

export const Route = createFileRoute('/products/$id')({
  // search params 带校验：非法 query 直接 400，且类型自动推导
  validateSearch: z.object({
    tab: z.enum(['overview', 'reviews']).default('overview'),
    page: z.coerce.number().min(1).default(1),
  }),
  loader: ({ params }) => getProduct({ data: params.id }), // server function 调用
  component: ProductPage,
});

function ProductPage() {
  const { id } = Route.useParams();
  const { tab, page } = Route.useSearch(); // { tab: 'overview'|'reviews', page: number }
  const product = Route.useLoaderData();
  return <h1>{product.name} · {tab} · {page}</h1>;
}
```
