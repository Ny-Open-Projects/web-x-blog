---
title: [AIC-977] AI Review 总把商品列表的正常写法（如合理的 any 使用）报成问题，开发者开始无视报告，怎么治理？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-977：AI Review 总把商品列表的正常写法（如合理的 any 使用）报成问题，开发者开始无视报告，怎么治理？
**答**：
- 误报治理的第一步是「承认误报存在并度量」——结论：不要假装 AI Review 全对，先统计误报率（被标记后未修改的比例），用数据定位问题规则。
- 精准化手段：① 给规则加上下文（如「测试文件允许 any」）；② 提供「误报反馈」按钮，反馈进入规则优化闭环；③ 对高频误报规则降权或关闭，先保住工程师对报告的信任。
- 「信任」是 Review 系统的生命线：一旦工程师养成无视习惯，真问题也会被忽略——结论：宁可少报不错报，召回让位于精确。
- 追问钩子：能说出「误报治理的核心指标是『阳性预测值(报出来的里真问题的比例)』而非召回率，要先提升信噪比重建信任」的候选人，理解了治理的优先级。

```typescript
// 误报治理：反馈闭环 + 规则降权
function tuneRules(reviews) { // reviews: {rule, wasActioned}[]
  const stats = {};
  for (const r of reviews) {
    stats[r.rule] ??= { total:0, actioned:0 };
    stats[r.rule].total++;
    if (r.wasActioned) stats[r.rule].actioned++;
  }
  return Object.entries(stats).map(([rule,s])=>({
    rule, precision:+(s.actioned/s.total).toFixed(2),
    action: s.actioned/s.total < 0.3 ? '降权/关闭' : '保留'
  })).sort((a,b)=>a.precision-b.precision);
}
console.log(tuneRules([
  {rule:'any告警',wasActioned:false},{rule:'any告警',wasActioned:false},
  {rule:'硬编码密钥',wasActioned:true},
]));
```
