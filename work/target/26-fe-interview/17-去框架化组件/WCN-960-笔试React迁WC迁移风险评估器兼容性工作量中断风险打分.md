---
title: [WCN-960] 手写迁移风险评估器：React 组件迁 WC 的兼容性 / 工作量 / 中断风险打分
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-960：手写迁移风险评估器：React 组件迁 WC 的兼容性 / 工作量 / 中断风险打分

**题目**：实现 `assessMigration(comp)`，comp 形如 `{ usesHooks, usesContext, domHeavy, hasForm, testCoverage, businessCritical }`（前四项布尔，后两项 0~100 数值）。要求输出 `{ score, level, blockers, effortDays }`：① score = 基础 100 - hooks扣15 - context扣20 - domHeavy扣10 - hasForm扣5 - (100-testCoverage)*0.2 - businessCritical*0.1，截断到 0~100；② level：score≥70 '低风险'，40~69 '中风险'，<40 '高风险'；③ blockers 列出扣分>15 的因素名（hooks/context 等）；④ effortDays = Math.ceil((100-score)/8)；⑤ 字段缺省：布尔默认 false，数值默认 50；不修改输入。请自足实现并给出可运行示例。

**答**：

```javascript
function assessMigration(comp = {}) {
  const c = comp || {};
  const { usesHooks = false, usesContext = false, domHeavy = false,
    hasForm = false, testCoverage = 50, businessCritical = 50 } = c;
  const deductions = {
    hooks: usesHooks ? 15 : 0, context: usesContext ? 20 : 0,
    domHeavy: domHeavy ? 10 : 0, hasForm: hasForm ? 5 : 0,
    coverage: (100 - testCoverage) * 0.2, critical: businessCritical * 0.1,
  };
  let score = 100 - Object.values(deductions).reduce((s, x) => s + x, 0);
  score = Math.max(0, Math.min(100, Math.round(score)));
  const level = score >= 70 ? '低风险' : score >= 40 ? '中风险' : '高风险';
  const blockers = Object.entries(deductions).filter(([, v]) => v > 15).map(([k]) => k);
  const effortDays = Math.ceil((100 - score) / 8);
  return { score, level, blockers, effortDays };
}
console.log(assessMigration({ usesHooks: true, usesContext: true, testCoverage: 40, businessCritical: 90 }));
console.log(assessMigration()); // 默认，低风险
```

**评分点**：
- score 公式与截断正确（0~100）。
- level 三档划分正确。
- blockers 只在扣分>15 时列出对应因素。
- effortDays 计算正确（向上取整）。
- 默认值补全、不修改输入、示例可运行。
