---
title: [NODE-284] 消息顺序性保证？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-284：消息顺序性保证？
**答**:
- Kafka：同 key（如 orderId）进同分区 → 分区内串行；消费端单线程处理该分区（或按 key 哈希到内存队列串行）。
- RabbitMQ：单队列单消费者串行，或按业务路由到顺序队列。
- 全局有序代价大（单分区吞吐上限）——业务上只要"同实体有序"（key 有序）即可。
- 乱序补偿：版本号/时间戳消费端校验，旧版本事件丢弃（ARC 系列增量同步 rev 协议同款）。

```javascript
// 分区有序消费（kafkajs）
await consumer.subscribe({ topic: 'order-events', fromBeginning: false });
await consumer.run({
  partitionsConsumedConcurrently: 3,          // 分区间并行
  eachMessage: async ({ partition, message }) => {
    // 同分区内串行（kafkajs 保证）—— 同 orderId 的消息同分区
    await processOrderEvent(JSON.parse(message.value));
  },
});
// 乱序防护：
function apply(event) {
  if (event.rev <= state.rev) return;         // 旧版本事件丢弃
  state.rev = event.rev; /* apply */ 
}
```
