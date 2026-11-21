---
title: [ALG-191] WebSocket 长连接在弱网下会"半开"（TCP 未断但收不到数据）。如何用心跳检测发现死链，并用指数退避做断线重连？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-191：WebSocket 长连接在弱网下会"半开"（TCP 未断但收不到数据）。如何用心跳检测发现死链，并用指数退避做断线重连？
**答**：心跳：固定间隔发 `ping`，把 `alive` 标记置 false；收到 `pong` 时置 true——下个周期发现仍是 false 说明一个完整周期没响应，主动 close 触发重连（半开链路只有靠应用层心跳发现）。重连：指数退避 `1s × 2^n` 封顶 30s 加随机抖动（防服务端恢复瞬间被重连潮打挂，即惊群）；连接成功重置计数。onclose 统一驱动重连，onopen 里重新启动心跳。

```javascript
class HeartbeatWS {
  constructor(url) { this.url = url; this.retries = 0; this.connect(); }
  connect() {
    this.ws = new WebSocket(this.url);
    this.ws.onopen = () => { this.retries = 0; this.heartbeat(); }; // 成功重置退避
    this.ws.onmessage = e => { if (e.data === 'pong') this.alive = true; };
    this.ws.onclose = () => this.reconnect();   // 主动 close 也走这里
  }
  heartbeat() {
    this.alive = true;
    clearInterval(this.timer);
    this.timer = setInterval(() => {
      if (this.alive === false) return this.ws.close(); // 一整个周期无 pong：判死
      this.alive = false;
      this.ws.send('ping');                   // 应用层心跳：唯一能发现半开链路
    }, 5000);
  }
  reconnect() {
    clearInterval(this.timer);
    // 指数退避 + 抖动：1s 2s 4s ... 30s 封顶，防重连潮惊群
    const delay = Math.min(30000, 1000 * 2 ** this.retries++) + Math.random() * 500;
    setTimeout(() => this.connect(), delay);
  }
}
```
