---
title: [MFW-517] 边缘全栈的数据访问：无 DB 直连时代的连接架构
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-517：边缘全栈数据访问：无 DB 直连时代的架构

**答**:
- Edge 无长连 TCP 的原因：边缘实例是短命/无状态的（连接池无意义）+ TCP 长连接的握手成本（每次冷启动建连 = 延迟）——架构响应：1) **HTTP 代理层**（Planetscale HTTP driver/Neon serverless driver——SQL over HTTP/ websocket）；2) **边缘原生存储**（D1/KV/Durable Objects——平台原生 API）；3) **中心网关**（edge 调中心 API——一跳内网）。
- 各方案的延迟特征：HTTP SQL（每查询一次 HTTP 往返——批量化重要：单请求多语句）、KV（毫秒读/最终一致）、中心代理（区域间 RTT 50-200ms——高频查询不适合）。
- 选型矩阵：读多写少的会话/配置 → KV；强一致事务 → 中心 API（接受 RTT）或区域化主库（延迟感知路由 RBL-14）；分析聚合 → 边缘物化视图（预聚合 KV）。
- 追问钩子：为什么「连接池」在 Edge 架构中失效？——连接池的价值 = 复用 TCP 建连成本（池驻留在长进程）；Edge 实例随时缩容/无共享内存——池随实例死亡；替代是「把建连成本转移到平台侧」（HTTP driver 由平台维护 HTTP/2 多路复用）——「短命运行时的一切有状态优化失效」是 Edge 架构的第一性约束（RBL-924 容器协商的极端版）。

```javascript
// Edge 数据访问三模式
// 1) HTTP SQL driver（单请求批量化）
import { execute } from '@planetscale/database';
const results = await execute(connection, [
  { sql: 'SELECT * FROM products WHERE id = ?', args: [id] },
  { sql: 'SELECT * FROM reviews WHERE pid = ?', args: [id] },   // 两查询一往返
]);
// 2) KV 会话缓存
const session = await env.SESSIONS.get(sid, 'json');    // 边缘 KV 毫秒读
// 3) 中心网关（强一致事务）
await fetch(`${ORIGIN}/api/tx`, { method: 'POST', body: tx });   // 接受跨区 RTT
// 选型决策
const route = (query) =>
  query.kind === 'session' ? kv()
  : query.kind === 'transaction' ? originTx()
  : httpSql();                                           // 默认 HTTP SQL
```
