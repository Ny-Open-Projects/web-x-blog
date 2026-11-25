---
title: [NODE-317] 消息队列深水区：消费端并发与下游对齐？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-317：消息队列深水区：消费端并发与下游对齐？
**答**:
- 对齐原则：消费并发上限 = min(分区数， 下游容量/单条耗时)——盲目拉满消费并发只会把下游打挂（背压反向传递）。
- 动态并发：按下游 P95 自适应（AIMD：成功加一失败减半）——Kafka consumer 的 fetch size 与 worker 池联动。
- 有界队列：消息拉取与处理解耦，队列满暂停 fetch（内置背压）——防内存膨胀。
- 熔断联动：下游熔断打开时暂停消费（pause/resume），避免白耗消息重试。

```javascript
// 下游对齐的消费调度
const queue = new PQueue({ concurrency: 8 });     // 对齐 DB 写入容量
let paused = false;
consumer.run({ eachMessage: async ({ message }) => {
  if (queue.size > 200) await consumer.pause([{ topic }]);   // 有界背压
  await queue.add(() => process(message));
  await consumer.resume([{ topic }]);
}});
// 下游熔断 → 消费暂停
breaker.on('open', () => consumer.pause([{ topic: 'orders' }]));
breaker.on('half-open-success', () => consumer.resume([{ topic: 'orders' }]));
```
