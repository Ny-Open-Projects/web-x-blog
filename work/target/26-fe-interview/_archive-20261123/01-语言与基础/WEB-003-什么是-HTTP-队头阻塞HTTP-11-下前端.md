---
title: [WEB-003] 什么是 HTTP 队头阻塞？HTTP/1.1 下前端如何缓解？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-003：什么是 HTTP 队头阻塞？HTTP/1.1 下前端如何缓解？
**答**：
- HTTP/1.1 中一个 TCP 连接同一时刻只能处理一个请求-响应，前一个响应没回来，后面的请求即使已发出也要排队，这就是应用层队头阻塞。
- HTTP 管道化（pipelining）理论上可以连续发送请求，但响应仍必须按序返回，且多数浏览器默认关闭。
- 缓解手段：域名分片（拆成多个子域名绕过 6 连接限制）、雪碧图/内联小资源减少请求数、资源按优先级排队加载。
- 根治要靠 HTTP/2 多路复用（但 TCP 层队头阻塞仍在，直到 HTTP/3/QUIC）。

```javascript
// 演示：HTTP/1.1 同域名 6 个并发限制。超过 6 个请求会排队，
// 前面的响应慢会阻塞后面的请求（队头阻塞在 DevTools Network 的 Waterfall 可见）
async function loadImages(ids) {
  const urls = ids.map((id) => `https://cdn.example.com/img/${id}.png`);
  console.time('http1-queue');
  // 浏览器会自动把并发限制在每域名约 6 个，其余请求进入队列等待
  await Promise.all(urls.map((u) => fetch(u)));
  console.timeEnd('http1-queue');
}
loadImages([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]); // 后 4 个要等前 6 个完成

// 缓解方案一：静态资源走独立域名，扩展并发通道
fetch('https://static2.example.com/img/7.png');
```
