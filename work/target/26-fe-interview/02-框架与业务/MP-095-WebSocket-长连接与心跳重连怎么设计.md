---
title: [MP-095] WebSocket 长连接与心跳重连怎么设计？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-095：WebSocket 长连接与心跳重连怎么设计？
**答**：
- `wx.connectSocket` 返回 SocketTask（推荐全部走 task 实例）；wx.onSocketOpen 等全局 API 与多连接冲突，避免混用。
- 心跳：定时发 ping，超时未收 pong 判定断线；重连用**指数退避**，切前台 onShow 立即重连、切后台暂停心跳省电。
- 消息可靠性：业务层 seq + ack，重连后补拉增量数据。

```javascript
class WsClient {
  connect() {
    this.task = wx.connectSocket({ url: 'wss://ws.example.com' })
    this.task.onOpen(() => { this.startHeartbeat(); this.resync() })
    this.task.onMessage((e) => this.handle(e.data))
    this.task.onClose(() => this.reconnect())   // 指数退避
  }
  startHeartbeat() {
    this.hbTimer = setInterval(() => this.task.send({ data: 'ping' }), 15000)
  }
  reconnect() {
    clearTimeout(this.hbTimer)
    const delay = Math.min(30000, (this.retry = (this.retry || 0) + 1) * 2000)
    setTimeout(() => this.connect(), delay)
  }
}
```
