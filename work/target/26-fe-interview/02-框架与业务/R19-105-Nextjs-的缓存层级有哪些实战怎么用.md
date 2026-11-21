---
title: [R19-105] Next.js 的缓存层级有哪些？实战怎么用？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-105：Next.js 的缓存层级有哪些？实战怎么用？
**答**：
- 四层：请求记忆（同一次渲染内相同 fetch 去重）、数据缓存（fetch 结果跨请求复用）、全路由缓存（构建期静态化整段 HTML/RSC payload）、路由缓存（客户端 RSC payload 的内存缓存）。
- 数据层按需声明：`next.revalidate` 走 ISR、`no-store` 实时、`tags` 供按标签失效。
- 写操作后主动失效：Server Action 里 revalidateTag 清数据缓存、revalidatePath 清整段路由。
- 路由缓存默认 30s 生命周期，router.refresh() 可强制刷新客户端缓存。

```tsx
// app/page.tsx —— 缓存层级实战
export const revalidate = 60;                 // 段级：全路由缓存 60s 重新生成

export default async function Page() {
  // 数据缓存：相同 URL 的 fetch 在有效期内复用
  const res = await fetch('https://api.example.com/data', {
    next: { revalidate: 60, tags: ['data'] },  // ISR + 按标签失效
  });

  // 需要实时的数据用 no-store，逐请求获取
  const user = await fetch('/api/me', { cache: 'no-store' });

  return <div>{/* 渲染数据 */}</div>;
}

// 写操作后的主动失效
import { revalidateTag, revalidatePath } from 'next/cache';

export async function updateData() {
  'use server';
  await saveData();
  revalidateTag('data');        // 只失效打了该标签的数据缓存
  revalidatePath('/page');      // 同时让整段路由缓存失效
}
```
