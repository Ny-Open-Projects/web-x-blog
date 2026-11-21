---
title: [NODE-298] MQ 链路追踪的续链？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-298：MQ 链路追踪的续链？
**答**:
- 异步链断裂问题：消息消费是"新入口"——上下文要随消息走：生产端把 trace 上下文注入消息头（traceparent），消费端提取并创建新 span（父 span 是生产端发送 span）。
- 消费端 span 命名：`process <topic>`——异步链路在 trace 树里是"树分叉"（一条 trace 覆盖同步链+异步分支）。
- 延迟任务/重试链：重试消息保留原 traceId + 新 spanId——追踪一条消息的完整生命周期。
- OTel instrumentation 已内建（kafkajs/amqplib 插件）——理解原理用于排查"链路断了"。

```javascript
// 生产端：注入上下文
import { context, propagation } from '@opentelemetry/api';
const carrier = {};
propagation.inject(context.active(), carrier);       // traceparent → carrier
await producer.send({ messages: [{ value, headers: carrier }] });
// 消费端：提取 + 新 span
consumer.run({ eachMessage: async ({ message }) => {
  const ctx = propagation.extract(context.active(), message.headers);   // 从消息头提取
  await tracer.startActiveSpan(`process ${topic}`, {}, ctx, async (span) => {
    await process(JSON.parse(message.value));
    span.end();
  });
}});
```
