---
title: [SCN-708] SLA 趋势对比与周报复盘视图怎么设计？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-708：SLA 趋势对比与周报怎么设计？
**答**：
- 趋势三线：本周曲线 + 上周同刻对比线 + SLO 目标线，一目了然是「周期性波动」还是「趋势性劣化」。
- 周报自动生成：达标率/预算消耗/超 SLO 事件清单/与上周差值，每项附一句结论模板（不许只给数字不给结论）；人工补充根因与改进项。
- 事件标注：图上自动标注发版/大促/故障时间点，趋势异动可解释。
- 归因辅助：劣化自动关联变化集（发版 diff/配置变更/流量增长），给出候选原因排序。
- 追问钩子：周报怎么避免变成「报喜不报忧」——结论模板强制包含「最差的三件事」，且指标口径自动取数（不可手工填数）。

```javascript
async function weeklyReport(week) {
  const cur = await metrics.weekly(week), prev = await metrics.weekly(week - 1);
  return {
    compliance: cur.compliance, delta: cur.compliance - prev.compliance,
    budgetBurn: cur.burn / cur.budget,                 // 预算消耗率
    worst3: [...cur.metrics].sort((a, b) => a.compliance - b.compliance).slice(0, 3)
      .map(m => `${m.key} 达标率 ${m.compliance}（${m.owner}）`),   // 强制最差三件事
    annotations: events.in(week),                      // 发版/故障自动标注
    autoNarrative: cur.compliance < prev.compliance
      ? `较上周下降 ${(prev.compliance - cur.compliance) * 100}%，主要贡献：${topDrift(cur, prev)}` : null,
  };
}
```
