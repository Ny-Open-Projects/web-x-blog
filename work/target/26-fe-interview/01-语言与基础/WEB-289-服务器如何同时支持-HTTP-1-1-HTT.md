---
title: [WEB-289] 服务器如何同时支持 HTTP/1.1、HTTP/2、HTTP/3 并让浏览器选到最快的？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP3]
type: 面试题
---

## WEB-289：服务器如何同时支持 HTTP/1.1、HTTP/2、HTTP/3 并让浏览器选到最快的？
**答**：
- 入口按端口分工：443 上同时跑 TCP（1.1/2 由 ALPN 协商）和 UDP（QUIC/3）。
- HTTP/1.1→2 客户端走 TLS ALPN 直接协商；HTTP/3 的发现依赖响应头 Alt-Svc: h3=":443"，浏览器记住后在后续请求尝试 UDP。
- 灰度做法：Alt-Svc 先带短 max-age 观察指标，稳定后加 ma=31536000 并配 DNS HTTPS 记录（SVCB）让首次连接就直连 h3。

```javascript
// Nginx/Caddy 典型配置要点
// listen 443 ssl http2;        # TCP 侧 ALPN: h2 / http/1.1
// listen 443 quic reuseport;   # UDP 侧 HTTP/3
// add_header Alt-Svc 'h3=":443"; ma=86400';   # 引导浏览器尝试 h3
const negotiate = (clientProtos, serverProtos) =>
  clientProtos.find(p => serverProtos.includes(p)); // ALPN 逻辑
console.log(negotiate(['h3', 'h2', 'http/1.1'], ['h2', 'http/1.1'])); // h2
```
