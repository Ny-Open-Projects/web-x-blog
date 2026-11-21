---
title: [WEB-284] QUIC 的流和 HTTP/2 的多路复用本质区别是什么？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP3]
type: 面试题
---

## WEB-284：QUIC 的流和 HTTP/2 的多路复用本质区别是什么？
**答**：
- HTTP/2 的所有流复用同一条 TCP 字节流，任何 segment 丢包，TCP 层会卡住后面所有流的数据交付（传输层队头阻塞）。
- QUIC 的流是独立交付单元：流 A 丢包只重传/阻塞流 A，流 B 的数据照常递交给应用。
- 代价：QUIC 需要在用户态自己实现可靠传输、流控与拥塞控制，CPU 开销高于内核态 TCP。

```javascript
// HTTP/2: stream1 的第3个帧丢了 → TCP 缓冲区卡住 → stream2 的帧已到达也无法上交
// QUIC: 每条流独立维护"已连续收到的最大偏移"
const quicStream = (streamId) => {
  const received = new Set();
  let next = 0;
  return {
    onChunk(offset, data) {
      received.add(offset);
      // 只推进本流的交付指针，其他流不受影响
      while (received.has(next)) next += data.length;
      console.log('stream', streamId, '可交付到字节', next);
    },
  };
};
console.log('流级独立 = QUIC 解决队头阻塞的核心');
```
