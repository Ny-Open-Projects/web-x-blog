---
title: [WCN-953] 手写 WC vs 框架组件成本收益评估器：按团队规模 / 技术栈数 / 生命周期推荐
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-953：手写 WC vs 框架组件成本收益评估器：按团队规模 / 技术栈数 / 生命周期推荐

**题目**：实现 `evaluateStack({ frameworks, teams, componentCount, lifespanYears, changeFreq })`，返回 `{ recommendation, scores, reasons }`。要求：① 计算两套方案成本分（越低越好）：wcCost = componentCount × (1 + changeFreq × lifespanYears)；adapterCost = componentCount × (1 + 0.5 × (frameworks-1) × (1 + changeFreq × lifespanYears)) + teams × 2；② frameworks<2 时直接推荐「框架原生」（WC 优势不足）；③ 否则按 scores 比较给出「纯 WC」或「框架组件+适配层」；④ reasons 给出至少两条关键依据（如栈数、变更频率）；⑤ 输入缺失字段给默认值（frameworks=2,teams=2,componentCount=20,lifespanYears=2,changeFreq=0.2），不抛异常。请自足实现并给出可运行示例。

**答**：

```javascript
function evaluateStack(opts = {}) {
  const { frameworks = 2, teams = 2, componentCount = 20,
          lifespanYears = 2, changeFreq = 0.2 } = opts || {};
  const churn = changeFreq * lifespanYears;
  const wcCost = componentCount * (1 + churn);
  const adapterCost = componentCount * (1 + 0.5 * (frameworks - 1) * (1 + churn)) + teams * 2;
  let recommendation, reasons = [];
  if (frameworks < 2) {
    recommendation = '框架原生';
    reasons.push('框架数<2，WC 跨栈优势不足');
  } else {
    recommendation = wcCost <= adapterCost ? '纯 WC' : '框架组件+适配层';
    reasons.push(`跨 ${frameworks} 个框架，栈数越多越利于 WC`);
    reasons.push(`变更频率 ${changeFreq}，频繁变更时适配层成本放大`);
  }
  return { recommendation,
    scores: { wcCost: +wcCost.toFixed(1), adapterCost: +adapterCost.toFixed(1) },
    reasons };
}
console.log(evaluateStack({ frameworks: 4, teams: 5, componentCount: 60, lifespanYears: 3, changeFreq: 0.1 }));
console.log(evaluateStack({ frameworks: 1 })); // 框架原生
console.log(evaluateStack()); // 用默认值
```

**评分点**：
- 两套成本公式计算正确（含 changeFreq×lifespan 的变更放大）。
- frameworks<2 直接推荐框架原生的短路逻辑正确。
- reasons 给出至少两条关键依据且与实际输入相关。
- 默认字段补全、非对象输入健壮不抛异常。
- 返回结构正确、示例可运行。
