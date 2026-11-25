---
title: [NODE-736] 笔试题——实现 MQ 消费者框架（幂等/重试/死信/顺序）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-736：手写 MQ 消费框架

**需求与边界**：
- 需求：MQ 消费完整框架（SCN-NODE-651）——① 幂等（消息 ID SETNX）；② 退避重试（1s/10s/1min——延迟队列）；③ 死信（3 次后 DLQ + 告警）；④ 并发控制（per-key 顺序 + 全局限流——SCN-NODE-693）；⑤ 优雅关闭（排空——SCN-NODE-722）。

**答**：
```javascript
class ConsumerFramework {
  constructor({ concurrency = 10, maxRetries = 3 } = {}) {}
  async handle(message) {
    const key = `mq:${message.id}`;
    if (!(await redis.set(key, 1, 'PX', 86400_000, 'NX')))
      return;                                          // 幂等：重复消息跳过
    try {
      await byKeyQueue.run(message.key, () => handler(message));   // per-key 顺序
    } catch (e) {
      await redis.del(key);                            // 失败释放幂等键，重投的消息才能再进来
      const attempt = message.attempts ?? 0;
      if (attempt >= this.maxRetries) {
        await dlq.send(message); alert({ type: 'DLQ', id: message.id });   // 死信 + 告警
        return;
      }
      await delayedQueue.schedule(message, backoff(attempt));   // 退避重试（1s/10s/1min）
    }
  }
  async drain() {                                      // 优雅关闭（SCN-NODE-722）
    await byKeyQueue.drain();                          // 排空在途
    await consumer.stop();                             // 停止拉取
  }
}
// 全局限流（下游保护）
const limiter = tokenBucket({ rate: DOWNSTREAM_QPS });
consumer.wrap(handler => async (m) => {
  await limiter.take();                                // 消费限流（SCN-NODE-693）
  await handler(m);
});
```

**评分点**:
- 幂等 SETNX + 顺序 per-key + 全局限流三件套。
- 退避重试延迟队列（SCN-NODE-651 退避纪律）。
- 死信 + 告警（人工兜底——放弃是显式决策）。
- 优雅关闭排空（SCN-NODE-722 联动）。

## 变体与延伸（补充）

**变体与延伸**：

1. per-key 顺序消费时某条消息一直失败，会阻塞同 key 后续吗 → 会，所以失败 3 次就转延迟队列跳过，超 maxRetries 直接进 DLQ，保证同 key 不被一条毒消息卡死。
2. 优雅关闭排空要等多久，等不完怎么办 → 先停止拉新消息，最多等 30s 处理在途，超时把剩余消息 nack 回队列交给其他实例，而不是硬 kill 丢消息。
3. 死信队列堆积后能否自动重投 → 先按错误类型分类，可重试的批量重投并重置 retry 计数，不可重试的落库归档，全自动重投等于让毒消息再毒一次。
