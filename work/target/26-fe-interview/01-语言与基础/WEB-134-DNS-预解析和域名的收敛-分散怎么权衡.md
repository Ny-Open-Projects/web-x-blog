---
title: [WEB-134] DNS 预解析和域名的收敛/分散怎么权衡？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-134：DNS 预解析和域名的收敛/分散怎么权衡？
**答**：
- HTTP/1.1 时代同域 6 连接限制，工程上把静态资源散到多个子域（domain sharding）换并发；代价是多次 DNS、多次 TLS，Cookie 也跟着域名走。
- HTTP/2/3 单连接多路复用，域名应收敛：散域名反而破坏连接复用，还会拖慢握手。
- `dns-prefetch` 只提前解析；`preconnect` 把 DNS+TCP+TLS 都提前做完，用于关键第三方域。
- 预解析对不可控第三方域收益最大（统计、CDN、字体）；自家主域浏览器一般会提前解析。
- Cookie 瘦身也属域名规划：静态域用独立裸域，不带业务 Cookie。

```html
<!-- 关键第三方域做完整预连接，用户点击前完成 DNS 加 TCP 加 TLS -->
<link rel="preconnect" href="https://cdn.example.com" crossorigin>
<!-- 次要域只做 DNS 预解析，几乎零成本 -->
<link rel="dns-prefetch" href="//img.example.com">
<!-- HTTP/2 时代建议：主站与 API 收敛到同一域名，去掉无意义的散子域 -->
<script src="https://app.example.com/static/app.js"></script>
```
