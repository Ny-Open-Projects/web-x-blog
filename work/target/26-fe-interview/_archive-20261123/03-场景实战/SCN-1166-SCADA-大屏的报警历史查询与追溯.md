---
title: [SCN-1166] SCADA 大屏的报警历史查询与追溯（事故回放）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1166：SCADA 大屏的报警历史查询与追溯（事故回放）

**答**：
- 追溯：报警历史（时间/点位/值/操作）多条件检索；事故回放（数据+报警+操作时间轴同步回放）。
- 导出：事故调查报告导出（合规）。
- 性能：历史检索走归档库（冷数据慢提示）。

```javascript
// 事故回放
function incidentReplay(incidentTs, windowMs = 30 * 60_000) {
  const [from, to] = [incidentTs - windowMs / 2, incidentTs + windowMs / 2];
  return {
    tags: queryTags(from, to),                         // 数据曲线
    alarms: alarmsIn(from, to),                        // 报警时间轴
    ops: operationsIn(from, to),                       // 操作时间轴
    sync: (t) => playAll(t),                           // 三轨同步回放
  };
}
function queryTags(f, t) { return []; }
function alarmsIn(f, t) { return []; }
function operationsIn(f, t) { return []; }
function playAll(t) { return true; }
```
