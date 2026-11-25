---
title: [TST-778] AI 时代「测试右移」：线上故障如何自动转化为混沌场景
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-778：AI 时代「测试右移」：线上故障如何自动转化为混沌场景

**答**：
- 结论：右移闭环=「线上故障 → AI 提取故障特征 → 生成混沌场景 → 纳入回归库」，让每次真实事故变成未来的防线。
- AI 从事故报告/日志/监控中提取「故障模式」（哪个依赖失败、什么表现、如何恢复），结构化为注入参数。
- 转化必须人工审核：脱敏、控制爆炸半径、验证场景不会造成二次伤害。
- 追问钩子：AI 把一次事故转成场景但注入条件过于苛刻无法复现，怎么办？

```javascript
// 线上故障 → 混沌场景结构化
function faultToScenario(incident) {
  return {
    name: incident.type + '-regression',
    inject: { target: incident.failedDependency, type: incident.failureMode },
    steady: { metric: incident.keyMetric, threshold: incident.slo },
    source: incident.id, // 可追溯到原事故
  };
}
console.log(faultToScenario({
  id: 'INC-1', type: 'payment', failedDependency: 'pay-sdk',
  failureMode: 'timeout', keyMetric: 'errorRate', slo: 0.01,
}));
```
