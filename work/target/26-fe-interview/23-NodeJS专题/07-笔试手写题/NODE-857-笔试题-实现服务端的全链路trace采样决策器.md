---
title: [NODE-857] 笔试题——实现全链路 trace 采样决策器（头采样+尾采样）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-857：手写采样决策

**需求与边界**：
- 需求：trace 采样（SCN-NODE-645）——① 头采样（入口决定采样标记——全链跟随，SCN-NODE-645 traceparent）；② 尾采样（错误/慢请求 100% 保留——SCN-NODE-645 采样策略）；③ 采样与压测/灰度标记的组合（SCN-NODE-717/670）；④ 采样率动态（过载降采样——SCN-NODE-794）。
- 边界：① 头采样的标记传播（采样决定 → 全链——SCN-OPS-216 贯穿）；② 尾采样的成本（全 trace 缓冲后判定——内存开销）；③ 采样率调整的热更（SCN-NODE-663）。

**答**：
```javascript
// 头采样（入口决定——全链跟随）
function headSample(req) {
  const sampled = Math.random() < dynamicSampleRate();   // 动态（SCN-NODE-794）
  return { traceparent: buildTraceparent({ sampled, traceId: newTraceId() }),
    sampled };
}
// 尾采样（collector 侧：错误/慢全保留）
function tailSample(trace) {
  const hasError = trace.spans.some(s => s.status === 'error');
  const isSlow = trace.duration > P99_THRESHOLD;
  return hasError || isSlow || trace.sampled;          // 错/慢全保留（SCN-NODE-645）
}
// 动态采样率（过载降采样——SCN-NODE-794）
const rate = overloaded() ? 0.01 : config.traceSampleRate;
```

**评分点**:
- 头采样标记全链跟随（SCN-OPS-216 贯穿）。
- 尾采样（错误/慢 100%——SCN-NODE-645 成本与排障平衡）。
- 动态采样率热更（SCN-NODE-663/794）。
- 与压测/灰度标记组合（SCN-NODE-717）。
