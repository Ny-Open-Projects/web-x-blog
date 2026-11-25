---
title: [MFW-104] SvelteKit 的 hooks（handle、handleFetch、handleError）各管什么？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-104：SvelteKit 的 hooks（handle、handleFetch、handleError）各管什么？
**答**：
- `handle`：**每个请求**进出的总闸（≈ Next Middleware + Nitro middleware），用于鉴权解析 locals、计时、改响应头。`event.locals` 是请求级上下文载体，load/action 里通过 `locals` 取。
- `handleFetch`：拦截 load 内的 `event.fetch`，用于服务端代理（绕 CORS）、统一注入内部网关头、重写到内网服务。
- `handleError`：未捕获错误的最后一站（服务端+客户端各一份），用于上报 APM，**不能**用来改响应——改状态码要在 handle 里做或让错误自带 status。
- 与 Next 对照：handle ≈ middleware.ts + instrumentation 合体；handleFetch ≈ rewrites 的运行时版；handleError ≈ error.tsx 之外的日志层。

```ts
// src/hooks.server.ts
import type { Handle, HandleFetch, HandleServerError } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
  // 1. 鉴权：解析 session -> locals（后续 load/action 直接用）
  const sid = event.cookies.get('session');
  event.locals.user = sid ? await getSessionUser(sid) : null;

  // 2. 计时与响应头
  const t0 = Date.now();
  const response = await resolve(event);
  response.headers.set('server-timing', `total;dur=${Date.now() - t0}`);
  return response;
};

export const handleFetch: HandleFetch = async ({ request, event }) => {
  // 内部 API 代理：服务端请求补内部头，绕过浏览器 CORS
  if (request.url.startsWith('https://internal-api/')) {
    request = new Request(request.url.replace('https://internal-api', 'http://internal:8080'), request);
    request.headers.set('x-forwarded-user', event.locals.user?.id ?? 'anon');
  }
  return fetch(request);
};

export const handleError: HandleServerError = ({ error, event }) => {
  apm.captureException(error, { path: event.url.pathname, userId: event.locals.user?.id });
  return { message: '内部错误' }; // 返回给客户端的脱敏 message
};
```
