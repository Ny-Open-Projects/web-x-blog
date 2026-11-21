---
title: [PER-206] 笔试题：手写一个基于 PerformanceObserver 的 INP 采集上报 SDK（含采样与过滤）
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-206：手写一个基于 PerformanceObserver 的 INP 采集上报 SDK（含采样与过滤）

**题目**：实现 `createInpTracker({ report })`。要求：① 用 Event Timing API 收集所有交互，按 interactionId 聚合，同一次交互取最长 duration；② 每 50 次交互采样一次，取当前已见最差值上报；③ 过滤 bfcache 恢复与页面隐藏期间的交互；④ 页面 `pagehide` 时兜底上报最后一段。

**答**：核心是三件事——interactionId 聚合（一次交互多事件取 max）、`durationThreshold` 过滤微小交互、visibility/pagehide 边界兜底。上报用 sendBeacon 保证卸载不丢。

```javascript
function createInpTracker({ report }) {
  const byId = new Map();          // interactionId -> worst duration
  let sampled = 0, pageWorst = 0, visible = true;

  const obs = new PerformanceObserver((list) => {
    for (const e of list.getEntries()) {
      if (e.interactionId == null) continue;
      if (!visible) continue;                          // 后台标签不计
      if (document.wasDiscarded) continue;
      const w = byId.get(e.interactionId) ?? 0;
      byId.set(e.interactionId, Math.max(w, e.duration));
    }
    const count = byId.size;
    if (count >= (sampled + 1) * 50) {                 // 每 50 次交互采样
      sampled = Math.floor(count / 50);
      pageWorst = Math.max(...byId.values());          // 采样点取当前最差
      report({ metric: 'INP', value: pageWorst, samples: count, url: location.pathname });
    }
  });
  obs.observe({ type: 'event', durationThreshold: 16, buffered: true });

  document.addEventListener('visibilitychange', () => {
    visible = document.visibilityState === 'visible';
    if (!visible) flush();
  });
  const flush = () => pageWorst && navigator.sendBeacon(
    '/rum/inp', JSON.stringify({ metric: 'INP', value: pageWorst, url: location.pathname }));
  addEventListener('pagehide', flush);                 // bfcache/卸载兜底

  return { flush };
}

// createInpTracker({ report: (d) => fetch('/rum', { method: 'POST', body: JSON.stringify(d), keepalive: true }) })
```

**评分点**：
- 是否用 `interactionId` 聚合并对同一次交互取 max（漏掉这步口径就错了）。
- 是否设置 `durationThreshold`（默认会灌入海量微事件）与 `buffered: true`（漏掉 observer 注册前的交互）。
- 边界处理：visibility 过滤、pagehide/sendBeacon 兜底上报，bfcache 恢复样本剔除。
- 采样口径正确：每 50 次交互取"最差"而非平均值。
