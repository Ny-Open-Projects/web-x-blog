---
title: [WEB-294] QUIC 的流控和 TCP 滑动窗口有什么区别？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP3]
type: 面试题
---

## WEB-294：QUIC 的流控和 TCP 滑动窗口有什么区别？
**答**：
- TCP 只有连接级窗口；QUIC 有流级 + 连接级双层流控，避免一条慢流占满连接窗口拖死其他流。
- 接收端用 MAX_DATA/MAX_STREAM_DATA 主动调窗口，发送端被限流时发 DATA_BLOCKED 便于诊断。
- 调参实践：流窗口太小限制单流吞吐，太大加剧接收缓冲压力；一般流窗口 ≈ BDP（带宽×RTT）。

```javascript
const conn = { maxData: 4 * 1024 * 1024, used: 0, streams: {} };
function onStreamData(conn, sid, len) {
  conn.used += len;
  conn.streams[sid] ??= { max: 512 * 1024, used: 0 };
  conn.streams[sid].used += len;
  if (conn.streams[sid].used > conn.streams[sid].max) return 'BLOCKED';
  if (conn.used > conn.maxData) return 'CONN_BLOCKED';
  return 'OK';
}
console.log(onStreamData(conn, 0, 600 * 1024)); // BLOCKED：流级先卡住
```
