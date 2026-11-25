---
title: [XP-353] 跨端崩溃率与 ANR 的前端联动
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-353：跨端崩溃率与 ANR 的前端联动

**答**：
- 前端责任：避免主线程长任务（ANR 主因）、监听器泄漏、内存暴涨（OOM 崩溃）。
- 联动：前端性能指标（长任务率）与原生崩溃率关联分析（内存 OOM 前常有 JS 内存暴涨）。
- 阈值：崩溃率 > 0.1% 或 ANR > 0.05% 触发专项。

```javascript
// 崩溃联动分析
function crashCorrelation(crashRecords, perfRecords) {
  const oomSessions = crashRecords.filter(c => c.type === 'oom')
    .map(c => c.sessionId);
  const perf = perfRecords.filter(r => oomSessions.includes(r.sessionId));
  return {
    oomCount: oomSessions.length,
    memPattern: avg(perf.map(p => p.peakMemMB)),
    note: avg(perf.map(p => p.peakMemMB)) > 400
      ? 'OOM 会话内存显著偏高，优先治理内存' : '无明显关联',
  };
}
function avg(a) { return a.length ? a.reduce((s, v) => s + v, 0) / a.length : 0; }
```
