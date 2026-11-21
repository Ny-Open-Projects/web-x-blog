---
title: [ARC-404] 笔试题：手写埋点 SDK 的上报队列与重试
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-404：笔试题：手写埋点 SDK 的上报队列与重试
**题目**：实现 Tracker：1) track(event) 入队；2) 队列满 N 条或定时 T 秒批量 flush；3) 上报失败指数退避重试最多 3 次；4) 页面卸载时用 sendBeacon 兜底不丢数据。
**评分点**：
- 批量合并与触发条件（数量阈值 + 时间窗双触发）。
- 指数退避正确（1s/2s/4s）且重试期间不阻塞新入队。
- unload 兜底 sendBeacon（异步不阻断关闭）。
- 队列上限防内存膨胀（满了丢弃最旧或立即 flush）。
```javascript
class Tracker {
  #queue = []; #retry = 0; #timer = null;
  constructor(private url: string, private max = 20, private flushMs = 5000) {
    addEventListener('pagehide', () => this.#beacon());           // 卸载兜底
    this.#timer = setTimeout(() => this.flush(), this.flushMs);
  }
  track(event) {
    this.#queue.push({ ...event, ts: Date.now() });
    if (this.#queue.length >= this.max) this.flush(); else this.#schedule();
  }
  async flush() {
    if (!this.#queue.length) return;
    const batch = this.#queue.splice(0, this.max);                // 取走一批
    try {
      await fetch(this.url, { method: 'POST', body: JSON.stringify(batch), keepalive: true });
      this.#retry = 0;
    } catch {
      if (++this.#retry <= 3) {
        setTimeout(() => { this.#queue.unshift(...batch); this.flush(); },
          2 ** this.#retry * 500);                                // 1s/2s/4s 退避
      }                                                          // 3 次失败丢批（埋点允许）
    }
  }
  #beacon() { if (this.#queue.length) navigator.sendBeacon(this.url, JSON.stringify(this.#queue)); }
  #schedule() { clearTimeout(this.#timer); this.#timer = setTimeout(() => this.flush(), this.flushMs); }
}
```
