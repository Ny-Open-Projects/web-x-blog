---
title: [WCN-619] 笔试：实现元素库的 INP 采样与归因打点器（事件延迟采集 + 归因到组件）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-619：笔试：实现元素库的 INP 采样与归因打点器（事件延迟采集 + 归因到组件）

**答**：
- 需求：实现 INPTracker，监听 pointerdown/keydown 计算事件处理到下一帧渲染的延迟，归因到触发的 WC 标签，超阈值上报。
- 思路：用事件时间戳记录 startTime，requestAnimationFrame 两帧后算 duration；取 P75 作为 INP；用 event.composedPath() 找到最近的自定义元素做归因。
- 边界：只统计用户交互事件；防止同一次交互重复计时；采样率控制数据量。

```javascript
class INPTracker {
  constructor(threshold = 200, sample = 0.1) {
    this.samples = []; this.pending = null;
    this.threshold = threshold; this.sample = sample;
  }
  start() {
    ['pointerdown', 'keydown'].forEach(type =>
      document.addEventListener(type, e => this.onEvent(e), true));
  }
  onEvent(e) {
    if (Math.random() > this.sample || this.pending) return;
    this.pending = { t: e.timeStamp, target: this.closestWC(e) };
    requestAnimationFrame(() => requestAnimationFrame(() => {
      const d = performance.now() - this.pending.t;
      this.samples.push({ d, wc: this.pending.target });
      if (d > this.threshold) this.report(this.pending.target, d);
      this.pending = null;
    }));
  }
  closestWC(e) {
    return e.composedPath().find(n => n.nodeName?.includes('-'))?.nodeName || 'unknown';
  }
  report(wc, d) { console.warn('[INP]', wc, d.toFixed(1), 'ms'); }
}
new INPTracker().start();
```

**评分点**：
- 用 composedPath 穿透 Shadow DOM 归因到自定义元素。
- 双 rAF 计算到下一帧的真实交互延迟（而非仅同步耗时）。
- 采样率 + 防重复计时，避免数据爆炸与统计失真。
- 超阈值上报带组件标签，可直接定位责任组件。
