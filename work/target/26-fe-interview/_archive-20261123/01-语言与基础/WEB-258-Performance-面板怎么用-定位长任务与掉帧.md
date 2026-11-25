---
title: [WEB-258] Performance 面板怎么用？定位长任务与掉帧
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 排查]
type: 面试题
---

## WEB-258：Performance 面板怎么用？定位长任务与掉帧

**答**：
- 流程：录 5 秒交互 → 看 FPS 轨道（掉帧区间）→ Frame 图红色块 → 定位对应 Main 线程火焰图 → 自底向上看谁占时最长。
- 长任务：Main 轨道 >50ms 的任务会被标红旗（Long Task），展开看是脚本执行、样式重算（紫色 Recalculate Style）、布局（Layout/强制同步 reflow）还是 GC。
- 常见结论对应：红色火焰深=JS 太重（拆分/算法）；Layout 频繁=布局抖动（读 offsets 与写样式交替）；GC 频繁=临时对象过多。
- 辅助工具：`PerformanceObserver('longtask')` 线上采集；Coverage 面板看死代码；Memory 面板抓堆快照查泄漏。
- 真机注意：DevTools 在开发者机器上跑，低端手机要配合 CPU 4x slowdown 模拟。

```javascript
// 线上长任务采集
new PerformanceObserver((list) => {
  for (const t of list.getEntries()) {
    navigator.sendBeacon('/perf/longtask', JSON.stringify({
      dur: t.duration, name: t.name, ts: t.startTime,
    }));
  }
}).observe({ type: 'longtask', buffered: true });
```
