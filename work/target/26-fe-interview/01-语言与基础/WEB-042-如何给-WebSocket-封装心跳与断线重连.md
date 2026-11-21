---
title: [WEB-042] 如何给 WebSocket 封装心跳与断线重连？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-042：如何给 WebSocket 封装心跳与断线重连？
**答**：
- 心跳：定时发 ping，超时未收到 pong 判定连接已死，主动 close 触发重连。
- 重连要指数退避 + 抖动，避免服务端恢复瞬间被重连风暴打死。
- 代码要处理"重复连接"、连接期间调用 send 的排队、页面卸载时主动断开等边界。
- 面试时说清"为什么要心跳"：TCP 半打开连接不会主动通知应用层，只能靠应用层探测。

```javascript
// 生产级 WebSocket 客户端封装：心跳 + 指数退避重连
class ReconnectingWS {
  constructor(url) {
    this.url = url;
    this.retry = 0;
    this.heartbeatInterval = 30000;
    this.connect();
  }
  connect() {
    if (this.socket) this.socket.close();
    this.socket = new WebSocket(this.url);

    this.socket.addEventListener('open', () => {
      this.retry = 0; // 重置退避
      this.startHeartbeat();
    });
    this.socket.addEventListener('message', (e) => {
      const msg = JSON.parse(e.data);
      if (msg.type === 'pong') this.gotPong = true;
      this.onMessage?.(msg);
    });
    this.socket.addEventListener('close', () => {
      this.stopHeartbeat();
      this.scheduleReconnect();
    });
    this.socket.addEventListener('error', () => this.socket.close());
  }
  startHeartbeat() {
    this.stopHeartbeat();
    this.heartbeatTimer = setInterval(() => {
      this.gotPong = false;
      this.send({ type: 'ping', ts: Date.now() });
      // 一个心跳周期内没收到 pong 视为死连接
      setTimeout(() => {
        if (!this.gotPong && this.socket.readyState === WebSocket.OPEN) {
          this.socket.close(); // close 事件会触发重连
        }
      }, 5000);
    }, this.heartbeatInterval);
  }
  stopHeartbeat() {
    clearInterval(this.heartbeatTimer);
  }
  scheduleReconnect() {
    const delay = Math.min(30000, 1000 * 2 ** this.retry) + Math.random() * 500; // 退避 + 抖动
    this.retry += 1;
    console.log(`reconnect in ${Math.round(delay)}ms, attempt=${this.retry}`);
    setTimeout(() => this.connect(), delay);
  }
  send(data) {
    if (this.socket.readyState === WebSocket.OPEN) {
      this.socket.send(JSON.stringify(data));
    }
  }
  destroy() {
    this.stopHeartbeat();
    this.socket.close(); // 页面卸载时主动断开，不再重连
    this.socket.onclose = null;
  }
}

const client = new ReconnectingWS('wss://api.example.com/ws');
client.onMessage = (msg) => console.log(msg);
```
