---
title: [NODE-113] 手写 koa-bodyparser——为什么必须流式解析？multipart 怎么处理？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, 20]
type: 笔试题
---

## NODE-113：手写 koa-bodyparser——为什么必须流式解析？multipart 怎么处理？
**答**：
- body 是**可读流**，不存在同步属性，必须监听 `data/end` 事件攒齐才能拿到完整内容。
- 流式解析的意义：**限长即断**（超过 limit 立即 destroy，不下载完才发现超限），高并发下避免大 body 撑爆内存。
- multipart（文件上传）绝不能攒进内存：按 busboy 事件流逐 field/file 处理，文件部分直接 pipe 到磁盘或对象存储。
- 细节：`content-length` 预检快速拒绝、JSON 解析失败转 400、`ctx.is()` 只处理声明的类型。

```javascript
function bodyParser({ limit = 1024 * 1024 } = {}) {
  return async (ctx, next) => {
    if (!ctx.is('application/json')) return next(); // 只处理 JSON
    const declared = Number(ctx.req.headers['content-length'] || 0);
    if (declared > limit) ctx.throw(413, 'payload too large');
    ctx.request.body = await readJson(ctx.req, limit);
    await next();
  };
}

function readJson(stream, limit) {
  return new Promise((resolve, reject) => {
    let size = 0; const chunks = [];
    stream.on('data', (chunk) => {
      size += chunk.length;
      if (size > limit) {
        stream.destroy(); // 限长即断，不浪费带宽
        return reject(Object.assign(new Error('too large'), { status: 413 }));
      }
      chunks.push(chunk);
    });
    stream.on('end', () => {
      if (!chunks.length) return resolve({});
      try { resolve(JSON.parse(Buffer.concat(chunks).toString('utf8'))); }
      catch { reject(Object.assign(new Error('invalid json'), { status: 400 })); }
    });
    stream.on('error', reject);
  });
}

// multipart 思路（生产直接用 busboy）：
// const form = busboy({ headers: ctx.headers, limits: { fileSize: 50 * 1024 * 1024 } });
// form.on('file', (name, fileStream, info) => fileStream.pipe(ossUploader)) // 不落内存直传
// form.on('field', (name, value) => (fields[name] = value));
// ctx.req.pipe(form); // busboy 解析边界，逐块吐事件
```
