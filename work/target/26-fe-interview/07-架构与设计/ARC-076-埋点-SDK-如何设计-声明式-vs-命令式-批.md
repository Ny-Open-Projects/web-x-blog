---
title: [ARC-076] 埋点 SDK 如何设计（声明式 vs 命令式、批量上报、采样）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-076：埋点 SDK 如何设计（声明式 vs 命令式、批量上报、采样）？
**答**：
- 命令式（`track('buy_click', {...})`）灵活但侵入业务；声明式（`data-track` 属性/组件包裹）由 SDK 统一代理捕获，业务零侵入。
- 架构选型通常是"声明式为主、命令式兜底"：80% 常规事件走 DOM 代理，复杂事件显式调用。
- 批量上报（攒批 + 页面卸载 flush）与采样分级（PV 全量、点击 100%、滚动类 10%）控制成本。

```typescript
// 声明式埋点：DOM 代理统一捕获，业务侧零侵入
// <button data-track='{"event":"buy_click","sku":"123"}'>购买</button>
export function installDeclarativeTracking(track: TrackFn) {
  document.addEventListener('click', (e) => {
    const el = (e.target as HTMLElement).closest('[data-track]');
    if (!el) return;
    try { track(JSON.parse(el.getAttribute('data-track')!)); } catch { /* 静默 */ }
  }, { capture: true });                       // capture 保证被 stopPropagation 的按钮也能埋到
}

// 埋点队列：批量 + 卸载兜底
class Tracker {
  private queue: TrackEvent[] = [];
  track(e: TrackEvent) {
    this.queue.push({ ...e, ts: Date.now() });
    if (this.queue.length >= 20) this.flush();
  }
  flush = () => {
    if (!this.queue.length) return;
    navigator.sendBeacon('/collect', JSON.stringify(this.queue));
    this.queue = [];
  };
  constructor() { addEventListener('pagehide', this.flush); }  // visibilitychange/pagehide 而非 unload
}
// 采样策略：PV 全量；点击 100%；曝光 20%；滚动/停留时长 5%
```
