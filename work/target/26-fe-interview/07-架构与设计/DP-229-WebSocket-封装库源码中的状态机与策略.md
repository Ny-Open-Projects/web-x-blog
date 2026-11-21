---
title: [DP-229] 源码识别：WebSocket 封装库源码中的状态机与策略？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-229：源码识别：WebSocket 封装库源码中的状态机与策略？
**答**:
- 状态模式：CONNECTING/OPEN/CLOSING/CLOSED + 业务态（reconnect-wait/degraded-polling），封装库把裸 WS 三个事件（open/close/message/error）收敛成状态转移。
- 策略：重连策略（次数/退避/抖动）、心跳策略（间隔/超时/pong 校验）、降级策略（WS 失败 → HTTP 轮询）都是注入点。
- 观察者：on(event, handler) 业务事件层（消息类型分发），与底层连接事件分离。
- 识别要点：能指出"消息队列缓冲"——CLOSED 期间 send 的消息入队，重连后 flush（常见封装细节）。

```javascript
// WS 封装状态机（源码级简化）
class WsClient {
  state = 'idle';
  buffer = [];
  constructor({ reconnect: { base = 500, max = 8 }, heartbeat: { interval = 25000 } }) {
    this.reconnectBackoff = a => Math.min(base * 2 ** a, 30_000);   // 策略注入
    this.heartbeatInterval = interval;
  }
  connect() {
    this.state = 'connecting';
    const ws = new WebSocket(this.url);
    ws.onopen = () => { this.state = 'open'; this.startHeartbeat(); this.flush(); };  // 缓冲消息回放
    ws.onmessage = e => this.emitter.emit(parse(e.data).type, parse(e.data));          // 业务观察者
    ws.onclose = () => { this.state = 'reconnect-wait';
      setTimeout(() => this.connect(), this.reconnectBackoff(this.attempt++)); };
  }
  send(msg) {
    if (this.state === 'open') this.ws.send(JSON.stringify(msg));
    else this.buffer.push(msg);                       // CLOSED 期间入队
  }
  startHeartbeat() {
    this.timer = setInterval(() => { this.send({ type: 'ping' });
      setTimeout(() => this.state === 'open' && !this.ponged && this.ws.close(), 5000); // 超时判死
      this.ponged = false; }, this.heartbeatInterval);
  }
}
```
