---
title: [NODE-651] 消息队列消费（幂等/重试/死信）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-651：MQ 消费怎么做？
**答**：
- 消费幂等：消息至少一次投递（at-least-once）——消费端幂等键（消息 ID + Redis SETNX / DB 唯一约束——SCN-FIN-519 幂等键同源）；重复消息的处理是 MQ 接入的第一件事。
- 重试与死信：消费失败 → 延迟重试（退避：1s/10s/1min——立即重试在故障期是风暴）→ 超过上限进死信队列（DLQ + 告警——死信有人盯：人工/自动补偿任务）。
- 顺序性：分区/队列级有序（同 key 消息同分区——Kafka key 路由）；消费端并行破坏顺序（多 worker）——需要顺序的消费用单 worker per key 或顺序窗口。
- 背压与限流：消费速率与下游容量匹配（消费限流——下游保护，SCN-NODE-641 限流复用）；积压监控与扩容联动。
- 追问钩子：为什么「立即重试」在 MQ 消费中是最危险的反模式——失败通常是下游故障（DB 满/下游超时），立即重试以队列速率轰炸故障下游（比正常流量更凶——重试风暴）；退避重试给下游恢复窗口，死信兜底让「放弃」是显式决策而非消息丢失。

```javascript
consumer.run({ eachMessage: async ({ message }) => {
  const ok = await idempotent.tryLock(message.id);     // SETNX 幂等
  if (!ok) return;                                     // 重复消息跳过
  try { await handle(message); }
  catch (e) {
    if (attempt(message) < 3) await scheduleRetry(message, backoff(attempt));
    else await dlq.send(message), alert('DLQ');        // 死信 + 告警
  }
}});
```
