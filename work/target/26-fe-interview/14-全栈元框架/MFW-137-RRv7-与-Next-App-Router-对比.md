---
title: [MFW-137] React Router v7 和 Next App Router 的核心差异？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-137：React Router v7 和 Next App Router 的核心差异？
**答**：
- 渲染模型：RRv7 保持**客户端 React 全量水合**（loader 数据序列化下发）；Next 走 **RSC**——服务端组件不进客户端 bundle，交互边界用 'use client' 标注。这是最本质的分叉。
- 数据层：RRv7 显式 loader/action（web 标准心智，POST 到路由）；Next 把取数揉进 RSC、mutation 用 Server Action（函数级 RPC）。
- 心智成本：RRv7 的一切都显式（loader、clientLoader、类型生成、渲染模式开关），可控性强；Next 更多隐式约定（缓存默认值、动态 API 触发），上手快但排查缓存问题要框架内部知识。
- 生态与部署：Next 生态最大但深绑 Vercel；RRv7 自托管简单（Vite 产物 + 任意 Node/Edge），Vite 生态直接可用。
- 团队选型：需要 RSC 级 bundle 优化/团队已深 React Server 生态选 Next；要可控、可迁移、Vite 生态选 RRv7。

```tsx
// 同一页面的两种心智

// ===== Next App Router：取数即组件 =====
// app/products/[id]/page.tsx
export default async function Page({ params }: { params: Promise<{ id: string }> }) {
  const product = await db.product.findUnique({ where: { id: (await params).id } });
  return <h1>{product?.name}</h1>; // 服务端组件，不进客户端 bundle
}

// ===== RRv7：loader 显式分离 =====
// app/routes/product.tsx
export async function loader({ params }: Route.LoaderArgs) {
  return { product: await db.product.findUnique({ where: { id: params.id } }) };
}
export default function Page({ loaderData }: Route.ComponentProps) {
  // 组件全量进 bundle，数据经序列化下发
  return <h1>{loaderData.product.name}</h1>;
}
```
