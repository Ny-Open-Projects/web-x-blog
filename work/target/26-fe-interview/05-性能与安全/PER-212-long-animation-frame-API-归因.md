---
title: [PER-212] Long Animation Frames API（LoAF）是什么？比 longtask 好在哪？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-212：Long Animation Frames API（LoAF）是什么？比 longtask 好在哪？

**答**：
- LoAF（`long-animation-frame`）把"慢帧"作为观测单位：一帧 ≥ 50ms 即产生条目，包含 duration、blockingDuration、渲染与样式耗时（styleAndLayoutStart）、以及 scripts 数组（每个慢脚本的 invoker、sourceURL、行号、耗时）。
- 对比 longtask：longtask 只知道"有一个 >50ms 的任务"，无法归因到脚本与函数，更看不到渲染段；LoAF 把 input delay、handler 执行、presentation 三段全部纳入，是 INP 归因的一等公民。
- 典型用法：采集 LoAF 并按 blockingDuration 聚合，上报 top 慢脚本清单给监控平台，直接生成"哪个 SDK/哪个函数拖慢交互"的排行榜。
- 兼容性：Chrome 123+；用 `if ('PerformanceObserver' in window && supportedEntryTypes.includes('long-animation-frame'))` 特性检测，不支持时降级 longtask。

```javascript
// LoAF 采集器：按脚本聚合阻塞时长，产出慢脚本 Top 榜
const scriptCost = new Map();   // sourceURL -> 累计 blockingDuration
new PerformanceObserver((list) => {
  for (const f of list.getEntries()) {
    if (f.duration < 50) continue;
    for (const s of f.scripts) {
      const key = s.invoker || s.sourceURL || 'inline';
      scriptCost.set(key, (scriptCost.get(key) || 0) + s.duration);
    }
  }
}).observe({ type: 'long-animation-frame', buffered: true });
// 定期上报 top5：
setInterval(() => {
  const top = [...scriptCost.entries()].sort((a, b) => b[1] - a[1]).slice(0, 5);
  navigator.sendBeacon('/rum/loaf', JSON.stringify(top)); scriptCost.clear();
}, 30000);
// entry.styleAndLayoutStart 可算出渲染耗时 = duration - scriptsTotal，用于区分"脚本慢"还是"渲染慢"
```
