---
title: [NODE-474] Node 服务的 MQ 延迟与堆积（lag）处置预案如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-474：MQ 延迟与堆积处置
**答**:
- lag 是队列健康核心指标（消费延迟 = 业务延迟：消息延迟 10 分钟 = 用户积分晚到 10 分钟）。分级响应：lag 缓慢上升 → 扩消费者（NODE-437）；lag 剧增 → 故障处置（消费报错？上游突增？）。
- 堆积处置预案：扩容消费者（到分区上限——Kafka 消费者数 ≤ 分区数）、临时降级消费（非关键消息延后处理：暂停低优先级 topic 消费者让位）、批量处理模式（攒批处理提升吞吐 NODE-307）、必要时跳段（记录 checkpoint 跳过积压段 + 对账补偿——业务可接受时）。
- 根因处置：消费者 bug（毒消息死信隔离 ARC-344）、下游变慢（消费逻辑里同步调慢接口——改异步/加缓存）、上游突增（削峰：限流上游或扩容）。
- 预防：消费幂等（堆积重放安全）、消息 TTL/最大长度（防无限积压爆存储）、lag 告警分级（预计清空时间 > SLA 即告警——按吞吐算 ETA 而不是按绝对量）。
- 恢复：堆积清空后恢复常规消费速率、堆积期间的业务影响对账（积压期间的积分是否补齐）。
```javascript
// lag ETA 告警
setInterval(async () => {
  const { lag, throughput } = await consumer.lag();              // 条数/条每秒
  const eta = lag / throughput;
  if (eta > sla()) alert(`topic lag ${lag}, ETA ${eta}s 超 SLA`);
}, 30e3);
// 处置：scaleConsumer(+n) → lag 仍增 → 暂停 low-priority topic → 批处理模式
```
