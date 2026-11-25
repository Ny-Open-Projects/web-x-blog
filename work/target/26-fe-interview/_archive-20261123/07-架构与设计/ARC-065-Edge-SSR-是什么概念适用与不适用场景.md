---
title: [ARC-065] Edge SSR 是什么概念？适用与不适用场景？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-065：Edge SSR 是什么概念？适用与不适用场景？
**答**：
- Edge SSR：渲染逻辑跑在离用户最近的边缘节点（CDN 边缘运行时），省去回源机房的网络延迟，TTFB 显著下降。
- 约束：边缘运行时不是完整 Node（无长连接池/文件系统，CPU/内存受限），依赖需边缘兼容（如 fetch-based 的 client）。
- 适用：全球分发、个性化轻逻辑（鉴权/A-B 分流/地域内容）；不适合重计算、直连内网数据库的渲染。

```typescript
// Next.js Middleware（跑在 Edge 运行时）：个性化在边缘完成，零回源
// middleware.ts
import { NextRequest, NextResponse } from 'next/server';

export const config = { runtime: 'edge', matcher: ['/', '/mall/:path*'] };

export function middleware(req: NextRequest) {
  const country = req.geo?.country ?? 'US';               // 边缘内置地理信息
  const bucket = abTest(req, 'new-checkout', [50, 50]);   // 边缘分流
  const res = NextResponse.rewrite(
    new URL(`/${country.toLowerCase()}/mall${req.nextUrl.pathname}?exp=${bucket}`, req.url),
  );
  res.cookies.set('exp', bucket, { maxAge: 86400 });
  return res;
}
// 页面本体仍是 SSR，但鉴权/分流/地域改写在边缘完成，TTFB 从 ~400ms 降到 ~50ms
```
