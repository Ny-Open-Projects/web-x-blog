---
title: [MFW-531] SvelteKit 的 load 函数：同构数据管道与序列化边界
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-531：SvelteKit load 函数：同构管道与序列化

**答**:
- load 的双环境语义：**同构**（服务端 load = prerender/SSR；client 导航时 load 也可跑——`+page.js` 同构 / `+page.server.js` 仅服务端）——「server-only 数据（密钥）放 .server.js、通用逻辑放 .js」的边界设计。
- 序列化边界：server load 的返回值自动序列化传给 client（devalue 编码：Date/Map/循环引用支持——devalue 比 JSON 强 RBL-502 的 Svelte 版）；同构 load 在 client 导航时直接执行（无序列化成本）。
- 数据依赖：`await parent()`（布局 load 数据流——嵌套 load 的父子依赖，串行瀑布的显式化）+ 并行段（多个 +page.server.js 同级并行）；「瀑布显式化」让 N+1 数据流可见（可优化）。
- 追问钩子：为什么 SvelteKit 用「文件后缀区分 server/client load」而不是 RSC 的组件标注（'use client'）？——Svelte 的模型是「组件同构、数据层分环境」（load 函数是数据的归属地）；RSC 是「组件级环境标注」（渲染位置决定）——两种边界模型：数据边界（SK）vs 组件边界（RSC）——SK 的 load 模型对「全同构组件 + 少量 server 数据」的应用更直白，RSC 对「深度 server 渲染」表达力更强。

```svelte
// +page.server.js —— 仅服务端（可访问密钥）
export const load = async ({ params, locals }) => {
  const user = await locals.auth();                     // 仅 server
  return { product: await db.products.find(params.id) };// devalue 序列化传 client
};
// +page.js —— 同构（client 导航时也执行）
export const load = async ({ fetch, parent }) => {
  const { product } = await parent();                   // 显式依赖（瀑布可见）
  const reviews = await fetch(`/api/reviews/${product.id}`).then(r => r.json());
  return { reviews };
};
// 序列化边界：devalue 支持 Date/Map/循环
// server load 返回 { createdAt: new Date(), meta: new Map(...) } —— client 收到同类型
```
