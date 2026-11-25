---
title: [WEB-573] 笔试：手写 WebTransport 双通道消息管理器
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, 网络]
type: 笔试题
---

## WEB-573：笔试：手写 WebTransport 双通道消息管理器

**答**：实现 `WtChannel`：① 连接 WebTransport，ready 超时 3s 触发 WebSocket 降级回调 `onFallback`；② `send(msg, { reliable })`：reliable=true 走新建 bidirectional stream，否则走 datagram；③ datagram 发送失败静默丢弃（低价值消息），stream 发送失败重试 1 次；④ 连接 closed 时自动重连一次并重放 reliable 队列中的未确认消息。

```javascript
const enc = new TextEncoder();

class WtChannel {
  constructor(url, { onFallback } = {}) {
    this.url = url; this.onFallback = onFallback;
    this.pending = []; // reliable 未确认队列
    this._connect();
  }
  async _connect() {
    const wt = new WebTransport(this.url);
    const timeout = new Promise((_, rj) => setTimeout(() => rj(new Error('wt-timeout')), 3000));
    try { await Promise.race([wt.ready, timeout]); this.wt = wt; this._listen(); }
    catch { this.onFallback?.(); }
  }
  _listen() {
    this.wt.closed.then(() => this._reconnect()).catch(() => this._reconnect());
  }
  async _reconnect() {
    if (this.reconnecting) return;
    this.reconnecting = true;
    await this._connect();
    this.reconnecting = false;
    for (const msg of this.pending.splice(0)) this.send(msg, { reliable: true });
  }
  async send(msg, { reliable = true } = {}) {
    const bytes = enc.encode(JSON.stringify(msg));
    if (!this.wt) return;
    if (!reliable) {
      try { await this.wt.datagrams.writable.getWriter().write(bytes); } catch {} // 允许丢
      return;
    }
    this.pending.push(msg);
    try {
      const s = await this.wt.createBidirectionalStream();
      await s.writable.getWriter().write(bytes);
      this.pending = this.pending.filter(m => m !== msg); // 确认后出队
    } catch {
      if (!this._retried(msg)) { this._markRetry(msg); return this.send(msg, { reliable: true }); }
    }
  }
  _retried(m) { return m.__r; }
  _markRetry(m) { m.__r = true; }
}
```

**评分点**：
- ready 超时竞速实现降级触发，理解 WebTransport 依赖 h3 可用
- reliable/unreliable 双通道语义区分（stream vs datagram）
- reliable 消息未确认重放队列 + 重连后重放
- 重试与重连都有上限/去重，避免雪崩
