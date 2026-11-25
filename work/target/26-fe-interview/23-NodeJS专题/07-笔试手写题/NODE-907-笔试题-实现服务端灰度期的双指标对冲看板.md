---
title: [NODE-907] 笔试题——实现灰度对冲看板（主指标+守护指标成对）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-907：手写对冲看板

**需求与边界**：
- 需求：对冲看板（SCN-OPS-252）——① 主指标与守护指标成对（SCN-OPS-252 映射）；② 合取判定（主达标 AND 守护不劣化——SCN-OPS-252）；③ 成对展示（看板纪律）；④ 判定失败的修复建议（SCN-OPS-252）。
- 边界：① 映射表配置化（SCN-OPS-252）；② 守护指标基线动态（SCN-OPS-304）；③ 判定的样本量（SCN-OPS-203）。

**答**：
```javascript
const HEDGE = { conversion: 'complaint_rate', latencyImprovement: 'cpu', deployFreq: 'changeFailRate' };
async function hedgeBoard(gray) {
  const pairs = Object.entries(HEDGE).map(([main, guard]) => ({
    main: metricVs(gray, main), guard: metricVs(gray, guard),   // 成对（SCN-OPS-252）
    pass: mainOk(gray, main) && guardOk(gray, guard),           // 合取（SCN-OPS-252）
  }));
  return { pairs: pairs.map(p => ({ ...p, fix: p.pass ? null : hedgeFix(p) })),
    allPass: pairs.every(p => p.pass),
    note: '合取判定——单指标优化不代表净收益（SCN-OPS-252）' };
}
```

**评分点**:
- 成对展示（SCN-OPS-252 看板纪律）。
- 合取判定（主 AND 守护——SCN-OPS-252）。
- 修复建议映射 + 动态基线（SCN-OPS-304）。
- 样本量约束（SCN-OPS-203）。
