---
title: [SCN-752] 笔试题——实现 SLA 周报自动生成（对比+最差三件事+叙述）？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-752：手写 SLA 周报生成器

**需求与边界**：
- 输入：本周与上周各指标的达标率/预算消耗/事件；输出报告对象：总体结论、差值表、最差三件事（带 owner）、事件清单、自动叙述。
- 边界：① 最差三件按「SLO 距离」排序（未达标的优先）；② 无达标下降时结论为中性；③ 每项结论必须带数据（不给纯形容词）。

**答**：
```javascript
async function weeklyReport(week) {
  const [cur, prev] = await Promise.all([metrics.week(week), metrics.week(week - 1)]);
  const rows = cur.metrics.map(m => ({
    key: m.key, owner: m.owner,
    compliance: m.compliance,
    delta: m.compliance - (prev.metrics.find(p => p.key === m.key)?.compliance ?? m.compliance),
    breach: m.compliance < m.slo,
  }));
  const worst3 = [...rows].sort((a, b) =>
    (b.breach ? 1 : 0) - (a.breach ? 1 : 0) || a.compliance - b.compliance).slice(0, 3);
  const declining = rows.filter(r => r.delta < 0);
  return {
    week,
    overall: cur.compliance, delta: cur.compliance - prev.compliance,
    budgetBurn: cur.burn / cur.budget,
    rows, worst3: worst3.map(r => `${r.key} 达标率 ${(r.compliance * 100).toFixed(2)}%（${r.owner}）`),
    events: cur.events,
    narrative: declining.length
      ? `总体达标率 ${(cur.compliance * 100).toFixed(2)}%（环比 ${(cur.compliance - prev.compliance >= 0 ? '+' : '')}${((cur.compliance - prev.compliance) * 100).toFixed(2)}pp），${declining.length} 项指标下降，预算消耗 ${(cur.burn / cur.budget * 100).toFixed(0)}%`
      : `总体达标率 ${(cur.compliance * 100).toFixed(2)}%，各项指标环比持平或改善，预算消耗 ${(cur.burn / cur.budget * 100).toFixed(0)}%`,
  };
}
```

**评分点**:
- 环比差值逐指标计算（缺失上周回退本周）。
- 最差三件排序规则（breach 优先，再按达标率升序）。
- 结论强制带数据（pp/百分比）。
- 预算消耗并入叙述（行动语言）。
