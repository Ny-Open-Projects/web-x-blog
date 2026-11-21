---
title: [WEB-286] QUIC 的 ACK 机制和 TCP 确认有什么区别？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP3]
type: 面试题
---

## WEB-286：QUIC 的 ACK 机制和 TCP 确认有什么区别？
**答**：
- TCP 只有累计确认（SACK 是补丁）；QUIC 每个包带唯一包号（单调递增，永不复用），ACK 帧直接携带 ACK Range 列表，精确到包。
- QUIC ACK 里还带 ECT/ECN 支持和应答延迟信息，便于发送端做更准确的 RTT 估计。
- 包号不复用也让"丢包"和"重传"在协议层天然可区分，RTT 测量更准。

```javascript
// QUIC ACK 帧示意： Largest Acknowledged + ACK Range 列表
const ackFrame = {
  largest: 120,          // 收到的最大包号
  ackDelay: 15,          // 应答延迟 ms，供 RTT 校正
  ranges: [[115, 120], [113, 113], [100, 105]], // 不连续区间
};
const isAcked = n => ackFrame.ranges.some(([lo, hi]) => n >= lo && n <= hi);
console.log('包114是否已确认:', isAcked(114), '包106:', isAcked(106));
```
