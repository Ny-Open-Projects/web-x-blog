---
title: [PER-090] 103 Early Hints 是什么？如何在服务端启用资源提示？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-090：103 Early Hints 是什么？如何在服务端启用资源提示？

**答**：
- Early Hints：服务器在**最终响应之前**先发一个 103 状态码，把预加载提示（preload/preconnect）提前告诉浏览器——HTML 还在生成时浏览器就开始下载关键资源，省掉“HTML 下载完才知道要什么”的空窗。
- 与 preload 的关系：HTML 里的 `<link rel=preload>` 必须等 HTML 头解析到才生效，103 把这一步提前到 TTFB 之前，LCP 收益通常在几十到几百毫秒。
- 服务端实现要求：上游（应用）返回 hint 列表，边缘节点（支持 103 的代理/CDN）在回源期间先行下发；nginx 需较新版本或用支持 103 的网关。
- 注意事项：hint 是建议不是承诺，浏览器可忽略；不要塞过多资源，避免挤占关键路径带宽。

```javascript
// Node 原生 HTTP2 服务：发送 103 Early Hints（自建网关场景）
const http2 = require('http2');
const server = http2.createSecureServer({
  key: require('fs').readFileSync('key.pem'),
  cert: require('fs').readFileSync('cert.pem'),
});

server.on('stream', (stream, headers) => {
  if (headers[':path'] !== '/') return stream.respond({ ':status': 404 }).end();
  // 1) 最终响应之前先发 103：关键资源提示立刻生效
  stream.respond({
    ':status': 103,
    'link': '</img/hero.avif>; rel=preload; as=image; fetchpriority=high, '
          + '</fonts/brand.woff2>; rel=preload; as=font; type=font/woff2; crossorigin, '
          + '<https://api.example.com>; rel=preconnect; crossorigin',
  });
  // 2) 再正常返回页面（此处模拟耗时的模板渲染）
  setTimeout(() => {
    stream.respond({ ':status': 200, 'content-type': 'text/html; charset=utf-8' });
    stream.end('<!doctype html><html><head><link rel="preload" as="image" href="/img/hero.avif"></head><body>ok</body></html>');
  }, 150);
});
server.listen(8443);
```
