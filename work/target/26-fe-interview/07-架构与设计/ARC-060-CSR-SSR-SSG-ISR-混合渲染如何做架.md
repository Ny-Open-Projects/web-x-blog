---
title: [ARC-060] CSR/SSR/SSG/ISR 混合渲染如何做架构决策？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-060：CSR/SSR/SSG/ISR 混合渲染如何做架构决策？
**答**：
- 按页面特性选模式：营销/文档页 SSG（最快、最稳）、内容会后台更新的页面 ISR（静态 + 定时再生）、强个性化/实时页面 SSR、纯工具后台 CSR。
- 混合渲染的关键是"按路由声明模式"，一个应用内不同路由走不同渲染管线。
- 决策依据三问：内容时效性、个性化程度、SEO/首屏要求。

```typescript
// Next.js：按路由声明渲染模式的架构
// app/(marketing)/layout.tsx —— SSG：构建期生成，内容变更随发布
// app/(marketing)/page.tsx
export const dynamic = 'force-static';

// app/blog/[slug]/page.tsx —— ISR：静态 + 每 60s 后台再生
export const revalidate = 60;

// app/dashboard/page.tsx —— CSR：强个性化，不 SEO
'use client';
export default function Dashboard() { /* 全客户端渲染 */ }

// app/feed/page.tsx —— SSR：每请求实时渲染
export const dynamic = 'force-dynamic';
// 决策矩阵：
// SSG：内容低频变 + SEO 必需     ISR：内容分钟级变 + SEO 必需
// SSR：内容实时变/强个性化       CSR：内部工具、SEO 无关、重交互
```
