---
title: [NODE-018] 服务端如何完整实现 CORS？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, 20]
type: 笔试题
---

## NODE-018：服务端如何完整实现 CORS？
**答**：
- CORS 由浏览器执行，**服务端只需返回正确的响应头**。简单请求：`Access-Control-Allow-Origin`。预检请求（非简单方法/自定义头/content-type 非 form 等）先发 `OPTIONS`：需返回 `Allow-Origin` + `Allow-Methods` + `Allow-Headers` + `Max-Age`（缓存预检，减少 OPTIONS 风暴）。
- 带 cookie 需 `Allow-Credentials: true`，且 `Allow-Origin` **不能是 `*`**，必须是具体来源（从 `req.headers.origin` 回显并做白名单校验）。
- 高频坑：Nginx 与 Node **重复加 CORS 头**导致重复 header 报错；`Allow-Origin` 无条件回显 origin 等于裸奔（可被任意站点带凭证调用）。

```javascript
const http = require('node:http');

const ALLOWED_ORIGINS = new Set(['https://app.example.com', 'http://localhost:5173']);

function cors(req, res) {
  const origin = req.headers.origin || '';
  if (ALLOWED_ORIGINS.has(origin)) {
    res.setHeader('access-control-allow-origin', origin); // 白名单回显，不是 *
    res.setHeader('access-control-allow-credentials', 'true'); // 允许带 cookie
    res.setHeader('vary', 'origin'); // 告诉 CDN 缓存按 origin 区分，防止缓存串源
  }
  if (req.method === 'OPTIONS') {
    res.setHeader('access-control-allow-methods', 'GET, POST, PUT, DELETE, OPTIONS');
    res.setHeader('access-control-allow-headers', 'content-type, authorization, x-request-id');
    res.setHeader('access-control-max-age', '86400');           // 预检缓存 24h
    res.setHeader('access-control-expose-headers', 'x-total-count'); // 让前端能读自定义头
    res.writeHead(204).end();                                    // 预检直接结束
    return true;
  }
  return false;
}

http.createServer((req, res) => {
  if (cors(req, res)) return;
  if (!req.headers.origin || ALLOWED_ORIGINS.has(req.headers.origin)) {
    res.writeHead(200, { 'content-type': 'application/json' });
    res.end(JSON.stringify({ ok: true }));
  } else {
    res.writeHead(403).end();
  }
}).listen(3000);
```
