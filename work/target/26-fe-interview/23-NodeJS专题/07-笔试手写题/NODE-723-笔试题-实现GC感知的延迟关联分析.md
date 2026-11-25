---
title: [NODE-723] 笔试题——实现 GC 停顿与请求延迟的关联分析？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-723：手写 GC 延迟关联

**需求与边界**：
- 需求：验证 P99 毛刺是否 GC 引起（SCN-NODE-635）——① perf_hooks PerformanceObserver 监听 GC（gc:minor/major + duration）；② 请求延迟采样对齐（同时间窗关联）；③ 归因输出（毛刺窗口内 major GC 占比——相关性证据）。
- 边界：① PerformanceObserver buffered（不丢事件）；② 关联窗口容差（GC 结束后 50ms 内完成的请求延迟归因）；③ 输出统计（毛刺请求中 GC 相关占比）。

**答**：
```javascript
import { PerformanceObserver, constants } from 'perf_hooks';
function gcCorrelation() {
  const gcEvents = [], reqLatencies = [];
  new PerformanceObserver((list) => {
    for (const e of list.getEntries())
      gcEvents.push({ start: e.startTime, dur: e.duration,
        kind: e.detail ? e.detail.type : e.kind });    // minor/major
  }).observe({ entryTypes: ['gc'], buffered: true });  // buffered 不丢
  function sampleRequest(id, ms, endTs) { reqLatencies.push({ id, ms, endTs }); }
  function correlate(thresholdMs = 500) {
    const spikes = reqLatencies.filter(r => r.ms > thresholdMs);
    const attributed = spikes.filter(s =>
      gcEvents.some(g => s.endTs >= g.start && s.endTs <= g.start + g.dur + 50));   // 窗口容差
    const majorShare = attributed.filter(s => gcEvents.some(g =>
      g.kind === 'major' && inWindow(s, g))).length;
    return {
      spikeCount: spikes.length,
      gcAttributed: attributed.length,
      gcShare: spikes.length ? attributed.length / spikes.length : 0,
      majorShare,                                      // major GC 占比（调优依据）
      verdict: attributed.length / spikes.length > 0.6 ? 'GC_DRIVEN' : 'OTHER',
    };                                                 // >60% 毛刺 GC 相关 → GC 调优
  }
  return { sampleRequest, correlate };
}
```

**评分点**:
- PerformanceObserver buffered 监听 GC（不丢事件）。
- 时间窗关联（GC 结束后 50ms 容差——SCN-NODE-635 归因）。
- major/minor 区分（调优方向不同）。
- 占比量化 verdict（>60% GC 相关 → 调优有依据）。
