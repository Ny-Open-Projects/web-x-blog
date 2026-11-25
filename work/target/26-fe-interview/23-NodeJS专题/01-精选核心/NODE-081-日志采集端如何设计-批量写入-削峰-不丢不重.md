---
title: [NODE-081] 日志采集端如何设计（批量写入、削峰、不丢不重）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-081：日志采集端如何设计（批量写入、削峰、不丢不重）？
**答**：
- 场景：前端埋点/网关日志高并发写入，直接同步写 DB 会打爆。采集端职责：**接收（轻校验）→ 内存队列缓冲（削峰）→ 批量落盘**（每 N 条或每 T 秒 flush）→ 失败重试 → 背压保护（队列满丢弃低优先级并计数告警）。
- 不丢不重：接收层先入 Redis Stream/Kafka（持久化）再消费写库，进程崩溃有 MQ 兜底；消费幂等（消息唯一 id 去重表）。
- 性能要点：批量 INSERT（一次 500 条）、`Promise.allSettled` 分批、限流保护下游、监控队列水位。

```javascript
// 内存缓冲 + 批量写入的采集端
class LogCollector {
  constructor({ flushSize = 500, flushInterval = 2000, maxQueue = 100000 }) {
    this.buffer = [];
    this.flushSize = flushSize;
    this.maxQueue = maxQueue;
    this.dropped = 0;
    setInterval(() => this.flush(), flushInterval).unref();
  }

  // 接收：轻校验 + 快速入队，绝不同步写库
  add(events) {
    for (const e of events) {
      if (!e.event || typeof e.ts !== 'number') continue;      // 轻校验，脏数据直接丢
      if (this.buffer.length >= this.maxQueue) {
        this.dropped++;                                         // 背压：队列满丢弃并计数
        continue;
      }
      this.buffer.push({ ...e, _id: crypto.randomUUID(), serverTs: Date.now() });
    }
    if (this.buffer.length >= this.flushSize) this.flush();     // 满批立即刷
  }

  // 批量落盘：失败重试 + 幂等写入
  async flush() {
    if (!this.buffer.length) return;
    const batch = this.buffer.splice(0, this.flushSize);
    try {
      await db.query('INSERT INTO events (_id, event, ts, payload) VALUES ? ON DUPLICATE KEY UPDATE _id = _id',
        [batch.map((b) => [b._id, b.event, new Date(b.ts), JSON.stringify(b)])]);
      // ON DUPLICATE KEY = 消费幂等：重复消息不产生重复行
    } catch (err) {
      this.buffer.unshift(...batch.slice(0, this.maxQueue - this.buffer.length)); // 放回队首重试
      console.error('日志批量写入失败:', err.message);
    }
  }
}

router.post('/collect', async (ctx) => {
  collector.add(ctx.request.body.events);   // 批量接口：前端聚合后上报
  ctx.status = 204;                          // 立即返回，不等落盘
});

// 监控：每分钟上报队列水位与丢弃数
setInterval(() => {
  metrics.gauge('collector_queue_size', collector.buffer.length);
  metrics.gauge('collector_dropped', collector.dropped);
}, 60000).unref();
```

## 追问（补充）

**追问**：

1. 进程 OOM 时内存 buffer 里未 flush 的日志怎么做到不丢 → 队列到 80% 就先同步写本地 WAL 文件再异步补传，崩溃重启后扫描残留文件补投，纯内存方案在 OOM 面前必然丢。
2. 一次 flush 500 条失败重试，会不会写重 → 每条日志带客户端生成的 uuid，落库用 INSERT IGNORE 或 uuid 唯一索引，重试天然去重，而不是靠位点。
3. 下游 DB 变慢时采集端怎么背压又不阻塞业务 → 队列水位分三档：80% 丢 debug、95% 只留 error、100% 直接拒绝并计数告警，主线程永不阻塞，丢弃量必须进看板。
