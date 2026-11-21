---
title: [OPT-179] HTTP 103 Early Hints 在首屏优化中怎么用？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-179：HTTP 103 Early Hints 在首屏优化中怎么用？

**答**：
- 问题：浏览器必须等 TTFB（HTML 响应头回来）才知道要加载哪些资源，服务器忙于生成 HTML 的这段时间被浪费。
- Early Hints：源站在最终响应前先发一个 `103` 信息性响应，携带 `Link` 头提示关键资源，CDN/浏览器提前开始 preconnect/preload，首屏资源发现提前 100~500ms。
- 落地方式：最简做法是 CDN 边缘缓存 103 提示（如 Cloudflare 自动生成），源站也可主动发；Node 层 `res.writeEarlyHints()`。
- 只放确定性的资源（首屏 CSS/JS 域名），不要塞过多（滥用会挤占带宽），与 200 响应的 Link 头保持一致避免冲突。

```javascript
// 一一对应：Node 原生 http 发送 103 Early Hints（Nginx 透传给浏览器）
const http = require('http');

http.createServer((req, res) => {
  // 1. 先发 103：不等业务逻辑，立即提示关键资源
  res.writeEarlyHints({
    link: [
      '</styles/main.css>; rel=preload; as=style',
      '</scripts/app.js>; rel=preload; as=script',
      '<https://cdn.example.com>; rel=preconnect',
    ],
  });
  // 2. 慢逻辑（查询 DB、拼 HTML）期间浏览器已在下载上述资源
  setTimeout(() => {
    // 3. 最终 200 响应：Link 头与 103 保持一致（不一致以 200 为准）
    res.writeHead(200, {
      'content-type': 'text/html',
      link: '</styles/main.css>; rel=preload; as=style',
    });
    res.end('<!doctype html><link rel="stylesheet" href="/styles/main.css">...');
  }, 300);
}).listen(3000);

// Express 开启：app.disable('x-powered-by'); 需要 Node >= 18.11 且 res.writeEarlyHints 存在
// Nginx 反代需 http2 开启；验证：curl -s -D - -o /dev/null --http2 https://site | grep -A1 103
```
