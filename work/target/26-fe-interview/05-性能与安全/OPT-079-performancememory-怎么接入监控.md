---
title: [OPT-079] performance.memory 怎么接入监控？跨浏览器怎么办？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-079：performance.memory 怎么接入监控？跨浏览器怎么办？

**答**：
- `performance.memory`（Chromium）提供 usedJSHeapSize/totalJSHeapSize/jsHeapSizeLimit，轮询即可得到**堆趋势曲线**，是发现泄漏与 GC 压力最便宜的探针。
- 三个正确姿势：**看趋势不看绝对值**（不同机型 limit 不同）、配合关键操作打标（进入页面/切换路由）、按 `jsHeapSizeLimit` 算内存压力比告警。
- 兼容性：Safari/Firefox 没有；跨浏览器用兜底方案——`console.memory`（仅 DevTools）、`navigator.deviceMemory`（设备档位）、或 PerformanceObserver 的 GC 类目（新 API）。
- 采样别太密：10-30s 一次足够，采样本身也是开销；上报走 idle 档。

```javascript
// 一一对应：堆内存采样 + 压力比告警 + 跨浏览器兜底
function startHeapMonitor({ intervalMs = 15_000, warnRatio = 0.8 } = {}) {
  if (!performance.memory) {
    // Safari/Firefox：降级为设备档位 + 页面存活时长上报，趋势分析换用快照抽查
    navigator.sendBeacon('/api/rum', JSON.stringify({
      metric: 'heap_unavailable',
      deviceMemory: navigator.deviceMemory ?? 'unknown',
    }));
    return () => {};
  }
  const timer = setInterval(() => {
    const { usedJSHeapSize, jsHeapSizeLimit } = performance.memory;
    const ratio = usedJSHeapSize / jsHeapSizeLimit;
    // 关键操作打标：内存曲线要能对齐到"用户做了什么"
    navigator.sendBeacon('/api/rum', JSON.stringify({
      metric: 'heap_used',
      valueMB: Math.round(usedJSHeapSize / 1048576),
      pressure: Number(ratio.toFixed(2)),
      route: location.hash,
      aliveMs: Math.round(performance.now()),
    }));
    if (ratio > warnRatio) {
      // 压力超 80%：大概率接近 OOM，先于崩溃发出诊断
      navigator.sendBeacon('/api/rum', JSON.stringify({
        metric: 'heap_pressure',
        valueMB: Math.round(usedJSHeapSize / 1048576),
        snapshotHint: '请结合堆快照排查',
      }));
    }
  }, intervalMs);
  return () => clearInterval(timer);
}
startHeapMonitor();
// 判读口诀：锯齿高频 = GC 抖动上对象池；台阶只升不降 = 泄漏，拍快照对比
```
