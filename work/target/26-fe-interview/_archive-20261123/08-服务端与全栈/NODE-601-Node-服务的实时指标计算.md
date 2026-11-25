---
title: [NODE-601] Node 服务的实时指标计算（大屏/监控的流式聚合）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-601：实时指标计算
**答**:
- 计算模式：滑动窗口聚合（事件流 → 滚动聚合：分钟级 QPS/错误率——Redis 滑动窗口计数）、实时大盘（大屏数据源——秒级新鲜度 ARC-538）、预聚合降载（精确实时 vs 秒级近似——按指标重要性分层）。
- 实现路径：轻量（Redis 窗口计数：INCR + TTL 分桶——分钟/小时桶）、中等（流处理：Kafka Streams/Flink——复杂指标）、查询时聚合（ClickHouse 秒级查询——明细入库实时查）。
- 一致性语义：近似值声明（实时指标标注精度：分钟桶对齐——不是精确到秒）、乱序与迟到数据（窗口闭合后迟到——修正策略：可更新窗口/最终一致声明）、时区与窗口对齐（业务日切窗口 ARC-481）。
- 性能保护：指标计算资源隔离（流计算不给在线链路抢资源）、热 key（超热指标分片计数 ARC-438）、下游爆炸保护（大屏刷新率限流——计算层限频）。
- 对账：实时值 vs 离线值校准（日终对账——实时计算的准确性监控，偏差告警）。
```javascript
// Redis 滑动窗口指标
async function incrMetric(name, dim) {
  const bucket = Math.floor(Date.now() / 60000);                 // 分钟桶
  const k = `m:${name}:${dim}:${bucket}`;
  await redis.multi().incr(k).expire(k, 3600).exec();            // 1h 保留
}
async function readLast(name, dim, minutes = 5) {
  const buckets = range(minutes).map(i => Math.floor(Date.now() / 60000) - i);
  return sum(await redis.mget(buckets.map(b => `m:${name}:${dim}:${b}`)));
}
```
