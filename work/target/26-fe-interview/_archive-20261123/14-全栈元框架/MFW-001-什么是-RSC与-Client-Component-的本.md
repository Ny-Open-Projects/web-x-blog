---
title: [MFW-001] 什么是 RSC？它与 Client Component 的本质区别是什么？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-001：什么是 RSC？它与 Client Component 的本质区别是什么？
**答**：
- RSC（React Server Component）是**只在服务端执行、不打包进客户端 JS bundle** 的组件：可以直接访问数据库/文件系统/密钥，返回的是可序列化的「RSC Payload」（描述 UI 的结构化数据），不是 HTML DOM。
- Client Component 是传统的 SSR + hydration 组件：服务端渲染首屏 HTML，客户端下载 JS 后「复活」交互能力（事件、state、effect）。
- 本质区别一句话：**RSC 从不进入客户端运行时，Client Component 要经历 hydration**。所以 RSC 的代码体积为 0、永远不需要更新，Client Component 才有 bundle 成本。
- 两者通过 props 通信：只能传**可序列化数据**或 **Client Component 引用**（作为 children 传下去），不能传函数（除非是 Server Action）。
- 追问钩子：RSC 不是 SSR——SSR 是「渲染成 HTML 的技术」，RSC 是「组件运行位置」的架构，两者可以组合使用。

```jsx
// app/products/page.tsx —— Server Component（默认）
import { db } from '@/lib/db';
import ProductCard from './product-card'; // Client Component

export default async function Page() {
  // 直接查库：没有 API 层、没有暴露密钥、0 行客户端 JS
  const products = await db.product.findMany({ take: 20 });
  return (
    <section>
      <h1>商品列表</h1>
      {products.map((p) => (
        // 传给 Client Component 的是纯数据（可序列化），不能传回调函数
        <ProductCard key={p.id} product={p} />
      ))}
    </section>
  );
}
```

```jsx
// app/products/product-card.tsx
'use client'; // 边界声明：从这里开始是客户端组件

import { useState } from 'react';

export default function ProductCard({ product }) {
  const [liked, setLiked] = useState(false); // 交互能力只有 client 有
  return (
    <div onClick={() => setLiked(!liked)}>
      <h2>{product.title}</h2>
      <span>{liked ? '❤️' : '🤍'}</span>
    </div>
  );
}
```
