---
title: [NODE-240] PM2 cluster 的负载分配策略？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-240：PM2 cluster 的负载分配策略？
**答**:
- 分发机制：cluster 的 accept 分发在 Linux 上默认由内核（SO_REUSEPORT）轮询，其他平台由 master 轮询分发——round-robin 偏差不感知连接耗时。
- 长连接偏差：SSE/WS 场景轮询分配导致某些 worker 连接集中——应用层做连接数均衡或外部 LB（Nginx least_conn）。
- 与 Nginx 的分工：PM2 cluster 做单机多核，Nginx 做跨机 LB+静态资源——两层各自轮询。
- 健康度感知：PM2 本身不带 least_conn；要"按负载分发"需要应用上报指标 + 网关层路由（NODE-28x 健康探针联动）。

```javascript
// 长连接均衡（应用层）
const counts = new Map();    // worker 内：当前连接数
io.on('connection', sock => { counts.set(sock.id, 1);
  sock.on('disconnect', () => counts.delete(sock.id));
});
// 上报当前连接数 → 网关按 least_conn 分发新连接（自研分发服务）
// 或外部方案：Nginx upstream { least_conn; server 127.0.0.1:300x; } —— 直接分到各 worker 端口（fork 模式）
```
