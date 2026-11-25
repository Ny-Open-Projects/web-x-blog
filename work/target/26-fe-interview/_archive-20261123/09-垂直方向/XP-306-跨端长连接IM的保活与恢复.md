---
title: [XP-306] 跨端长连接（IM）的保活与恢复
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-306：跨端长连接（IM）的保活与恢复

**答**：
- 保活：前台心跳 30s、后台（App 切后台）降频或断开（系统杀连接）、回到前台立即重连。
- 消息恢复：断线期间消息通过 seq 拉增量（服务端保留窗口）。
- 度量：重连成功率、恢复延迟（回前台到消息就绪）。

```javascript
// IM 保活
class KeepAliveWS {
  constructor(ws, { fg = 30_000, bg = 120_000 } = {}) {
    this.fg = fg; this.bg = bg; this.state = 'fg';
    document.addEventListener('visibilitychange', () =>
      this.state = document.hidden ? 'bg' : 'fg');
    setInterval(() => this.ping(), 1000);
  }
  ping() {
    const interval = this.state === 'fg' ? this.fg : this.bg;
    if (Date.now() - this._last < interval) return;
    this._last = Date.now();
    if (this.ws.readyState === 1) this.ws.send('ping');
    else reconnectWithBackoff();
  }
}
function reconnectWithBackoff() { /* 1s/2s/4s... */ }
```
