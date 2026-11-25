---
title: [NODE-037] CORS 与 credentials 如何配合？带 cookie 跨域常踩哪些坑？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-037：CORS 与 credentials 如何配合？带 cookie 跨域常踩哪些坑？
**答**：
- 带 cookie 的跨域请求，前端必须 `fetch(url, { credentials: 'include' })`（或 axios `withCredentials: true`）；服务端必须 `Access-Control-Allow-Credentials: true` 且 `Allow-Origin` 为**精确 origin**（`*` 时浏览器直接拒收响应）。
- 高频坑：① `Allow-Origin: *` + credentials 组合非法；② `SameSite=None` 的 cookie 必须同时 `Secure`，否则 Chrome 拒发；③ localhost 多端口同源但跨子域部署时 cookie domain 要写 `.example.com` 顶层域；④ CORS 头被 Nginx 和 Node 重复设置导致浏览器报"duplicate header"。
- 排查口诀：先看预检 OPTIONS 是否 204，再看响应头是否齐全，最后看 cookie 是否 SameSite/Secure 阻断。

```javascript
// 服务端：完整 credentials CORS
const ALLOWED = new Set(['https://app.example.com', 'http://localhost:5173']);
app.use(async (ctx, next) => {
  const origin = ctx.get('origin');
  if (ALLOWED.has(origin)) {
    ctx.set('access-control-allow-origin', origin);
    ctx.set('access-control-allow-credentials', 'true');
    ctx.set('vary', 'origin');
  }
  if (ctx.method === 'OPTIONS') {
    ctx.set('access-control-allow-methods', 'GET,POST,PUT,DELETE');
    ctx.set('access-control-allow-headers', 'content-type,authorization');
    ctx.set('access-control-max-age', '86400');
    ctx.status = 204;
    return;
  }
  await next();
});

// 服务端下发跨域 cookie：SameSite=None 必须 Secure
ctx.cookies.set('sid', sid, {
  httpOnly: true,
  sameSite: 'none',   // 跨站携带
  secure: true,       // 强制 HTTPS
  domain: '.example.com', // 跨子域共享
});
```

```javascript
// 前端：credentials 配置
// fetch
fetch('https://bff.example.com/api/me', {
  method: 'GET',
  credentials: 'include',          // 关键：携带跨域 cookie
  headers: { 'content-type': 'application/json' },
});
// axios
axios.create({ baseURL: 'https://bff.example.com', withCredentials: true });
```
