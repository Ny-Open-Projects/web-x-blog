---
title: [OPT-157] SPA 页面常驻不关 tab（数小时/数天），内存如何持续治理？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-157：SPA 页面常驻不关 tab（数小时/数天），内存如何持续治理？

**答**：
- 长驻页面的内存增长源：路由切换不释放的组件缓存、只进不出的数据缓存（消息列表/日志）、事件监听累积、定时器、 detached DOM。
- 治理原则：所有"会增长的结构"必须有上限——消息列表 capped ring buffer（保最近 N 条）、路由级组件缓存 LRU、缓存对象统一走带 TTL 的 Cache 类。
- 建立内存巡检：每 5 分钟采样 `performance.memory.usedJSHeapSize`，连续上升且 GC 后不回落则告警（配合 OPT-162）。
- 验证手段：Chrome DevTools heap snapshot 三快照法 + `allocation timeline` 定位增长点；长会话用 Puppeteer 跑 8 小时回归。

```javascript
// 一一对应：长驻 SPA 的三类内存上限治理
// 1. 消息列表：环形缓冲，只保留最近 500 条
class RingBuffer {
  constructor(limit) { this.limit = limit; this.items = []; }
  push(item) {
    this.items.push(item);
    if (this.items.length > this.limit) this.items.splice(0, this.items.length - this.limit); // 惰性裁剪
  }
  get all() { return this.items; }
}
const msgBuffer = new RingBuffer(500);
ws.onmessage = e => msgBuffer.push(JSON.parse(e.data)); // 挂一天也只占 500 条

// 2. 路由组件缓存：LRU 上限，keep-alive 场景最常用
class LRUCache {
  constructor(max = 10) { this.max = max; this.map = new Map(); } // Map 保序即 LRU
  get(k) { if (!this.map.has(k)) return; const v = this.map.get(k); this.map.delete(k); this.map.set(k, v); return v; }
  set(k, v) {
    if (this.map.has(k)) this.map.delete(k);
    this.map.set(k, v);
    if (this.map.size > this.max) {
      const oldest = this.map.keys().next().value;
      this.map.get(oldest)?.destroy?.();   // 驱逐前先销毁组件（解绑事件/定时器）
      this.map.delete(oldest);
    }
  }
}

// 3. 内存巡检：每 5 分钟采样，连续增长告警
let samples = [];
setInterval(() => {
  const mem = performance.memory;
  if (!mem) return;
  samples.push(mem.usedJSHeapSize);
  if (samples.length > 6) samples.shift();
  const growth = (samples[5] - samples[0]) / samples[0];
  if (growth > 0.3 && samples[5] > 200 * 1024 * 1024) {  // 30 分钟涨 30% 且超 200MB
    reportMemoryIncident(growth, mem);
  }
}, 5 * 60_000);
```
