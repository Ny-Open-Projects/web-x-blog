---
title: [WEB-001] HTTP/1.1 有哪些核心特性？相对 HTTP/1.0 改进了什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-001：HTTP/1.1 有哪些核心特性？相对 HTTP/1.0 改进了什么？
**答**：
- 默认长连接：`Connection: keep-alive`，一次 TCP 连接可复用发送多个请求，减少握手开销。
- 引入 Host 头，支持一台服务器部署多个虚拟站点，是后续 CDN 与虚拟主机的基础。
- 支持分块传输 `Transfer-Encoding: chunked`，以及 Range 断点续传（配合 206）。
- 更完善的缓存控制头（`Cache-Control`、`ETag`）和更多请求方法（PUT、DELETE、OPTIONS 等）。
- 缺陷：同一连接上请求是串行响应的，存在队头阻塞；浏览器对同域名并发连接数有限制（一般 6 个）。

```javascript
// HTTP/1.1 报文通过文本头携带关键信息，代码中可读取这些头验证特性
fetch('https://api.example.com/data')
  .then((res) => {
    // HTTP/1.1 长连接复用由浏览器自动管理
    console.log(res.headers.get('connection')); // "keep-alive"
    console.log(res.headers.get('cache-control')); // 例如 "max-age=3600"
    console.log(res.headers.get('content-type')); // "application/json; charset=utf-8"
    return res.json();
  })
  .then((data) => console.log(data));
```
