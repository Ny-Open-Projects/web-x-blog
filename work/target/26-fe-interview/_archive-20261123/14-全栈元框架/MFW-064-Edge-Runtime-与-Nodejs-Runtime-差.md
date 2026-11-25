---
title: [MFW-064] Edge Runtime 和 Node.js Runtime 有什么差异，怎么选？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-064：Edge Runtime 和 Node.js Runtime 有什么差异，怎么选？
**答**：
- Edge Runtime 是类 V8 isolate 的轻量沙箱（如 Cloudflare Workers/Vercel Edge），冷启动毫秒级、按请求就近执行；Node Runtime 是完整 Node 进程，能力全但冷启动慢、必须跑在区域机房。
- Edge 限制：无原生 TCP（`pg` 这类驱动跑不了）、部分 Node API 缺失（fs、crypto 部分子集）、单次执行有 CPU 时间/内存上限、无持久连接池。
- 选型：Middleware、A/B 分流、鉴权转发、重写请求这类「轻计算 + 快响应」放 Edge；需要 DB 长连接、重依赖、文件系统的 Route Handler/Server Action 放 Node。
- 数据库访问的 Edge 方案：HTTP 协议驱动（如 Neon serverless driver、PlanetScale、Prisma Accelerate），本质是把 TCP 换成 fetch。

```ts
// middleware.ts —— 必须跑 Edge（Next 强制），只做轻判断
import { NextRequest, NextResponse } from 'next/server';

export function middleware(req: NextRequest) {
  const country = req.geo?.country ?? 'CN';
  const res = NextResponse.next();
  res.headers.set('x-edge-region', country); // 毫秒级冷启动，适合每请求都跑
  return res;
}
export const config = { matcher: '/products/:path*' };
```

```ts
// app/api/db-query/route.ts —— 重数据访问走 Node runtime
export const runtime = 'nodejs'; // 显式声明，默认即 nodejs
import { Pool } from 'pg';       // TCP 驱动 Edge 上不可用
const pool = new Pool({ connectionString: process.env.DATABASE_URL });

export async function GET() {
  const { rows } = await pool.query('SELECT * FROM products LIMIT 10');
  return Response.json(rows);
}
```
