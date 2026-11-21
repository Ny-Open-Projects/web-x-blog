---
title: [NODE-015] 如何用原生 http 模块实现一个带路由与请求体解析的服务？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, 20]
type: 笔试题
---

## NODE-015：如何用原生 http 模块实现一个带路由与请求体解析的服务？
**答**：
- 原生 http 服务是 `EventEmitter`：`req` 是 **Readable**（IncomingMessage），`res` 是 **Writable**（ServerResponse）。没有路由、没有 body 解析、没有中间件——一切自己组装，这正是理解 Express/Koa 的基础。
- 请求体解析：监听 `data`/`end` 拼接 Buffer（注意限制大小防 OOM），或交给流式解析。
- 面试要求：手写一个支持 `GET /health`、`POST /echo`（JSON body）的最小服务，含 404、错误兜底。

```javascript
const http = require('node:http');

const routes = [];
function route(method, path, handler) { routes.push({ method, path, handler }); }

// 请求体解析：限制 1MB，超限直接 413
function readBody(req, limit = 1024 * 1024) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    let size = 0;
    req.on('data', (chunk) => {
      size += chunk.length;
      if (size > limit) { reject(Object.assign(new Error('payload too large'), { code: 413 })); req.destroy(); return; }
      chunks.push(chunk);
    });
    req.on('end', () => resolve(Buffer.concat(chunks)));
    req.on('error', reject);
  });
}

route('GET', '/health', (req, res) => json(res, 200, { status: 'ok' }));
route('POST', '/echo', async (req, res) => {
  const body = JSON.parse((await readBody(req)).toString() || '{}');
  json(res, 200, { youSaid: body });
});

function json(res, status, data) {
  res.writeHead(status, { 'content-type': 'application/json; charset=utf-8' });
  res.end(JSON.stringify(data));
}

const server = http.createServer(async (req, res) => {
  try {
    const matched = routes.find((r) => r.method === req.method && r.path === req.url.split('?')[0]);
    if (!matched) return json(res, 404, { error: 'Not Found', path: req.url });
    await matched.handler(req, res);
  } catch (err) {
    json(res, err.code === 413 ? 413 : 500, { error: err.message });
  }
});
server.listen(3000, () => console.log('http://localhost:3000'));
// curl -X POST localhost:3000/echo -d '{"msg":"hi"}' -H 'content-type: application/json'
```
