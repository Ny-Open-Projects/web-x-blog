---
title: [OPT-011] 为什么说 HTTP2 下的域名分片（domain sharding）已经过时？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-011：为什么说 HTTP2 下的域名分片（domain sharding）已经过时？

**答**：
- 域名分片是 HTTP1.1 时代绕过"单域名 6 个并发连接"限制的手段，HTTP2 单连接多路复用，分片反而有害：多个域名意味着多次 TLS 握手、连接无法复用、丢失 HTTP2 的流优先级。
- 老项目迁移到 HTTP2 后应合并域名；静态资源域名从多个收敛到一个。
- 注意残留问题：HTTP2 仍有 TCP 层队头阻塞（丢包阻塞所有流），弱网高丢包场景 HTTP3/QUIC 才是根治方案。
- 用 `nextHopProtocol` 可验证资源实际走的协议版本（h2 / h3 / http/1.1）。

```javascript
// 一一对应：用 PerformanceResourceTiming 检查各资源实际协议
const resources = performance.getEntriesByType('resource');
const byProtocol = resources.reduce((acc, r) => {
  // nextHopProtocol 如 "h2"、"h3"、"http/1.1"
  acc[r.nextHopProtocol] = (acc[r.nextHopProtocol] || 0) + 1;
  return acc;
}, {});
console.log('各协议资源分布：', byProtocol);
// 若发现多个域名仍在用 http/1.1，说明存在未收敛的分片或降级
```
