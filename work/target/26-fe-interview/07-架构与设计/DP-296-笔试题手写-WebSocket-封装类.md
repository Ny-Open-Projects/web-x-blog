---
title: [DP-296] 笔试题：手写 WebSocket 封装（重连/心跳/消息队列）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-296：笔试题：手写 WebSocket 封装（重连/心跳/消息队列）？
**题目**：实现 WsClient 类：1) 自动重连（指数退避+抖动，上限次数）；2) 心跳（ping/pong 超时判死）；3) 断线期间 send 入队，重连后 flush；4) on(event) 业务事件订阅；5) destroy 完整清理。
**评分点**：
- 退避+抖动公式正确（防重连风暴）。
- 心跳超时判死主动 close（不依赖 close 事件）。
- 队列 flush 时机正确（open 后按序发送）。
- destroy 清理定时器/监听/队列。
```javascript
class WsClient {
  #ws; #queue = []; #subs = new Map(); #attempt = 0; #timers = [];
  constructor(private url, private opts = { maxRetries: 10, heartbeat: 25000 }) {}
  connect() {
    this.#ws = new WebSocket(this.url);
    this.#ws.onopen = () => { this.#attempt = 0; this.#flush(); this.#heartbeat(); };
    this.#ws.onmessage = ({ data }) => { const m = JSON.parse(data); this.#subs.get(m.type)?.forEach(f => f(m)); };
    this.#ws.onclose = () => this.#reconnect();
  }
  #reconnect() {
    this.#clearTimers();
    if (this.#attempt++ >= this.opts.maxRetries) return this.#subs.get('dead')?.forEach(f => f());
    const delay = Math.min(500 * 2 ** this.#attempt, 30000) * (0.7 + Math.random() * 0.6);  // 1) 退避+抖动
    this.#timers.push(setTimeout(() => this.connect(), delay));
  }
  #heartbeat() {
    const t = setInterval(() => { this.send({ type: 'ping' });
      const dead = setTimeout(() => this.#ws.close(), 5000);   // 2) 超时判死
      this.#timers.push(dead);
      this.#ws.addEventListener('message', function once({ data }) { if (JSON.parse(data).type === 'pong') clearTimeout(dead); }, { once: true });
    }, this.opts.heartbeat);
    this.#timers.push(t);
  }
  send(msg) { this.#ws.readyState === 1 ? this.#ws.send(JSON.stringify(msg)) : this.#queue.push(msg); }  // 3)
  #flush() { this.#queue.splice(0).forEach(m => this.#ws.send(JSON.stringify(m))); }
  on(type, fn) { this.#subs.get(type) ?? this.#subs.set(type, new Set()).get(type).add(fn);
    return () => this.#subs.get(type)?.delete(fn); }
  destroy() { this.#clearTimers(); this.#ws?.close(); this.#queue = []; this.#subs.clear(); }  // 5)
  #clearTimers() { this.#timers.splice(0).forEach(clearTimeout); }
}
```
