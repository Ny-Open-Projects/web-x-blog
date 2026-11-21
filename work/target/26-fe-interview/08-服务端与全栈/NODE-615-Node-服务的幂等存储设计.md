---
title: [NODE-615] Node 服务的幂等存储设计（幂等键表的容量与查询）如何优化？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-615：幂等存储优化
**答**:
- 容量问题：幂等记录随请求量线性增长（QPS 1k × 24h = 8600 万行/天——TTL 清理是刚需）。
- 存储选型：DB 唯一索引（严格但写放大——核心资金接口）、Redis（TTL 天然——SETEX 过期自动清理，非严格可接受场景）、组合（Redis 预检 + DB 兜底——NODE-488）。分表策略（按月分表/按 hash 分片——大表治理）。
- TTL 设计：幂等窗口（重试最长间隔决定——24h 覆盖大多数重试场景）、清理任务（定期删除过期——分批防锁 NODE-335）、记录压缩（只存必要：键/状态/响应摘要——大响应存引用）。
- 查询优化：键设计（业务前缀 + hash——索引友好）、并发请求（processing 状态 + 等待——NODE-529）、写入路径优化（ON CONFLICT DO NOTHING——单次往返）。
- 监控：幂等命中率（重复请求占比——异常高 = 上游重试配置问题）、表大小趋势（清理任务有效性）、写入延迟（幂等检查的开销——P99 < 5ms 目标）。
```javascript
// Redis + DB 组合幂等
async function checkIdem(key) {
  if (await redis.get(key)) return cached(key);                  // 快路径
  const row = await db.idem.findOne(key);                        // 兜底
  if (row) await redis.setex(key, 86400, row.response);
  return row?.response ?? null;                                  // miss → 执行后双写
}
// 清理：cron → DELETE WHERE created < now-24h LIMIT 10000 循环
```
