---
title: [WCN-798] 笔试：手写设计系统 ROI 度量数据聚合器（节省工时估算）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-798：笔试：手写设计系统 ROI 度量数据聚合器（节省工时估算）

**答**：
- 需求：实现 `estimateROI(records)`，records 为 `[{ team, beforeHours, afterHours, adoption, devs, monthlySalary }]`。对每条：单人月省时 = (beforeHours-afterHours)；团队月省工时 = 单人省时 × devs × adoption；月省成本 = 团队月省工时 × (monthlySalary/(devs*160))。汇总总月省成本 totalSaved 与总投入 cost（参数第二参数 investment）。返回 `{ byTeam, totalSaved, roi, paybackMonths }`（roi=(totalSaved*12-investment)/investment，paybackMonths=investment/totalSaved）。边界：afterHours>beforeHours 记 0 省时；adoption 0~1；totalSaved 为 0 时 payback 为 Infinity。
- 要点：逐条计算并汇总；负收益归零；roi 与回本周期；边界防御（除零）。

```javascript
function estimateROI(records, investment) {
  const byTeam = [];
  let totalSaved = 0;
  for (const r of records || []) {
    const savedPerDev = Math.max(0, (r.beforeHours || 0) - (r.afterHours || 0));
    const adoption = Math.min(1, Math.max(0, r.adoption ?? 0));
    const teamSavedHours = savedPerDev * (r.devs || 0) * adoption;
    const hourly = (r.monthlySalary || 0) / ((r.devs || 1) * 160);
    const savedCost = teamSavedHours * hourly;
    totalSaved += savedCost;
    byTeam.push({ team: r.team, savedCost });
  }
  const roi = investment > 0 ? (totalSaved * 12 - investment) / investment : 0;
  const paybackMonths = totalSaved > 0 ? investment / totalSaved : Infinity;
  return { byTeam, totalSaved, roi, paybackMonths };
}
console.log(estimateROI([
  { team:'A', beforeHours:10, afterHours:6, adoption:0.8, devs:10, monthlySalary:300000 },
], 100000));
```

**评分点**：
- 单人省时负值归零，adoption 限幅 0~1（边界正确）。
- 时薪换算与成本估算公式正确。
- roi 与 paybackMonths 计算，除零有防御（Infinity）。
- 按团队聚合 + 汇总，返回结构完整可决策。
