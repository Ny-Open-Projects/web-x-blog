---
title: [PER-213] 笔试题：手写 LoAF 长帧采集器，按 invoker 聚合并区分"脚本慢"与"渲染慢"
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-213：手写 LoAF 长帧采集器，按 invoker 聚合并区分"脚本慢"与"渲染慢"

**题目**：实现 `trackLoAF(report, threshold = 50)`：① 采集 long-animation-frame 条目；② 每帧计算脚本耗时与渲染耗时（`styleAndLayoutStart` 起到帧尾），按 invoker 聚合脚本耗时；③ 渲染耗时占比 > 40% 的帧单独标记 renderHeavy；④ 每 10 帧批量上报。不支持 LoAF 时降级 longtask 计数。

**答**：归因公式：脚本总耗时 = sum(scripts[].duration)；渲染耗时 ≈ duration - 脚本总耗时 - 阻塞外的空闲。用 `styleAndLayoutStart` 更精确：渲染段 = duration - (styleAndLayoutStart - startTime)。

```javascript
function trackLoAF(report, threshold = 50) {
  const invokers = new Map();
  let frames = [];

  const supported = PerformanceObserver.supportedEntryTypes?.includes('long-animation-frame');
  if (!supported) {   // 降级：仅计数 longtask
    new PerformanceObserver((l) => {
      frames.push({ duration: l.getEntries().reduce((s, e) => s + e.duration, 0), degraded: true });
      if (frames.length >= 10) report({ frames, degraded: true }), (frames = []);
    }).observe({ type: 'longtask', buffered: true });
    return;
  }

  new PerformanceObserver((list) => {
    for (const f of list.getEntries()) {
      if (f.duration < threshold) continue;
      let scriptTotal = 0;
      for (const s of f.scripts) {
        const key = `${s.invoker || s.sourceURL || 'inline'}`;
        invokers.set(key, (invokers.get(key) || 0) + s.duration);
        scriptTotal += s.duration;
      }
      const renderCost = f.styleAndLayoutStart
        ? f.startTime + f.duration - f.styleAndLayoutStart
        : f.duration - scriptTotal;
      frames.push({
        duration: Math.round(f.duration),
        blocking: Math.round(f.blockingDuration),
        renderCost: Math.round(renderCost),
        renderHeavy: renderCost > f.duration * 0.4,   // 渲染占比 > 40%
      });
      if (frames.length >= 10) {
        report({ frames, invokers: [...invokers.entries()].sort((a, b) => b[1] - a[1]).slice(0, 5) });
        frames = []; invokers.clear();
      }
    }
  }).observe({ type: 'long-animation-frame', buffered: true });
}
```

**评分点**：
- 特性检测与 longtask 降级路径完整。
- 正确区分脚本段与渲染段（styleAndLayoutStart 或 duration - scriptTotal），并给出 renderHeavy 判定。
- 按 invoker 聚合（而不是逐帧上报原始条目），上报量可控。
- 批量上报节流（10 帧一批），不逐帧打点。
