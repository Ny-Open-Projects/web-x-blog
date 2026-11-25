---
title: [WEB-005] HTTP/2 的多路复用是怎么工作的？解决了什么问题？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-005：HTTP/2 的多路复用是怎么工作的？解决了什么问题？
**答**：
- HTTP/2 把报文拆成二进制帧（Frame），一个 TCP 连接里可以同时交错传输多个 Stream（逻辑流），每个 Stream 承载一个请求-响应。
- 帧上有 Stream ID 标识归属，接收端按 ID 重组，多个请求互不等待，解决了 HTTP/1.1 的应用层队头阻塞。
- 并发能力不再受浏览器 6 连接限制，域名分片、雪碧图等 HTTP/1.1 优化手段随之过时甚至有害。
- 注意：所有 Stream 共享一条 TCP 连接，TCP 丢包重传时仍会阻塞所有流，即 TCP 层队头阻塞（HTTP/3 才解决）。

```javascript
// HTTP/2 下多个请求跑在一条连接上，前端写法不变，收益由协议层自动获得
const resources = [
  fetch('/api/user'),
  fetch('/api/orders'),
  fetch('/api/messages'),
  fetch('/static/app.js'),
  fetch('/static/app.css'),
];
// 同一连接上 5 个请求并行交错传输，无需排队等前一个响应结束
const [user, orders, messages] = await Promise.all(resources.slice(0, 3)).then(
  ([u, o, m]) => Promise.all([u.json(), o.json(), m.json()])
);
console.log(user, orders, messages);
```
