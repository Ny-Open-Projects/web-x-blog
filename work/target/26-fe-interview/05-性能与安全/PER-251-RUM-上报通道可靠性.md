---
title: [PER-251] RUM 上报在页面卸载/弱网/隐私模式下会丢数，怎么设计可靠的采集通道？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-251：RUM 上报在页面卸载/弱网/隐私模式下会丢数，怎么设计可靠的采集通道？

**答**：
- 卸载丢数是最常见损失（性能数据恰恰在离开页面时最完整）。方案：`sendBeacon`（浏览器保证后台续传）为主；不支持时降级 `fetch keepalive: true`；再降级同步 XHR（最后手段，阻塞卸载要慎用）。上报时机绑 `visibilitychange(hidden)` + `pagehide`，不用 unload。
- 弱网丢数：批量压缩（gzip/分片）、失败静默放弃（性能数据允许丢，别为重试引入复杂性）、上报体积上限（beacon 64KB）。
- 隐私模式限制：Safari 隐私模式 localStorage 不可用、部分 API 受限——SDK 所有存储访问包 try-catch，内存降级兜底。
- 防重与去重：sessionId + 序号幂等键，服务端按键去重；重复上报（bfcache 恢复后重复 flush）不会虚增样本。

```javascript
class RUMChannel {
  constructor(url) { this.url = url; this.buf = []; this.seq = 0; this.sid = this._sid(); }
  send(metric) {
    this.buf.push({ ...metric, sid: this.sid, seq: ++this.seq, page: routeTemplate(location.pathname) });
    if (this.buf.length >= 20) this.flush();
  }
  flush() {
    if (!this.buf.length) return;
    const body = JSON.stringify(this.buf); this.buf = [];
    if (navigator.sendBeacon?.(this.url, body)) return;        // 1. beacon
    fetch(this.url, { method: 'POST', body, keepalive: true }).catch(() => {}); // 2. keepalive
  }
  _sid() { try { const k = 'rum_sid';
      return localStorage.getItem(k) || (localStorage.setItem(k, crypto.randomUUID()), localStorage.getItem(k));
    } catch { return crypto.randomUUID(); } }                  // 隐私模式降级内存 id
}
document.addEventListener('visibilitychange', () => document.visibilityState === 'hidden' && rum.flush());
addEventListener('pagehide', () => rum.flush());               // 不用 unload
```
