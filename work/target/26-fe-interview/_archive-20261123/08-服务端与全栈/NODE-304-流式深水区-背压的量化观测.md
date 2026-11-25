---
title: [NODE-304] 流式深水区：背压的量化观测？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-304：流式深水区：背压的量化观测？
**答**:
- 观测点三处：可读流 readableLength（内部缓冲字节数）、可写流 writableLength/needDrain（积压量）、pipeline 各段吞吐差（前段 QPS > 后段 = 积压）。
- 指标化：writableLength 直方图 + drain 事件计数 + write false 频率——"背压发生率"进监控。
- 异常模式：writableLength 持续高位 → 下游慢（客户端慢/DB 慢）；内存涨但 writableLength 低 → 上游 push 过快（自定义流背压缺失 NODE-211）。
- 容量联动：背压率高时自动降并发/限流（NODE-272 队列思路的流版本）。

```javascript
// 背压观测探针
setInterval(() => {
  metrics.histogram('stream.writableLength', ws.writableLength, { route: ctx.path });
  metrics.inc('stream.writeFalse', ws.writableNeedDrain ? 1 : 0);
}, 5000);
ws.on('drain', () => metrics.inc('stream.drain'));
// 判读：writeFalse/min > 10 && writableLength > highWaterMark → 下游瓶颈告警
// 修复：下游并发扩容 / 上游加队列限流 / 水位线调大（NODE-222）
```
