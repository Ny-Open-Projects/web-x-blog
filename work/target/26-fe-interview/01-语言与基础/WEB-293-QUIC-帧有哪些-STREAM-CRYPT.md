---
title: [WEB-293] QUIC 帧有哪些？STREAM、CRYPTO、ACK 各自负责什么？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP3]
type: 面试题
---

## WEB-293：QUIC 帧有哪些？STREAM、CRYPTO、ACK 各自负责什么？
**答**：
- 帧是 QUIC 包内的最小单元：STREAM 帧载应用数据，CRYPTO 帧载 TLS 握手，ACK 帧确认收包。
- 连接控制类：PING（保活/RTT）、PATH_CHALLENGE/RESPONSE（迁移验证）、NEW_CONNECTION_ID（迁移备选）、CONNECTION_CLOSE。
- 流控类：MAX_DATA / MAX_STREAM_DATA / DATA_BLOCKED，类似 HTTP/2 WINDOW_UPDATE 的角色。

```javascript
// 一个 QUIC 包可携带多个帧
const packet = {
  header: { dcid: 'ab12', pn: 42 },
  frames: [
    { type: 'ACK', largest: 40 },
    { type: 'STREAM', sid: 0, offset: 1024, data: '...' },
    { type: 'MAX_DATA', max: 1048576 },      // 提升连接级流控窗口
  ],
};
console.log(packet.frames.map(f => f.type).join(' / '));
```
