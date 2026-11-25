---
title: [MFW-051] 动态路由的 generateStaticParams 是怎么决定哪些页面静态化的？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-051：动态路由的 generateStaticParams 是怎么决定哪些页面静态化的？
**答**：
- 它在**构建期**执行，返回的参数组合（如商品 id 列表）会预渲染成静态 HTML；没返回的组合按 `dynamicParams` 决定行为：true（默认）是首次访问时按需 SSR/ISR 再缓存，false 则直接 404。
- 构建期只跑一次，不能在里面读请求级数据（cookies/headers），否则破坏静态化前提。
- 与 getStaticProps 时代相比，它配合 ISR 就是「白名单预生成 + 长尾按需生成」的组合拳，适合商品 SKU 量大但头部商品固定的电商场景。
- 返回值结构要和路由段的动态参数一一对应，嵌套动态段可以逐层返回实现组合。

```tsx
// app/products/[id]/page.tsx
// 构建期预渲染销量 Top 100 的商品，长尾按需生成
export const revalidate = 3600; // ISR：1 小时过期

export async function generateStaticParams() {
  const top100 = await db.product.findMany({
    where: { isHot: true },
    select: { id: true },
  });
  return top100.map((p) => ({ id: p.id })); // [{ id: 'a1' }, ...]
}

// dynamicParams: 'true'（默认）=> 未预渲染的 id 首次访问走 SSR 并入缓存
// 设为 false => 未列出的 id 直接 404，可防止恶意遍历
export const dynamicParams = true;

export default async function ProductPage({
  params,
}: { params: Promise<{ id: string }> }) {
  const { id } = await params; // Next 15 后 params 是 Promise
  const product = await db.product.findUnique({ where: { id } });
  if (!product) notFound();
  return <div>{product.name}</div>;
}
```
