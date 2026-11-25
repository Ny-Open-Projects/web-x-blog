---
title: [WCN-797] 如何量化设计系统对业务研发提效与一致性的真实收益？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-797：如何量化设计系统对业务研发提效与一致性的真实收益？

**答**：
- 结论：提效用「需求交付时长、重复造轮子率、组件复用率」的前后对比衡量；一致性用「裸值率下降、token 覆盖率、视觉回归通过率」衡量；用对照团队/时间趋势做归因。
- 建立基线（引入前）与持续看板，结合定性反馈（NPS、访谈）；避免把业务自然增长误算成平台功劳，用差分法（对比未采用团队）。
- 追问钩子：采用率低时是平台不好还是业务不知情？考察「采用漏斗分析：认知→试用→深度使用」的定位能力。

```javascript
function measureImpact(before, after, control) {
  const delta = (a, b) => (b - a) / a;            // 变化率
  const deliveryGain = delta(before.deliveryDays, after.deliveryDays);
  const controlGain = delta(control.deliveryDays, control.afterDeliveryDays || control.deliveryDays);
  return {
    deliveryGain,                                  // 采用团队变化
    attributable: deliveryGain - controlGain,      // 差分：扣除自然变化
    reuseRate: after.reuseRate,
    bareValueDrop: delta(before.bareValue, after.bareValue),
  };
}
console.log(measureImpact(
  { deliveryDays: 10, bareValue: 0.4 },
  { deliveryDays: 7, reuseRate: 0.8, bareValue: 0.15 },
  { deliveryDays: 10, afterDeliveryDays: 9.5 }
));
```
