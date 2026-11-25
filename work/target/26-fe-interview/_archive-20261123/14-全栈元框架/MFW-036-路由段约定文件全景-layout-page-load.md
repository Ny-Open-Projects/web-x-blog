---
title: [MFW-036] App Router 路由段的约定文件全景：各自职责与渲染顺序？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-036：App Router 路由段的约定文件全景：各自职责与渲染顺序？
**答**：
- 一段路由可包含：`page.tsx`（URL 终点，唯一）、`layout.tsx`（持久壳）、`template.tsx`（每导航重建）、`loading.tsx`（Suspense 骨架）、`error.tsx`（错误边界）、`not-found.tsx`（404）、`route.ts`（API 端点，与 page 互斥）、`default.tsx`（并行路由回退）。
- 渲染包裹顺序（由外到内）：`layout → template → error 边界 → not-found 边界 → loading 边界(Suspense) → page`；loading/error/not-found 实质都是包住 page 的边界。
- `page.tsx` 与 `route.ts` 同段冲突（一个 URL 不能既是页面又是 API）；API 用 Route Handler（GET 可缓存，POST/动态处理变更）。
- 只有 page/route 产生 URL；layout 等纯组合，多层嵌套 layout 逐层包 children。
- 记忆法：**page 定义「有什么」，layout 定义「包什么」，loading/error 定义「坏了怎样」，template 定义「每次重来」**。

```jsx
// app/products/page.tsx —— 渲染顺序示意
// 1. root layout        <html><body><Nav>{...}</Nav></body></html>
// 2. template           每导航重建的动效壳
// 3. error boundary     包住本段
// 4. loading (Suspense) page 挂起时先出骨架
// 5. page               真实内容

export const metadata = { title: '商品' };

export default async function Page() {
  const items = await getProducts();
  return <List items={items} />;
}
```

```jsx
// app/api/products/route.ts —— Route Handler（与 page 互斥）
import { NextResponse } from 'next/server';
import { revalidateTag } from 'next/cache';

export async function GET() {
  const data = await getProducts();
  return NextResponse.json(data); // GET + 静态段可进路由缓存
}

export async function POST(req: Request) {
  const body = await req.json();
  await db.product.create({ data: body });
  revalidateTag('products-list');
  return NextResponse.json({ ok: true }, { status: 201 });
}
```
