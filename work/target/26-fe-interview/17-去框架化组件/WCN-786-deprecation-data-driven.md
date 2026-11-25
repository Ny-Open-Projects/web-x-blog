---
title: [WCN-786] 如何用组件使用数据驱动弃用决策与投入产出分析？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-786：如何用组件使用数据驱动弃用决策与投入产出分析？

**答**：
- 结论：采集组件的引用量、覆盖业务方数量、关联工单/故障数、维护成本，按「低使用 + 高维护 + 高故障」判定弃用候选；用数据替代主观判断。
- 弃用决策要评估迁移成本（影响调用方数量 × 单点改造成本）与收益（维护人力释放），ROI 为正才推进；提供 codemod 降低迁移成本。
- 追问钩子：某组件使用量低但是合规关键组件（如支付按钮）能弃用吗？考察「使用量不是唯一维度，业务重要性/风险要加权」。

```javascript
function deprecationScore(m) {
  // 低使用、高故障、高维护成本 -> 高分（优先弃用候选）
  return (1 - m.usage) * 0.4 + m.defects * 0.3 + m.maintainCost * 0.3;
}
function roi(m, migrateCost, savedMonthly) {
  const benefit = savedMonthly * 12;
  return { score: deprecationScore(m), roi: (benefit - migrateCost) / migrateCost };
}
const m = { usage: 0.05, defects: 2, maintainCost: 3, critical: true };
const r = roi(m, 20, 5);
console.log(r, '关键组件需人工复核:', m.critical);
```
