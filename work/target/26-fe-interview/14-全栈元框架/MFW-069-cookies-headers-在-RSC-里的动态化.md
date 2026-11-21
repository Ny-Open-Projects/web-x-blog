---
title: [MFW-069] 为什么在 Server Component 里读 cookies 会把页面变动态？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-069：为什么在 Server Component 里读 cookies 会把页面变动态？
**答**：
- Full Route Cache 的前提是「渲染结果与请求无关」。`cookies()` / `headers()` / `searchParams` 是请求级数据，一旦读取就等于声明这棵子树/页面**每次请求都可能不同**，框架自动 opt-out 出静态缓存（并触发动态渲染）。
- 这是 Next 的「动态 API 自动切换」设计：开发者不必手动声明 dynamic，读了动态 API 即动态；反过来说，不慎在深层组件里读了一次 cookie，整页静态化就没了，是「静态页面悄悄变慢」的经典病因。
- 应对：把请求级数据收敛到叶子节点并配合 Suspense 分层，让静态壳（PPR 思路）先出，动态洞单独流式；或者把 cookie 改为中间件注入的轻量 header + 拆分缓存。
- Next 15 后这些 API 都是 async（`await cookies()`），读法本身也要注意同步调用会报错。

```tsx
// app/dashboard/page.tsx
import { Suspense } from 'react';

// 静态部分：不碰任何动态 API
function StaticNav() { return <nav>公共导航</nav>; }

// 动态部分：只在叶子读 cookies，配 Suspense 包住
async function UserGreeting() {
  const cookieStore = await cookies();          // 读取即动态
  const name = cookieStore.get('nickname')?.value ?? '游客';
  return <p>你好，{name}</p>;
}

export default function Dashboard() {
  return (
    <>
      <StaticNav />                    {/* 静态，可缓存 */}
      <Suspense fallback={<p>加载中…</p>}>
        <UserGreeting />               {/* 动态洞单独流式，不拖累整页 */}
      </Suspense>
    </>
  );
}
```
