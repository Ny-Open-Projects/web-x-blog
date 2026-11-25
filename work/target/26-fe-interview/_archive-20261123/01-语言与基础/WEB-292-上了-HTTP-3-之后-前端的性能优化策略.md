---
title: [WEB-292] 上了 HTTP/3 之后，前端的性能优化策略有什么变化？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP3]
type: 面试题
---

## WEB-292：上了 HTTP/3 之后，前端的性能优化策略有什么变化？
**答**：
- "少域名、少请求"的旧优化弱化：h3 流级复用无队头阻塞，域名分片反而破坏连接复用与 0-RTT。
- 资源合并（雪碧图、concat）收益下降，小而多的请求 + 高优先级调度更利于 LCP；但请求数仍影响服务端/设备成本。
- 仍要做的：预连接（preconnect 到关键第三方）、0-RTT 场景的关键 GET、配合 103 Early Hints 提前下发关键资源提示。

```javascript
// h3 时代的连接优化
<link rel="preconnect" href="https://cdn.example.com" crossorigin>
// 服务器 103 Early Hints（在最终响应前先发）:
// 103 Early Hints
// Link: </critical.css>; rel=preload; as=style
const opts = { domainSharding: false, bundle: false, earlyHints: true };
console.log('h3: 不分片、少合并、抢首字节前就把资源提示给出去');
```
