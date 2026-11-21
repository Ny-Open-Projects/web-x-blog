---
title: [NODE-391] Node 服务的后台任务失败补偿机制如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-391：后台任务失败补偿机制
**答**:
- 失败分类与对策：瞬时失败（网络抖动——指数退避重试，BullMQ attempts+backoff）、确定性失败（参数错误——重试无意义，直接死信 + 人工）、依赖故障（下游挂——熔断暂停消费，恢复后继续）。
- 补偿三通道：队列内重试（默认）、延迟补偿任务（失败后投递"补偿任务"延后执行）、对账兜底（ARC-382，定期扫未完成任务强制收敛）。
- 任务状态机：pending → running → done/failed/retry，每次转移记录（重试次数/最后错误/下次执行时间）；卡死检测（running 超 maxDuration 标记 failed 重投——进程崩溃的任务靠可见性超时回收，SQS 思想）。
- 补偿任务本身要幂等（NODE-381）且限流（补偿风暴不能打挂下游——补偿也走限流器）。
- 死信治理：死信队列有专门看板与处理 SOP（重放/丢弃/修复数据后重放），重放工具化。
```javascript
worker.on('failed', async (job, err) => {
  if (isPermanent(err)) return moveToDLQ(job, err);             // 确定性失败不重试
  if (job.attemptsMade >= job.opts.attempts)
    await scheduleCompensation({ type: 'requeue-later', job: job.data, after: '1h' }); // 延迟补偿
});
// 卡死回收：visibilityTimeout 后未 ack 的任务自动重新可见
```
