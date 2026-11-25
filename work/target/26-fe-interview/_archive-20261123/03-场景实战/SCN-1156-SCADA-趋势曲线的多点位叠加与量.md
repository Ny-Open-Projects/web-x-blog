---
title: [SCN-1156] SCADA 趋势曲线的多点位叠加与量程
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1156：SCADA 趋势曲线的多点位叠加与量程

**答**：
- 曲线：多点位同图叠加（不同单位双轴）、量程自适应/手动锁定（工艺标准量程）。
- 游标：时间游标读数（多点位同时刻对比）、区域缩放（拖拽放大）。
- 导出：趋势数据导出（CSV 分析）。

```javascript
// 多点位趋势
function trendOverlay(tags, range) {
  return {
    series: tags.map(t => ({ tag: t.id, unit: t.unit, data: queryTag(t.id, range) })),
    dualAxis: new Set(tags.map(t => t.unit)).size > 1,     // 多单位双轴
    rangeLock: t => t.standardRange ?? null,               // 工艺标准量程
    cursor: (ts) => tags.map(t => sampleAt(t.id, ts)),     // 同时刻对比
  };
}
function queryTag(id, range) { return []; }
function sampleAt(id, ts) { return 0; }
```
