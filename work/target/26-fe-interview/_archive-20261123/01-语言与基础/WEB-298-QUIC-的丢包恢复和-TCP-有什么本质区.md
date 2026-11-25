---
title: [WEB-298] QUIC 的丢包恢复和 TCP 有什么本质区别？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP3]
type: 面试题
---

## WEB-298：QUIC 的丢包恢复和 TCP 有什么本质区别？
**答**：
- TCP 重传包复用原四元组且序号空间混在一起，"这是原始包还是重传包"要靠时间戳猜；QUIC 包号单调递增不复用，重传就是新包号，一次清楚。
- QUIC 直接维护每个包的发送时间，RTT 用 ack 区间精确计算，RTO/PTO 探测也更准。
- 对前端的含义：弱网下重传更"聪明"，卡顿表现为短暂降速而不是长时间冻结。

```javascript
const sent = new Map(); // pn -> { time, size }
function send(pn, size) { sent.set(pn, { time: Date.now(), size }); }
function onAck(ackRanges) {
  for (const pn of sent.keys()) {
    if (ackRanges.some(([lo, hi]) => pn >= lo && pn <= hi)) {
      const { time } = sent.get(pn);
      console.log('RTT sample:', Date.now() - time); // 每个包可精确配对
      sent.delete(pn);
    }
  }
  // 未被确认且超时 → 直接判定丢失重发，无需猜测新旧
}
send(101, 1200);
```
