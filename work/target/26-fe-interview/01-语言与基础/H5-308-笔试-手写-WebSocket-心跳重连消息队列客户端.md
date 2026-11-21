---
title: [H5-308] 笔试：手写 WebSocket 心跳+重连+消息队列客户端
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 笔试题, WebSocket]
type: 笔试题
---

## H5-308：笔试：手写 WebSocket 心跳+重连+消息队列客户端

**题目**：实现完整 WS 客户端类 `RobustWS(url, handlers)`：心跳 30s（5s 无 PONG 判半开）、断线指数退避重连（上限 30s，带抖动）、离线消息入队恢复后补发、手动 close 后不再重连、最多重试 5 次后进入失败态并回调 onError。

**答**：
```javascript
class RobustWS {
  constructor(url, handlers = {}) {
    this.url = url; this.handlers = handlers;
    this.stopped = false; this.retry = 0; this.queue = [];
    this.#connect();
  }
  #connect() {
    this.ws = new WebSocket(this.url);
    this.ws.onopen = () => {
      this.retry = 0;
      this.#heartbeat();
      this.queue.splice(0).forEach(m => this.#raw(m)); // 补发
    };
    this.ws.onmessage = (e) => {
      const m = JSON.parse(e.data);
      if (m.type === 'PONG') { clearTimeout(this.pongTimer); return; }
      this.handlers.onMessage?.(m);
    };
    this.ws.onclose = () => {
      clearInterval(this.pingTimer); clearTimeout(this.pongTimer);
      if (this.stopped) return;
      if (++this.retry > 5) return this.handlers.onError?.('exceeded retries');
      const delay = Math.min(30000, 1000 * 2 ** (this.retry - 1)) + Math.random() * 1000;
      this.reconnectTimer = setTimeout(() => this.#connect(), delay);
    };
  }
  #heartbeat() {
    this.pingTimer = setInterval(() => {
      this.#raw({ type: 'PING' });
      this.pongTimer = setTimeout(() => this.ws.close(), 5000); // 半开检测
    }, 30000);
  }
  #raw(m) { this.ws.readyState === 1 ? this.ws.send(JSON.stringify(m)) : this.queue.push(m); }
  send(m) { this.#raw(m); }
  close() {
    this.stopped = true;
    clearTimeout(this.reconnectTimer);
    clearInterval(this.pingTimer); clearTimeout(this.pongTimer);
    this.ws?.close();
  }
}
```

**评分点**：
- 三套计时器（心跳/pong 超时/重连）的生命周期管理，onclose 统一清理
- 重试计数在 onopen 重置——恢复后重新计数
- 5 次上限 + onError 回调的失败态出口
- 离线队列在 onopen 补发，send 在 OPEN 检查
