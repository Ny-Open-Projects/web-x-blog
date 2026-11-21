---
title: [MFW-127] RRv7 的 loader 和 route module 是怎么工作的？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-127：RRv7 的 loader 和 route module 是怎么工作的？
**答**：
- route module = 一个路由文件同时导出：`loader`（取数，服务端+客户端导航都跑）、`action`（mutation，POST 到该路由）、`clientLoader`（客户端独占取数）、默认导出组件、`ErrorBoundary`、`HydrateFallback`（首屏水合前占位）。
- loader 时序：SSR 时服务端先跑完所有匹配 loader 再渲染 HTML；客户端导航时 router 先并行发起所有 loader（`useLoaderData` 挂起）再切换 UI——「数据就绪才导航」的 Remix 心智。
- `clientLoader` + `serverLoader` 组合：私密数据走 serverLoader，客户端增强（localStorage、实时库）走 clientLoader，`HydrateFallback` 控制水合期占位。
- 与 Next 对比：Next 把取数隐进组件（RSC），RRv7 显式分离 loader 与组件；RRv7 的 loader 返回值自动序列化下发（json），组件用 `useLoaderData` 类型安全消费。

```tsx
// app/routes/product.tsx —— 一个文件就是一个 route module
import type { RouteComponentProps } from 'react-router';

export async function loader({ params }: { params: { id: string } }) {
  const product = await db.product.findUnique({ where: { id: params.id } });
  if (!product) throw new Response('Not Found', { status: 404 });
  return { product };
}

// 客户端增强：服务端结果 + 浏览器实时库存
export async function clientLoader({ serverLoader, params }: any) {
  const { product } = await serverLoader();        // 复用服务端数据
  const liveStock = await stockSocket.get(params.id); // 客户端实时数据
  return { product, liveStock };
}

export default function Product({ loaderData }: any) {
  const { product, liveStock } = loaderData; // 类型由 typegen 自动生成
  return <h1>{product.name} · 库存 {liveStock}</h1>;
}

export function ErrorBoundary({ error }: any) {
  const status = error?.status ?? 500;
  return <h1>{status === 404 ? '商品不存在' : '出错了'}</h1>;
}

export function HydrateFallback() { return <p>加载中…</p>; }
```
