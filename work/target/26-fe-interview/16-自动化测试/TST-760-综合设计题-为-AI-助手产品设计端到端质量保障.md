---
title: [TST-760] 综合设计题：为一个 AI 助手产品设计端到端质量保障
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-760：综合设计题：为一个 AI 助手产品设计端到端质量保障

**答**：
- 结论：AI 助手的质量=「功能正确性 × 输出可靠性 × 安全合规 × 性能体验」四象限，每条都要有可测的断言。
- 功能：黄金集回归 + 属性断言；可靠性：多采样一致率与幻觉率；安全：Prompt 注入与 PII 泄露；性能：首 token 延迟与流式稳定性。
- 平台侧统一编排四类检查，设硬门禁（安全）+ 软门禁（质量分），持续监控线上漂移。
- 追问钩子：产品上线后用户反馈「答案变差」，如何用测试体系定位是模型还是工程问题？

```javascript
// AI 助手质量四维评分卡
function qualityScorecard(m) {
  const dims = {
    function: m.goldenPassRate,
    reliability: m.consistencyRate,
    security: 1 - m.piiLeakRate,
    perf: m.withinLatencyBudget ? 1 : 0,
  };
  const gate = dims.security >= 0.99; // 安全硬门禁
  const score = Object.values(dims).reduce((s, v) => s + v, 0) / 4;
  return { dims, gate, score: +score.toFixed(2), pass: gate && score >= 0.8 };
}
console.log(qualityScorecard({
  goldenPassRate: 0.9, consistencyRate: 0.85, piiLeakRate: 0, withinLatencyBudget: true,
}));
```
