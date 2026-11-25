---
title: [NODE-951] 笔试题——实现发布决策自动建议器（放行/延迟/缩小范围）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-951：手写决策建议

**需求与边界**：
- 需求：决策建议器（SCN-OPS-283）——① 多因子聚合（健康度/历史/日历/风险——SCN-OPS-283）；② 建议分级（PROCEED/DELAY/NARROW——SCN-OPS-283）；③ 建议可解释（SCN-OPS-283）；④ 建议不替代决策（SCN-OPS-283）。
- 边界：① 健康度因子（SCN-OPS-283 带病发布拦截）；② 历史画像（SCN-OPS-329）；③ 建议的置信度（SCN-OPS-283）。

**答**：
```javascript
async function releaseAdvice(plan) {
  const factors = {
    health: await systemHealth(),                      // 带病发布拦截（SCN-OPS-283）
    history: await similarSuccessRate(plan),           // 历史画像（SCN-OPS-329）
    calendar: await calendarConflicts(plan),
    risk: riskLevel(plan),                             // SCN-OPS-297
  };
  const reasons = [];
  let advice = 'PROCEED';
  if (factors.health.degraded) { advice = 'DELAY'; reasons.push('系统异常'); }
  else if (factors.history.successRate < 0.8) { advice = 'NARROW-SCOPE'; reasons.push('历史成功率低'); }
  else if (factors.calendar.conflict) { advice = 'DELAY'; reasons.push('日历冲突'); }
  return { advice, reasons, confidence: dataConfidence(factors),
    note: '建议供决策参考（SCN-OPS-283）' };
}
```

**评分点**:
- 多因子聚合（SCN-OPS-283）。
- 建议分级 + 可解释（SCN-OPS-283）。
- 带病发布拦截（SCN-OPS-283）。
- 历史画像（SCN-OPS-329）。
