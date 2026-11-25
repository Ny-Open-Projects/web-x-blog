---
title: [SCN-404] 笔试题——实现 IM 消息发送队列（串行+重试+超时）？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-404：手写 IM 发送队列：会话内串行保序、失败重试、ack 超时

**需求与边界**：
- 输入：发送函数（返回 ack）、消息流；输出：消息状态流转 sending→sent/failed。
- 边界要求：① 同会话串行（保序）、跨会话并行；② 重试 3 次指数退避，超限标 failed（可手动重发）；③ ack 超时 8s 判失败；④ 幂等 clientMsgId（重试不产生重复）。

**答**：
```javascript
class SendQueue {
  constructor({ send, retries = 3, ackTimeout = 8000 }) {
    this.send = send; this.retries = retries;
    this.ackTimeout = ackTimeout;
    this.queues = new Map();     // convId → 任务链
  }
  push(msg) {
    const q = this.queues.get(msg.convId) ??=
      Promise.resolve();         // 会话内串行链
    const task = q.then(() => this.exec(msg))
      .catch(() => {});          // 失败不阻塞后续
    this.queues.set(msg.convId, task);
    return task;
  }
  async exec(msg) {
    const id = msg.clientMsgId ?? uid();
    updateStatus(id, 'sending');               // 乐观上屏
    for (let i = 0; i <= this.retries; i++) {
      try {
        const ack = await withTimeout(
          this.send({ ...msg, clientMsgId: id }), // 幂等键
          this.ackTimeout);
        updateStatus(id, 'sent', ack.serverId);
        return ack;
      } catch (e) {
        if (i === this.retries) {
          updateStatus(id, 'failed', e.message);   // 手动重发入口
          throw e;
        }
        await sleep(2 ** i * 500);            // 指数退避
      }
    }
  }
}
const withTimeout = (p, ms) => Promise.race([
  p, sleep(ms).then(() => { throw new Error('ack 超时'); })]);
// 手动重发：resend(id) → queue.push(originalMsg)
//   （同 clientMsgId → 服务端幂等去重）。
// 跨会话：不同 convId 链互不阻塞（并行）。
```

**评分点**:
- 会话内串行链保序（Promise 链），跨会话并行互不阻塞。
- 幂等键 clientMsgId 全程携带（重试不重复上屏）。
- 三要素齐全：重试退避、ack 超时、failed 手动重发路径。
- 失败不阻塞同会话后续消息（catch 隔离）。
