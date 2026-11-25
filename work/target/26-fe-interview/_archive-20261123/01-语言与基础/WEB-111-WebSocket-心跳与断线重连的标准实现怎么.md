---
title: [WEB-111] WebSocket 心跳与断线重连的标准实现怎么做？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-111：WebSocket 心跳与断线重连的标准实现怎么做？
**答**：
- 两层心跳：协议层 ping/pong 帧由库/代理处理；应用层心跳更常用——客户端定时发 ping 消息，超时未收到 pong 判定死链主动 close，同时防止中间代理因空闲超时掐断连接。
- 重连采用指数退避 + 抖动，避免服务端故障恢复瞬间被重连风暴打垮；成功后重置退避。
- 消息不丢：重连期间消息进队列，重连成功后按序补发，必要时用序号去重。
- 页面隐藏时（visibilitychange）可暂停心跳省流量，恢复可见时立即探测。

```javascript
class ReconnectingWebSocket {
  constructor(url) {
    this.url = url;
    this.queue = [];          // 断线期间的待发消息
    this.retry = 1000;        // 退避基数
    this.connect();
  }
  connect() {
    this.ws = new WebSocket(this.url);
    this.ws.onopen = () => {
      this.retry = 1000;                      // 成功后重置退避
      this.alive = true;
      this.startHeartbeat();
      while (this.queue.length) this.ws.send(this.queue.shift()); // 补发积压
    };
    this.ws.onmessage = (e) => {
      if (e.data === 'pong') { this.alive = true; return; }
      this.onmessage?.(e);
    };
    this.ws.onclose = () => this.scheduleReconnect();
    this.ws.onerror = () => this.ws.close();
  }
  startHeartbeat() {
    clearInterval(this.timer);
    this.timer = setInterval(() => {
      if (!this.alive) return this.ws.close(); // 上一轮 pong 未回，判死重连
      this.alive = false;
      this.ws.send('ping');
    }, 15000);
  }
  scheduleReconnect() {
    clearInterval(this.timer);
    const delay = this.retry + Math.random() * 500; // 指数退避 + 抖动
    this.retry = Math.min(this.retry * 2, 30000);
    setTimeout(() => this.connect(), delay);
  }
  send(msg) {
    if (this.ws.readyState === WebSocket.OPEN) this.ws.send(msg);
    else this.queue.push(msg);                // 未连接先进队列
  }
}
```
