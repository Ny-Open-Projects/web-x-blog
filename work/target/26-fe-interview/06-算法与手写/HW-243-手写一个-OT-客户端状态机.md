---
title: [HW-243] 手写一个 OT 客户端状态机：本地未确认与已确认三态
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-243：手写一个 OT 客户端状态机：本地未确认与已确认三态

**答**：
- 需求：实现 OTClient：状态 Synchronized / Awaiting（本地 op 未确认）/ AwaitingWithBuffer（有未确认+缓冲）；localOp：Synchronized 直接发送，其他进缓冲；serverAck：确认后发送缓冲（缓冲需先对服务端并发 op 做变换）；serverOp：按状态做变换（Awaiting 需变换 pending）。
- 边界：serverOp 到达时 pending op 未确认 → 变换 pending 而不是直接应用；缓冲多条时逐条变换；状态转移表驱动。
- 评分点：三态转移表；变换方向正确（对端 op 先变换 pending）。

```javascript
class OTClient {
  constructor(revision = 0) { this.rev = revision; this.state = 'sync'; this.pending = null; this.buffer = []; }
  localOp(op, send) {
    if (this.state === 'sync') { send(op, this.rev); this.pending = op; this.state = 'awaiting'; }
    else this.buffer.push(op);                            // awaiting 状态进缓冲
  }
  serverOp(op) {                                          // 服务端并发 op（先于 ack）
    if (this.state === 'awaiting') {
      const { a1, b1 } = transform(this.pending, op);
      this.pending = a1; applyLocal(b1);                  // 本地应用变换后的服务端 op
    } else if (this.state === 'buffering') {
      let other = op;
      const pair = transform(this.pending, other);
      this.pending = pair.a1; other = pair.b1;
      this.buffer = this.buffer.map(b => { const p = transform(b, other); other = p.b1; return p.a1; });
      applyLocal(other);
    }
  }
  serverAck(rev) {                                        // pending 确认
    this.rev = rev; this.state = 'buffering';
    if (this.buffer.length) {
      const next = this.buffer.shift();
      sendToServer(next, ++this.rev);
      this.pending = next;
      if (!this.buffer.length) this.state = 'awaiting';
    } else this.state = 'sync';
  }
}
```
