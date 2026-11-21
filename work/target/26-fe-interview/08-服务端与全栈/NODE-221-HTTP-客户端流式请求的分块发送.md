---
title: [NODE-221] HTTP 客户端流式请求的分块发送？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-221：HTTP 客户端流式请求的分块发送？
**答**：
- 上行流：fetch body 支持 ReadableStream（undici/Node 18+）——大文件分片上传时用流式 body 避免整文件读入内存。
- chunked 传输：Node http.request 默认 Transfer-Encoding: chunked（未定长时）；设置 Content-Length 可避免分块（网关更友好）。
- 背压联动：请求流挂起（await body drain）时 fetch promise 不 resolve——用 pipeline(stream, req) 语义（undici 支持 duplex: 'half'）。
- 实战：分片上传服务（NODE-070）的流式实现：文件流 → gzip → 上传，全程零整块缓存。

```javascript
// 流式上传（fetch + Web 流）
const nodeSrc = createReadStream('big.bin');
const webBody = Readable.toWeb(nodeSrc);   // Node → Web
await fetch('https://up.example.com/upload', {
  method: 'PUT',
  body: webBody,                            // chunked 上传，内存占用 O(chunk) 不 O(file)
  duplex: 'half',                           // Node fetch 上传流必需声明
});
// 带进度与取消：
const ac = new AbortController();
setTimeout(() => ac.abort(), 60000);
await fetch(url, { body: webBody, signal: ac.signal });   // 取消 → 上游流 destroy → fd 释放
```
