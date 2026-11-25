---
title: [NODE-250] 多进程并发部署的综合面试题：如何设计一个能扛住 1 万 QPS 的 Node 服务？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-250：多进程并发部署的综合面试题：如何设计一个能扛住 1 万 QPS 的 Node 服务？
**答**:
- 分层答题：单机多核（cluster/PM2 8 实例）→ 多机（Nginx LB 3 台）→ 依赖（Redis 集中状态、连接池收敛）→ 缓存（本地+集中两级）→ 限流保护（网关+应用双限）。
- 单实例容量估算：Node 单进程 HTTP 吞吐 ~2-4k QPS（简单 JSON 响应），×8 核 ≈ 单机 1.6-3 万——留 40% 水位线设计。
- 瓶颈定位顺序：先看事件循环 ELU（CPU 层）、DB 连接池等待（依赖层）、网络缓冲（内存层）。
- 稳定性配套：优雅重启（NODE-244）、过载摘流（249）、trace 采样（NODE-36x）。

```javascript
// 容量与保护配置单
const plan = {
  instances: os.cpus().length,                 // cluster ×8
  keepAliveTimeout: 5,                         // Nginx upstream keepalive 匹配
  dbPool: { max: 20 },                         // 每进程 20 → ×8 = 160（对齐 DB max_connections）
  redisPool: { max: 50 },
  rateLimit: { window: '1s', perUid: 50 },     // Redis 计数（NODE-243）
  health: { eluThreshold: 0.85, rssMB: 500 },  // 摘流阈值
};
// 验证：autocannon -c 2000 -d 60 → 目标 P95 < 100ms 且 errors=0
// 扩展路径：单机饱和 → 横向加机器（Nginx upstream 扩列表）→ 分库分表
```
