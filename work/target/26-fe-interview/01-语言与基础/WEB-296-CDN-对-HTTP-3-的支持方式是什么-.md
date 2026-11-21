---
title: [WEB-296] CDN 对 HTTP/3 的支持方式是什么？边缘和源站可以不同协议吗？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP3]
type: 面试题
---

## WEB-296：CDN 对 HTTP/3 的支持方式是什么？边缘和源站可以不同协议吗？
**答**：
- HTTP/3 是逐跳协议：CDN 边缘对用户侧跑 h3，回源侧可以独立选择 TCP/HTTP2，两端互不影响。
- 边缘回源链路通常是长连接、专线质量好，h3 的弱网收益主要发生在"用户 ↔ 边缘"这段，这正是收益最大的一段。
- 接入注意：QUIC 需要 UDP 443 放行，运营商/企业防火墙可能拦 UDP，CDN 必须保留 TCP 回退，DNS/Alt-Svc 双开。

```javascript
// 链路示意
// 浏览器 --QUIC/UDP--> CDN 边缘 --HTTP/2 over TCP(专线)--> 源站
const hop = (edgeH3 = true, originH2 = true) => ({
  userToEdge: edgeH3 ? 'h3(UDP)' : 'h2(TCP)',
  edgeToOrigin: originH2 ? 'h2(TCP)' : 'h1.1(TCP)',
});
console.log(hop()); // 两跳协议解耦，弱网收益来自第一跳
```
