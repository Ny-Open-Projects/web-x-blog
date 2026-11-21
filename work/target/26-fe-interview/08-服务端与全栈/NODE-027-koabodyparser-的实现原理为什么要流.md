---
title: [NODE-027] koa-bodyparser 的实现原理？为什么要流式解析 body？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-027：koa-bodyparser 的实现原理？为什么要流式解析 body？
**答**：
- 原理：`ctx.req`（原生 IncomingMessage）是 Readable 流；bodyparser 在中间件里收集 `data`/`end`（或用 `raw-body` 库），按 `content-type` 分派解析（`application/json` → JSON.parse、`x-www-form-urlencoded` → querystring），结果挂到 `ctx.request.body`。
- 流式而非一次性 `readFile` 的原因：内存可控（超限即 413）、尽早开始、天然兼容 chunked 上传。生产还要求：只解析声明的方法（POST/PUT 等）、忽略 multipart（交给 formstream/busboy）、`onerror` 挂在 req 上防止 parse 失败崩溃进程。
- 高频追问：JSON.parse 大 body 会阻塞事件循环（同步 CPU）——超大 payload 应流式到磁盘或限制大小。

```javascript
// 简版 bodyparser 实现
function bodyParser(opts = {}) {
  const { enableTypes = ['json', 'form'], limit = '1mb' } = opts;
  const maxBytes = typeof limit === 'string'
    ? parseInt(limit) * (limit.endsWith('mb') ? 1024 * 1024 : 1024) : limit;

  return function bodyParserMiddleware(ctx, next) {
    const method = ctx.method.toUpperCase();
    if (!['POST', 'PUT', 'PATCH', 'DELETE'].includes(method)) return next();
    const type = (ctx.headers['content-type'] || '').split(';')[0].trim();

    if (type === 'multipart/form-data') return next();  // 交给专门的处理库

    return new Promise((resolve, reject) => {
      const chunks = [];
      let size = 0;
      ctx.req.on('data', (chunk) => {
        size += chunk.length;
        if (size > maxBytes) {
          ctx.req.removeAllListeners('data');   // 停止接收
          const err = new Error('body too large'); err.status = 413;
          ctx.req.destroy(err);
          return reject(err);
        }
        chunks.push(chunk);
      });
      ctx.req.on('end', () => {
        const raw = Buffer.concat(chunks).toString('utf8');
        try {
          ctx.request.body = type === 'application/json' && raw
            ? JSON.parse(raw)
            : Object.fromEntries(new URLSearchParams(raw));
          resolve(next());
        } catch (e) {
          e.status = 400; e.message = 'invalid json body';
          reject(e);
        }
      });
      ctx.req.on('error', reject);
    });
  };
}

// app.use(bodyParser()) → ctx.request.body 直接可用
```
