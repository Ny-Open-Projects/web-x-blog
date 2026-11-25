---
title: [NODE-121] 连接池参数如何调优？池满问题怎么排查？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-121：连接池参数如何调优？池满问题怎么排查？
**答**：
- 核心参数：`connectionLimit`（单实例连接数，按 DB 端 `max_connections` 分摊，起步≈核数×2）、`queueLimit`（排队上限，满了快速失败而非无限堆积）、`maxIdle/idleTimeout`（回收空闲连接）。
- 池满症状：报 "Queue limit reached" 或获取连接超时；`enqueue` 持续增长是前兆指标。
- 排查分流：DB 侧 CPU/IO 不高而队列长 → 池太小；DB 侧打满 → 慢查询占住连接（NODE-122），先治 SQL 再谈扩容。
- 红线：一次请求串行复用 1 个连接；并行查询数 × 并发请求 ≤ 池容量，否则互相排队放大延迟。

```javascript
const mysql = require('mysql2/promise');
const pool = mysql.createPool({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASS,
  database: 'shop',
  connectionLimit: 20,
  maxIdle: 10, idleTimeout: 60_000,
  queueLimit: 200,             // 排队上限，满了抛错快速失败
  waitForConnections: true,
  connectTimeout: 3000,
  enableKeepAlive: true,
});

// 两个关键监控点：排队（需求超供给的先兆）与在用数
pool.on('enqueue', () => metrics.inc('db_pool_enqueue'));
setInterval(() => {
  const inUse = pool.pool._allConnections.length - pool.pool._freeConnections.length;
  metrics.gauge('db_pool_in_use', inUse);
}, 5000).unref();

// 反例（放大排队）：一个请求并行抢 10 个连接 × 100 并发 = 需求 1000 > 池 20
// const [a, b] = await Promise.all([bigQuery1(), bigQuery2()]); // 大查询请串行或降并发
```
