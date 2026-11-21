---
title: [MFW-042] 怎么用 Middleware 做灰度发布 / A-B 测试（含会话一致性）？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-042：怎么用 Middleware 做灰度发布 / A-B 测试（含会话一致性）？
**答**：
- 核心机制：middleware 按**分桶规则**（user id hash / cookie / geo / UA）决定流量去向，用 `NextResponse.rewrite` 把请求改写到 `/beta` 版本——**浏览器 URL 不变**，用户无感。
- 会话一致性是关键：分桶结果必须**写进 cookie 固化**，否则同一次会话刷新页面可能跳桶（实验数据被污染）。
- 分桶算法：按稳定标识（userId 或生成的匿名 id）取 hash，对 100 取模得到分组——保证同用户永远同桶。
- 实验配置热更新：分桶比例存远端配置（fetch 一次后缓存），不用发版改代码；Edge 里可用模块级内存缓存短 TTL。
- 统计与归因：响应头注入 `x-experiment: home-v2`，服务端日志/埋点据此归因；确保两版本页面都有曝光事件。

```ts
// middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

function hash(str) {
  let h = 0;
  for (const c of str) h = (h * 31 + c.charCodeAt(0)) | 0;
  return Math.abs(h);
}

export async function middleware(req: NextRequest) {
  const exp = req.nextUrl.pathname;
  if (exp !== '/') return NextResponse.next();

  // 1) 取稳定标识：优先 userId cookie，否则生成匿名 id
  let uid = req.cookies.get('uid')?.value;
  const isNew = !uid;
  uid ??= crypto.randomUUID();

  // 2) 分桶：hash % 100 < 10 -> 实验组（10% 灰度）
  const bucket = hash(uid) % 100;
  const isBeta = bucket < 10;

  const res = isBeta
    ? NextResponse.rewrite(new URL('/home-v2', req.url)) // 改写到新版页面，URL 不变
    : NextResponse.next();

  // 3) 会话固化：uid 与分组都写 cookie，刷新不跳桶
  res.cookies.set('uid', uid, { maxAge: 31536000, path: '/' });
  res.cookies.set('exp-home', isBeta ? 'v2' : 'v1', { maxAge: 31536000, path: '/' });
  res.headers.set('x-experiment', `home:${isBeta ? 'v2' : 'v1'}`);
  if (isNew) res.headers.set('x-new-user', '1');
  return res;
}

export const config = { matcher: ['/', '/home-v2'] };
```
