---
title: [AV-064] 实时消息的可靠性（ACK/重发/乱序）怎么保证？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-064：实时消息的可靠性（ACK/重发/乱序）怎么保证？
**答**：
- 三种投递语义：至多一次（丢了就丢，如弹幕）、至少一次（ACK+重发，可能重复，如礼物计数要做幂等）、恰好一次（至少一次 + 去重 ID）。
- DataChannel 可靠模式（ordered:true）已经保证有序可靠，走类 TCP；不可靠模式（maxRetransmits:0）类 UDP，适合高频状态（位置同步）。
- 自研 ACK：消息带 msgId，接收方回 ack；发送方维护 unacked 队列，超时重发（指数退避），收到 ack 移除。
- 乱序处理：按 (senderId, seq) 排序窗口，先缓存后交付；状态类消息只认最新（last-write-wins）。
- 持久化兜底：重要消息（连麦申请）写服务端队列，离线成员重连后拉取，防"只发给了在线的人"。

```javascript
// DataChannel 上的 ACK/重发层
class ReliableChannel {
  constructor(dc) {
    this.dc = dc; this.unacked = new Map(); this.nextId = 0;
    dc.onmessage = (e) => {
      const m = JSON.parse(e.data);
      if (m.ack) { this.unacked.delete(m.ack); return; } // 对端确认
      dc.send(JSON.stringify({ ack: m.id }));            // 立即回 ACK
      this.onMessage?.(m.payload);
    };
  }
  send(payload, { maxRetry = 5 } = {}) {
    const id = `${this.dc.label}-${this.nextId++}`;
    const frame = JSON.stringify({ id, payload });
    let retry = 0;
    const attempt = () => {
      if (!this.unacked.has(id)) return;      // 已确认
      if (retry++ >= maxRetry) return this.onFail?.(id); // 彻底失败上抛
      this.dc.readyState === 'open' && this.dc.send(frame);
      const delay = 300 * 2 ** retry + Math.random() * 100;
      this.unacked.set(id, setTimeout(attempt, delay));
    };
    this.unacked.set(id, setTimeout(attempt, 0));
  }
  // 高频不可靠消息走独立通道
  static createFastChannel(pc, label) {
    return pc.createDataChannel(label, { ordered: false, maxRetransmits: 0 });
  }
}
```
