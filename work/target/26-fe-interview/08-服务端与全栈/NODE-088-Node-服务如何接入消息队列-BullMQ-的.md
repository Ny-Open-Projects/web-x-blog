---
title: [NODE-088] Node 服务如何接入消息队列（BullMQ 的队列、延迟与重试设计）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-088：Node 服务如何接入消息队列（BullMQ 的队列、延迟与重试设计）？
**答**：
- MQ 解决三件事：**削峰**（突发流量入队慢慢消费）、**解耦**（生产者不关心消费者）、**异步化**（耗时操作后台做）。BFF 常见：发短信/邮件、导出、缓存刷新、审计埋点。
- BullMQ 核心：Queue（生产）、Worker（消费，`concurrency` 控并发）、`attempts + backoff`（指数退避重试）、`delay`（延迟任务）、`removeOnComplete`（防堆积）、失败进 `failed` 集合人工处理或死信。
- 注意：处理器必须**幂等**（at-least-once 语义下消息会重复投递）；消费失败先重试后告警；监控队列积压水位（`getJobCounts`）。

```javascript
const { Queue, Worker, QueueEvents } = require('bullmq');
const IOREDIS_OPTS = { connection: { host: 'redis', maxRetriesPerRequest: null } };

// 生产：注册通知任务（延迟 + 重试策略）
const notifyQueue = new Queue('notify', IOREDIS_OPTS);
await notifyQueue.add('sms', { phone: '138****', template: 'order-shipped' }, {
  delay: 60_000,                                   // 1 分钟后发送（留撤销窗口）
  attempts: 5,
  backoff: { type: 'exponential', delay: 2000 },   // 2s 4s 8s 16s 32s
  removeOnComplete: { count: 1000 },               // 只保留最近 1000 条完成记录
  removeOnFail: false,                             // 失败保留，人工排查
  jobId: `sms-${orderId}`,                         // 业务幂等键：重复添加自动去重
});

// 消费：幂等处理器
new Worker('notify', async (job) => {
  const { phone, template } = job.data;
  const sent = await redis.get(`sms:sent:${job.id}`);
  if (sent) return;                                 // 幂等：已发送跳过（at-least-once 防重）
  await smsClient.send(phone, template);
  await redis.set(`sms:sent:${job.id}`, '1', 'EX', 86400);
}, { ...IOREDIS_OPTS, concurrency: 10 });

// 队列事件与监控
const qe = new QueueEvents('notify', IOREDIS_OPTS);
qe.on('failed', ({ jobId, failedReason }) => {
  log.error({ event: 'job_failed', jobId, failedReason });
  if (failedReason) alertToOps(`任务 ${jobId} 最终失败: ${failedReason}`); // 5 次重试后告警
});
setInterval(async () => {
  const counts = await notifyQueue.getJobCounts('waiting', 'active', 'failed');
  if (counts.waiting > 5000) log.warn({ event: 'queue_backlog', ...counts }); // 积压告警
}, 30000).unref();
```
