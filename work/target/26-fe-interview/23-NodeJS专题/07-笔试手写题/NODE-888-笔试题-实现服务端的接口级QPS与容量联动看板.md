---
title: [NODE-888] 笔试题——实现接口级 QPS 容量联动看板（水位+余量+扩容建议）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-888：手写容量看板

**需求与边界**：
- 需求：容量看板（SCN-NODE-647/765）——① 接口级 QPS 水位（当前/稳态容量/余量——SCN-NODE-647 模型）；② 压测基线（SCN-NODE-647 稳态）；③ 余量告警（<30% 扩容建议——SCN-NODE-834）；④ 大促预估联动（SCN-NODE-765）。
- 边界：① 稳态容量的时效（压测数据过期——SCN-NODE-647 重测周期）；② 水位分位（P99——SCN-NODE-647）；③ 建议的可执行（扩容清单——SCN-NODE-834）。

**答**：
```javascript
async function capacityBoard(apis) {
  const rows = await Promise.all(apis.map(async (api) => {
    const qps = await currentQps(api);
    const steady = await steadyCapacity(api);          // 压测稳态（SCN-NODE-647）
    const margin = 1 - qps / steady;
    return { api, qps, steady, margin,
      suggest: margin < 0.3 ? scaleSuggest(api) : null };   // 余量告警（SCN-NODE-834）
  }));
  const campaign = campaignCapacityPlan(apis);         // 大促预估（SCN-NODE-765）
  return { rows: rows.sort(byMargin), campaign,
    note: rows.some(r => r.stale > 90) ? `${r.api} 压测数据超 90 天——建议重测` : null };   // 压测时效
}
```

**评分点**:
- 水位/余量/告警（SCN-NODE-647/834）。
- 压测基线时效（90 天重测——SCN-NODE-647）。
- 大促预估联动（SCN-NODE-765）。
- 排序（余量最小优先）。
