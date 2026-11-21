---
title: [NODE-125] MySQL 主从复制与读写分离如何落地？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-125：MySQL 主从复制与读写分离如何落地？
**答**：
- 架构：写走主库，读走从库（读多写少业务吞吐翻倍）；复制是**异步**的，存在延迟窗口。
- 核心规则：**写后读必须走主**——下单后立刻查订单，走从库可能读不到，用户感知"丢单"。
- 实现层次：SQL 路由（写判定 + forceMaster 开关）、会话级策略（写后 N 秒内读主）、关键业务强制读主。
- 监控：`Seconds_Behind_Master` 超阈值把从库摘出读池；连接池读库单独配（NODE-121）。

```javascript
const master = mysql.createPool({ host: 'db-master', connectionLimit: 20, /* ... */ });
const slave = mysql.createPool({ host: 'db-slave', connectionLimit: 40, /* ... */ });

const WRITE_RE = /^\s*(insert|update|delete|replace|create|alter|begin)\b/i;
async function routeQuery(sql, params, { forceMaster = false } = {}) {
  if (forceMaster || WRITE_RE.test(sql)) return master.query(sql, params);
  return slave.query(sql, params);
}

// 写后读走主：事务提交后的第一次读强制主库
await routeQuery('INSERT INTO orders (id, uid) VALUES (?, ?)', [orderId, uid]);
const order = await routeQuery('SELECT * FROM orders WHERE id = ?',
  [orderId], { forceMaster: true });

// 会话级策略：写后 500ms 内的读都走主
function markJustWrote(ctx) { ctx.state.wroteAt = Date.now(); }
const shouldForceMaster = (ctx) => ctx.state.wroteAt && Date.now() - ctx.state.wroteAt < 500;
```
