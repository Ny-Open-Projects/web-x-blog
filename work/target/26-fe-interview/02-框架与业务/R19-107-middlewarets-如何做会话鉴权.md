---
title: [R19-107] middleware.ts 如何做会话鉴权？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-107：middleware.ts 如何做会话鉴权？
**答**：
- middleware 运行在边缘，每个请求先过它：检查 cookie 会话，未登录 302 到登录页并带 from 参数记录来路。
- 公开路径（login/register/auth API）直接放行，避免死循环重定向。
- 可以向下游注入解析好的用户头（x-user-id），页面层不再重复解析会话。
- matcher 必须排除 _next/static、图片等静态资源，否则浪费边缘计算。

```typescript
// middleware.ts —— 在边缘对每个请求做会话检查
import { NextResponse, type NextRequest } from 'next/server';

const PUBLIC_PATHS = ['/login', '/register', '/api/auth'];

export function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;
  if (PUBLIC_PATHS.some(p => pathname.startsWith(p))) return NextResponse.next();

  const session = request.cookies.get('session')?.value;
  if (!session) {
    const loginUrl = new URL('/login', request.url);
    loginUrl.searchParams.set('from', pathname);   // 记录来路，登录后跳回
    return NextResponse.redirect(loginUrl);
  }

  // 向下游请求注入用户头，避免每个页面重复解析会话
  const headers = new Headers(request.headers);
  headers.set('x-user-id', parseSession(session).userId);
  return NextResponse.next({ request: { headers } });
}

export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon.ico).*)'],  // 排除静态资源
};
```

---

## 第十七章 测试与质量（R19-108 ~ R19-112）
