---
title: [WEB-283] QUIC 的 QPACK 头压缩与 HTTP/2 的 HPACK 有什么区别？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP3]
type: 面试题
---

## WEB-283：QUIC 的 QPACK 头压缩与 HTTP/2 的 HPACK 有什么区别？
**答**：
- HPACK 依赖单一编码流的顺序解码，HTTP/2 里一个包丢失会阻塞后续所有头解码（队头阻塞）；QPACK 引入独立的通知机制，允许流乱序到达后再解码。
- QPACK 把"动态表更新"和"头数据"拆到不同的控制流上，编码器可等对端确认后再用该条目，用一点压缩率换乱序可用。
- 面试落点：能讲清"为什么换了协议还要重新设计头压缩"——根因都是解决 TCP 层队头阻塞的连带问题。

```javascript
// QPACK 的取舍（示意）：动态表条目必须先被"确认"才能引用
// 编码器流（单向）：发送新增/删除动态表条目的指令
// 请求流头数据：引用动态表时带上 Referenced-Entry-Count
// 解码器流（单向）：回复 Section Acknowledgment 确认解码完成
// 若流 P1 丢失，P2 的头可以先缓存，等 P1 到达且动态表同步后再解码
const h3Headers = [
  [':method', 'GET'],
  [':path', '/api/goods'],
  ['user-agent', 'Chrome/120'], // 高频头：大概率命中动态表
];
console.log('QPACK = HPACK 思想 + 流级解耦，避免头解码依赖单一字节流');
```
