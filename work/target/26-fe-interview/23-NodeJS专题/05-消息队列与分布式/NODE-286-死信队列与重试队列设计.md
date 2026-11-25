---
title: [NODE-286] 死信队列与重试队列设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-286：死信队列与重试队列设计？
**答**:
- 重试队列分级：retry-1s/retry-30s/retry-5m（延迟递增，避免毒消息阻塞主队列）——Kafka 用多 topic + 延迟投递实现，BullMQ 用 backoff 原生支持。
- 死信（DLQ）：重试 N 次仍失败 → DLQ + 告警——人工介入或后台任务修复后回放。
- 设计要点：死信消息带完整上下文（原始 payload+失败原因+重试次数）；DLQ 消费面板（运营可重放）。
- 防毒消息：重复失败的消息隔离，不能无限重试占用资源（重试预算）。

```javascript
// 分级重试（Kafka 多 topic）
async function processWithRetry(msg) {
  try { await process(msg); }
  catch (e) {
    const retries = msg.headers?.['x-retry'] ?? 0;
    if (retries < 3) {
      const delayTopic = ['retry-1s', 'retry-30s', 'retry-5m'][retries];
      await producer.send({ topic: delayTopic, messages: [{ value: msg.value, headers: { 'x-retry': String(retries + 1) } }] });
    } else {
      await producer.send({ topic: 'dlq', messages: [{ value: msg.value, headers: { 'x-error': String(e) } }] });
      alert.dlq(msg);                                  // 死信告警
    }
  }
}
```
