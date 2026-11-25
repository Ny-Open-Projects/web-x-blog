---
title: [NODE-675] Redis pub/sub 与 MQ（Kafka/RabbitMQ）怎么选？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-675：pub/sub vs MQ 怎么选？
**答**：
- Redis pub/sub：广播语义（无持久化——订阅者不在线消息丢失）、低延迟、扇出轻量——适合「在线通知」（WS 广播跨实例，SCN-NODE-650）、缓存失效通知。
- MQ（Kafka/RabbitMQ）：持久化 + 消费确认 + 重试/死信——适合「业务事件」（订单/消息必达，SCN-NODE-651 消费纪律）。
- 决策问题：消息丢了会怎样？——丢得起（实时性优先）用 pub/sub；丢不起（业务正确性）用 MQ；「实时且不能丢」——MQ + 消费后推送（复杂度换可靠性）。
- 混用模式：MQ 做主干（业务事件持久化）+ pub/sub 做枝叶（实时通知广播）——各按语义分工。
- 追问钩子：为什么「缓存失效通知」常用 pub/sub 而「订单事件」必须 MQ——失效通知丢了最多多一次回源（缓存 miss 自愈，代价小）；订单事件丢了是数据不一致（不可自愈）——按「丢失代价」选基础设施，而不是按「技术偏好」；代价小的广播用轻量 pub/sub，代价大的必达走 MQ。

```javascript
// pub/sub：WS 广播（丢失可容忍）
redisSub.subscribe('ws:broadcast');
redisSub.on('message', (ch, msg) => localBroadcast(msg));
// MQ：订单事件（不可丢）
await kafka.producer.send({ topic: 'orders',
  messages: [{ key: order.id, value: JSON.stringify(order) }] });   // 分区有序
```
