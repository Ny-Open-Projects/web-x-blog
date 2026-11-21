---
title: [DP-298] 笔试题：手写埋点 SDK 核心（批量/采样/页面离开兜底）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-298：笔试题：手写埋点 SDK 核心（批量/采样/页面离开兜底）？
**题目**：实现 Tracker：1) track(event, props) 入队；2) 批量上报（50 条或 5s）；3) 采样率配置（track 按比例丢弃，pv 全量）；4) visibilitychange/pagehide 时 sendBeacon 兜底不丢数据；5) 失败重试进本地缓存。
**评分点**：
- 批量触发条件正确（任一满足）。
- 采样决策点在入队前（省内存），pv 豁免。
- pagehide + sendBeacon（而非 unload + fetch）。
- 失败落 localStorage，下次启动重放。
```javascript
class Tracker {
  #queue = [];
  #timer = null;
  constructor({ endpoint, sampleRate = 1 }) {
    this.endpoint = endpoint; this.sampleRate = sampleRate;
    document.addEventListener('visibilitychange', () => document.visibilityState === 'hidden' && this.#flush(true));
    addEventListener('pagehide', () => this.#flush(true));
    this.#replayLocal();                                 // 5) 启动重放
  }
  track(event, props = {}) {
    if (event !== 'pv' && Math.random() > this.sampleRate) return;  // 3) 采样决策
    this.#queue.push({ event, props, ts: Date.now(), sid: sessionId() });
    if (this.#queue.length >= 50) return this.#flush();             // 2) 数量触发
    this.#timer ??= setTimeout(() => this.#flush(), 5000);          // 时间触发
  }
  #flush(beacon = false) {
    if (!this.#queue.length) return;
    clearTimeout(this.#timer); this.#timer = null;
    const batch = this.#queue.splice(0);
    if (beacon && navigator.sendBeacon) { navigator.sendBeacon(this.endpoint, JSON.stringify(batch)); return; }
    fetch(this.endpoint, { method: 'POST', body: JSON.stringify(batch), keepalive: true })
      .catch(() => this.#saveLocal(batch));              // 失败落盘
  }
  #saveLocal(batch) { const prev = JSON.parse(localStorage.getItem('__track_retry') ?? '[]');
    localStorage.setItem('__track_retry', JSON.stringify(prev.concat(batch).slice(-200))); }
  #replayLocal() { const saved = localStorage.getItem('__track_retry');
    if (saved) { navigator.sendBeacon?.(this.endpoint, saved); localStorage.removeItem('__track_retry'); } }
}
```
