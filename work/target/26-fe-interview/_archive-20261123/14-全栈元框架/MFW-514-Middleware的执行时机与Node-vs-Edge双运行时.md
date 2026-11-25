---
title: [MFW-514] Middleware 执行时机与 Node/Edge 双运行时的选型矩阵
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-514：Middleware 执行时机与 Node/Edge 双运行时选型

**答**:
- Middleware 的执行时机：**每次请求最前**（匹配后、渲染前）——能做的：重写/重定向/加 header/鉴权短路/AB 分流（RBL-888 的网关版）；不能做的：重 IO（无 DB 直连的 Edge 限制 RBL-267）、长计算（CPU 时间限制）。
- 双运行时选型矩阵：Edge（冷启动毫秒级/无 Node API/全球分布——轻路由决策）vs Node（全 API/冷启动重——重逻辑）；Next 15 的 Node middleware 缓解（streaming 权衡）——「middleware 保持轻、重活进 route handler」的分层。
- Middleware 的错误面：middleware 抛错 = 500 全站（最前层无兜底）——middleware 的防御性编程（try 包裹降级放行）比 route 更严格；「middleware 挂 = 全站挂」是它的风险特征。
- 追问钩子：为什么 middleware 默认跑 Edge？——middleware 的语义是「每请求的轻量路由决策」——全球边缘执行让决策离用户最近（鉴权重定向 RTT 最小）；Node 版冷启动重（每请求开销）——「每请求 × 轻计算」的场景恰好是 Edge 的甜蜜点；选型的本质是「执行频率 × 单次成本」的乘积优化。

```javascript
// middleware.ts —— 每请求最前执行
import { NextResponse } from 'next/server';
export function middleware(req) {
  const { pathname } = req.nextUrl;
  // 1) 鉴权短路（轻）
  const session = req.cookies.get('session');
  if (pathname.startsWith('/admin') && !session) {
    return NextResponse.redirect(new URL('/login', req.url));
  }
  // 2) 灰度分流（RBL-888 网关版）
  const bucket = hash(req.headers.get('x-user-id') ?? '') % 100;
  const res = NextResponse.next();
  res.headers.set('x-gray', bucket < 10 ? 'new' : 'old');
  // 3) 重活绝不在这做 —— 转 route handler
  return res;
}
export const config = { matcher: ['/((?!_next|favicon).*)'] };
// 防御性：middleware 抛错 = 全站 500
export function middleware(req) {
  try { return logic(req); }
  catch { return NextResponse.next(); }                  // 降级放行而非 500
}
```
