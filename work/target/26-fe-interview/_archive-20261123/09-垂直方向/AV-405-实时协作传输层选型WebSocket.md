---
title: [AV-405] 实时协作传输层选型：WebSocket vs WebRTC DataChannel
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-405：实时协作传输层选型：WebSocket vs WebRTC DataChannel

**答**：
- WS：服务器中转、可靠有序、扩展简单——默认选型。
- DataChannel：P2P 低延迟（<50ms）、可配置不可达/无序——游戏/笔迹高频流。
- 混合：控制消息 WS，高频流 DataChannel（同一会话双通道）。

```javascript
// 双通道协作
class DualChannel {
  constructor(ws, dc) { this.ws = ws; this.dc = dc; }
  send(msg) {
    if (msg.kind === 'cursor' || msg.kind === 'stroke-partial')
      this.dc.send(JSON.stringify(msg));               // 低延迟不可达
    else this.ws.send(JSON.stringify(msg));            // 可靠有序
  }
}
// DataChannel 配置：{ ordered: false, maxRetransmits: 0 }（不可达模式）
```
