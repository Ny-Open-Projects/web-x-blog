---
title: [ENG-184] 基建项目的 ROI 怎么评估？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-184：基建项目的 ROI 怎么评估？
**答**：
- ROI =（年化节省人力成本 − 建设与维护成本）/（建设与维护成本）；维护成本按建设成本的 30% 年化，不能只算建设。
- 节省量化要保守：使用人数 × 频次 × 单次节省时长 × 时薪 × 折减系数（0.5~0.7），杜绝拍脑袋放大。
- 隐性收益单列不折算：质量提升 故障减少 一致性 招聘吸引力，定性说明放报告附录。
- 决策阈值：ROI 低于 1 且无战略理由不立项；3 以上优先；立项时把 ROI 计算假设写进文档，事后对账。

```javascript
// scripts/infra-roi.mjs —— 基建项目 ROI 评估
function evaluate({
  users, timesPerWeek, minutesSaved, hourlyCost,
  buildDays, maintainRatio = 0.3, discount = 0.6,
}) {
  const annualSavedHours = users * timesPerWeek * 52 * (minutesSaved / 60) * discount
  const savedCost = annualSavedHours * hourlyCost
  const buildCost = buildDays * 8 * hourlyCost
  const maintainCost = buildCost * maintainRatio
  const roi = (savedCost - maintainCost) / buildCost
  return {
    annualSavedHours: annualSavedHours.toFixed(0),
    savedCost: savedCost.toFixed(0),
    buildCost: buildCost.toFixed(0),
    maintainCost: maintainCost.toFixed(0),
    roi: roi.toFixed(2),
    verdict: roi >= 3 ? '优先立项' : roi >= 1 ? '可立项' : '不立项 除非有战略理由',
  }
}
// 示例 脚手架 40 人使用 每周 2 次 每次省 30 分钟 建设 15 人天
console.log(evaluate({ users: 40, timesPerWeek: 2, minutesSaved: 30, hourlyCost: 120, buildDays: 15 }))
```
