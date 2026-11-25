---
title: [MFW-761] RSC 的边缘渲染适配
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-761：RSC 的边缘渲染适配

**答**:
- RSC 在 Edge 的适配约束（RBL-787 + RBL-517 的 RSC 版）：1) **RSC 渲染的依赖**（React SSR 的 renderToReadableStream——edge 运行时的 React SSR 支持（Vercel Edge 支持 React SSR——Cloudflare Workers 的 React SSR 需要适配）；2) **数据层限制**（无 TCP 连接池——RBL-517 HTTP driver；3) **Node API 禁用**（fs/crypto 完整——RSC 组件中的 Node API 引用 = 部署失败 RBL-787 审计）；4) **runtime 选择**（`export const runtime = 'edge'`——Next 的边缘渲染声明）。
- RSC 边缘渲染的组件约束：server 组件不能用 Node API（fs/path——edge 环境无）；可用 Web API（fetch/crypto.subtle/URL——Web 标准 RBL-735）；「组件的 runtime 兼容性」：per-route 的 runtime 声明（某些路由 edge、某些 node——混合部署 RBL-575）。
- 追问钩子：为什么「RSC 在 Edge」的适配比「传统 SSR」更复杂？——传统 SSR = 整个 app 在同一 runtime（统一适配）；RSC = server 组件分散在树中（每个组件的 runtime 兼容性独立检查——一个组件用 fs = 整路由不可 edge）；「per-component 的 runtime 约束」：RSC 的组件级数据获取使 runtime 约束分散到每个组件（审计粒度更细 RBL-787 的 RSC 版）——混合部署（某些路由 edge、某些 node）的产物策略。

```typescript
// app/products/page.tsx —— edge 渲染
export const runtime = 'edge';
export default async function Page() {
  // ✅ Web API：fetch/crypto.subtle/URL
  const data = await fetch('https://api.example.com/products');   // fetch OK
  const hash = await crypto.subtle.digest('SHA-256', new TextEncoder().encode('x'));   // Web Crypto
  // ❌ Node API：fs/path/process.binding → edge 不支持
  // const fs = await import('fs');  ← 构建失败（RBL-787 审计）
  return <div>{JSON.stringify(await data.json())}</div>;
}
// app/admin/page.tsx —— node 渲染（fs 可用）
export const runtime = 'nodejs';
import fs from 'fs';                                     // node runtime 可以
// 混合部署：per-route runtime——RBL-575 区域感知 + RBL-787 API 审计
```
