---
title: [MFW-029] Middleware 在 App Router 中执行时机是什么？能做哪些事、有哪些限制？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-029：Middleware 在 App Router 中执行时机是什么？能做哪些事、有哪些限制？
**答**：
- 执行时机：**缓存检查之前、每个请求最先执行**（Edge Runtime）——能重写/重定向/改请求头响应头，是全站流量的第一道关卡。
- 典型能力：鉴权拦截（未登录 302 到 /login）、A/B 分流与灰度（按 cookie/geo 改写 URL）、i18n 语言协商（Accept-Language 重写到 /zh /en）、安全头注入（CSP/HSTS）、打日志埋点。
- 限制：运行在 Edge Runtime——**没有 Node API**（fs、大型 npm 包不行），执行时长有限（一般 <50ms 预算）、不持久（无状态）；不能直接读数据库（应只校验 session cookie/调轻量接口）。
- `matcher` 控制生效范围，避免静态资源也过中间件；`NextResponse.rewrite` 改写的是后端目标路径、用户浏览器 URL 不变。
- 追问：middleware 与 layout 鉴权的区别——middleware 拦的是**请求**（能 redirect/rewrite），layout 守卫是**渲染结果层面**（渲染后再跳），关键资源要两层都做。

```ts
// middleware.ts（项目根）
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(req: NextRequest) {
  const { pathname } = req.nextUrl;

  // 1) 鉴权：未登录访问 /dashboard 重定向
  if (pathname.startsWith('/dashboard') && !req.cookies.get('session')) {
    const url = req.nextUrl.clone();
    url.pathname = '/login';
    url.searchParams.set('from', pathname);
    return NextResponse.redirect(url);
  }

  // 2) 灰度：带 x-beta cookie 的用户改写到新版本页面（URL 不变）
  if (req.cookies.get('x-beta') && pathname === '/') {
    const url = req.nextUrl.clone();
    url.pathname = '/beta-home';
    return NextResponse.rewrite(url);
  }

  // 3) 安全头：全站注入
  const res = NextResponse.next();
  res.headers.set('x-frame-options', 'DENY');
  return res;
}

export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon.ico).*)'], // 排除静态资源
};
```
