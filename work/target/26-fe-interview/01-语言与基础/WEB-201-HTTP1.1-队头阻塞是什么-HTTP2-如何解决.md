---
title: [WEB-201] HTTP/1.1 的队头阻塞是什么？HTTP/2 如何解决？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP2]
type: 面试题
---

## WEB-201：HTTP/1.1 的队头阻塞是什么？HTTP/2 如何解决？

**答**：
- HTTP/1.1 队头阻塞分两层：HTTP 层上同一连接一次只能处理一个请求响应（pipelining 要求严格按序返回，前面的慢会堵住后面的）；传输层上浏览器只能给同一域名开 6~8 个 TCP 连接来绕，成本高。
- HTTP/2 引入二进制分帧，把每个请求/响应拆成带 stream ID 的帧，一条连接上多路复用，帧交错传输、按 stream ID 重组，互不阻塞。
- HTTP/2 只解决了 HTTP 层的队头阻塞；TCP 层的队头阻塞仍在——任何丢包都要等重传，所有 stream 一起等，这是 HTTP/3 改用 QUIC 的动机（追问钩子）。

```javascript
// 对比示意：同一页面 6 个资源
// HTTP/1.1：6 个 TCP 连接，每条串行「请求→响应」，长请求阻塞同连接后续
// HTTP/2：1 条连接
//   stream1: HEADERS + DATA(分片)
//   stream3: HEADERS + DATA   ← 与 stream1 的帧交错传输
//   stream5: HEADERS + DATA
// 用 fetch 验证协议版本（Chrome DevTools Network 面板 Protocol 列更直观）：
const t0 = performance.now();
Promise.all([
  fetch('/api/slow?ms=2000'), // 慢请求
  fetch('/api/fast?ms=50'),
]).then(([slow, fast]) => {
  console.log('HTTP/2 下 fast 不被 slow 阻塞');
});
```
