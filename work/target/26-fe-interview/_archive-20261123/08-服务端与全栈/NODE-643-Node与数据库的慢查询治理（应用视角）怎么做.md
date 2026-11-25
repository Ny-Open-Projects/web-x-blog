---
title: [NODE-643] Node 与数据库的慢查询治理（应用视角）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-643：慢查询治理（应用侧）怎么做？
**答**：
- 应用侧能做的：查询超时（statement_timeout——不无限等）、连接池隔离（慢查询独占池 vs 快查询池分离——慢查询不饿死快接口）、查询日志采样（慢查询全量 + 快查询采样——SCN-SLA-724 分层采样）、N+1 检测（ORM 的查询计数告警）。
- 读写分离与路由：读走副本（延迟容忍标注——哪些查询可以读旧数据）、写走主库；应用层显式路由而非隐式代理（可测可控）。
- 批量化：N+1 → IN 批查/批量插入（copy/values 多值）——ORM 逐条操作的批量改写。
- 观测联动：慢查询与 trace 关联（traceId 进 SQL 注释——DBA 从慢日志反查到接口，SCN-NODE-564 可观测同源）。
- 追问钩子：为什么「慢查询池隔离」优于「统一池调参」——统一池时慢查询占住连接，快接口（毫秒级）也拿不到连接（池耗尽雪崩）；隔离后慢查询只耗尽自己的池，快接口不受影响——故障隔离在资源层的应用（SCN-NODE-639 池耗尽策略的进阶）。

```javascript
const pools = {
  fast: createPool({ max: 20, statement_timeout: 1000 }),   // 快接口池
  slow: createPool({ max: 5, statement_timeout: 30_000 }),  // 报表/导出池
};
// traceId 注入 SQL 注释
db.query(`/* trace=${traceId} */ SELECT ...`);
// N+1 检测
orm.on('query', () => { if (++queryCount > 50) warn(`N+1? ${traceId}`); });
```
