---
title: [MFW-023] ISR（增量静态再生）的机制是什么？和 SSR 怎么权衡？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-023：ISR（增量静态再生）的机制是什么？和 SSR 怎么权衡？
**答**：
- ISR = 静态页 + `revalidate`：首次请求回缓存的 HTML；revalidate 过期后，**下一个请求触发后台再生成**（该请求仍返回旧 HTML），新 HTML 写入 Full Route Cache——准实时、却享受静态性能。
- 适用：内容更新频率可容忍窗口延迟的页面（文章、商品详情、榜单）；不适合每请求都要实时的（购物车、余额）。
- 权衡要点：SSR 每请求渲染（CPU 成本高但实时）；ISR 命中缓存近乎 CDN 成本（毫秒级，可上 CDN s-maxage），代价是 N 秒数据延迟 + 后台渲染成本。
- on-demand ISR（revalidatePath/Tag）可以补足窗口期：事件驱动失效，把延迟降到接近 0，通常是最优组合。
- 追问：fallback 的 `generateStaticParams` 策略——构建期只生成热门页，长尾页首次访问时再生成（blocking fallback）。

```jsx
// app/product/[id]/page.tsx
import { revalidateTag } from 'next/cache';

// 构建期只预渲染 Top 100，长尾页运行期生成（blocking）
export async function generateStaticParams() {
  const top = await db.product.findMany({ orderBy: { sales: 'desc' }, take: 100 });
  return top.map((p) => ({ id: p.id }));
}

export const revalidate = 3600; // 1h 后台再生

export default async function ProductPage({ params }) {
  const product = await getProduct(params.id); // fetch 带 tag，写操作时 revalidateTag 即时失效
  return <h1>{product.title} ¥{product.price}</h1>;
}
```
