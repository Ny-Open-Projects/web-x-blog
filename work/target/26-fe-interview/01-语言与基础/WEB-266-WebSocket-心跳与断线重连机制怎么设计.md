---
title: [WEB-266] WebSocket 心跳与断线重连机制怎么设计？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, WebSocket]
type: 面试题
---

## WEB-266：WebSocket 心跳与断线重连机制怎么设计？

**答**：
- 为什么心跳：TCP 半开连接（NAT 超时、网络切换）浏览器不感知，不心跳就是「假在线」，发消息永远不达。
- 心跳设计：客户端定时发 ping，N 秒内没收到 pong 判定断开 → 主动 close 触发重连；间隔 < NAT 超时（通常 30~60s 内）。
- 重连策略：指数退避 + 抖动（1s、2s、4s...上限 30s），防止服务重启时全量客户端同时重连压垮（惊群）；达到上限后进入可见性驱动的惰性重连。
- 体验细节：连接状态暴露给 UI（在线/重连中/离线）；重连成功后拉取离线期间的增量消息（sequence id 续传）。

```javascript
class ReconnectingWS {
  constructor(url) { this.url = url; this.retry = 0; this.connect(); }
  connect() {
    this.ws = new WebSocket(this.url);
    this.ws.onopen = () => { this.retry = 0; this.startPing(); };
    this.ws.onmessage = (e) => {
      if (e.data === 'pong') clearTimeout(this.pongTimer);
      this.onmessage?.(e);
    };
    this.ws.onclose = () => {
      this.stopPing();
      const delay = Math.min(30000, 1000 * 2 ** this.retry++) + Math.random() * 1000;
      this.timer = setTimeout(() => this.connect(), delay); // 退避+抖动
    };
  }
  startPing() {
    this.pingTimer = setInterval(() => {
      this.ws.send('ping');
      this.pongTimer = setTimeout(() => this.ws.close(), 5000); // 5s 无 pong 判死
    }, 20000);
  }
}
```

**评分点**：
- 说明心跳目的（检测半开连接）
- 重连用指数退避 + 抖动，提到防惊群
- pong 超时主动断开而非干等 onclose
