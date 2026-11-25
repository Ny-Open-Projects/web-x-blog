---
title: [AV-208] WebRTC 数据通道 DataChannel：可靠性与有序性配置
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-208：WebRTC 数据通道 DataChannel：可靠性与有序性配置

**答**：
- DataChannel 两种模式：可靠有序（类 TCP，默认）与不可靠无序（maxRetransmits/maxPacketLifeTime，类 UDP）。
- 选型：信令/状态同步 → 可靠有序；游戏状态/实时弹幕 → 不可靠（旧消息丢弃优于堆积）。
- SCTP 分片：大消息（>16KB）自动分片但会阻塞——大文件走分块+流控。

```javascript
const dc = pc.createDataChannel('game', {
  ordered: false,                                          // 无序
  maxRetransmits: 0,                                       // 不重传（类 UDP）
});
dc.onmessage = (e) => handleGameEvent(JSON.parse(e.data));
// 可靠通道（信令）：默认参数即可
const signaling = pc.createDataChannel('signaling');
// 大文件传输：分块 + 流控（bufferedAmount 高水位）
function sendFile(dc, file) {
  const CHUNK = 16 * 1024;
  let offset = 0;
  const pump = () => {
    while (dc.bufferedAmount < 1 << 20 && offset < file.size) {   // 高水位 1MB
      dc.send(file.slice(offset, offset + CHUNK));
      offset += CHUNK;
    }
    if (offset < file.size) setTimeout(pump, 10);           // 低水位再续
  };
  pump();
}
```
