---
title: [NODE-285] 消息堆积的应对策略？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-285：消息堆积的应对策略？
**答**:
- 先定位：堆积原因是生产激增（大促）还是消费变慢（下游依赖慢）。
- 应对阶梯：横向扩消费者（Kafka 分区数允许内扩容）→ 批量消费（一次拉 N 条批处理）→ 降级处理（非核心消息改异步低优先级）→ 紧急旁路（堆积消息导出到冷存，事后回放）。
- 防堆积：消费端并发与下游容量对齐（DB 连接池/限流）；生产端削峰（ARC/NODE-144 已讲）；堆积水位告警（lag 指标）。
- 回溯风险：扩分区后 key 重分布会破坏顺序——扩容前确认业务是否敏感。

```javascript
// 批量消费（kafkajs fetch 批）
await consumer.run({
  eachBatch: async ({ batch, resolveOffset, heartbeat }) => {
    const msgs = batch.messages.map(m => JSON.parse(m.value));
    await bulkProcess(msgs);                            // 一次 DB 批量（比逐条快 10x）
    msgs.forEach(m => resolveOffset(m.offset));
    await heartbeat();                                  // 批处理中保活
  },
});
// 堆积告警：consumerGroup lag > 10w 持续 5min → P1 告警 + 自动扩容 worker 数
```
