---
title: [TST-776] 混沌实验与 AI 监控联动：如何验证「告警的有效性」
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-776：混沌实验与 AI 监控联动：如何验证「告警的有效性」

**答**：
- 结论：混沌实验是验证监控告警的「压力测试」——主动注入故障，看告警是否在预期时间内触发且指向正确根因。
- 验证三要素：检出率（是否告警）、时效（MTTD 是否达标）、准确度（是否指向正确服务/指标）。
- AI 监控（异常检测）要特别验证误报与漏报，用注入的「已知故障」作为 ground truth 计算准确率。
- 追问钩子：注入了故障但监控没告警，是监控坏了还是故障没生效？

```javascript
// 告警有效性：用已知注入故障作为 ground truth
function evaluateAlerts(injected, alerts) {
  const detected = injected.filter(f => alerts.some(a =>
    a.service === f.service && a.at >= f.at && a.at - f.at < 60000
  ));
  return {
    detectRate: +(detected.length / (injected.length || 1)).toFixed(2),
    missed: injected.filter(f => !detected.includes(f)).map(f => f.service),
  };
}
console.log(evaluateAlerts(
  [{ service: 'api', at: 1000 }],
  [{ service: 'api', at: 1050 }]
)); // detectRate:1
```
