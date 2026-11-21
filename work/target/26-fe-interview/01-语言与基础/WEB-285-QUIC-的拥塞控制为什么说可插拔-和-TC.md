---
title: [WEB-285] QUIC 的拥塞控制为什么说可插拔？和 TCP 有什么不同？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP3]
type: 面试题
---

## WEB-285：QUIC 的拥塞控制为什么说可插拔？和 TCP 有什么不同？
**答**：
- TCP 拥塞控制实现在内核里，升级要改操作系统；QUIC 在用户态实现，应用可以按业务选择 CUBIC、BBR 等算法，甚至热更新。
- Google BBR 不把丢包当拥塞信号，而是主动测量瓶颈带宽与 RTT，弱网/高丢包场景吞吐显著更好。
- 前端可感知：弱网图片/视频加载更稳，但不同 CDN 厂商算法不同，表现会有差异。

```javascript
// 用户态插拔拥塞控制（示意）
const ccs = {
  CUBIC: { onLoss: s => (s.cwnd *= 0.7) },                    // 丢包降窗
  BBR:   { onAck: s => { s.btlBw = Math.max(s.btlBw, s.rateSample); s.cwnd = s.btlBw * s.rtt * 2; } },
};
const conn = { cc: 'BBR', cwnd: 10, rtt: 40, btlBw: 100, rateSample: 90 };
const state = { ...conn };
ccs[conn.cc].onAck?.(state);
console.log('BBR 丢包不降窗，按带宽时积控窗:', state.cwnd);
// TCP 想换 BBR：得改内核；QUIC：改配置即可
```
