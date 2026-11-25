---
title: [AIC-770] AI 提效如何转化为可度量的业务价值
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-770：AI 提效如何转化为可度量的业务价值

**答**：
- 结论先行：提效本身不是价值，只有当「省下的时间」被 reinvest 到「更多交付 / 更快上市 / 更少事故」时才成为业务价值；度量的终点是后者，不是「节省了多少人时」。
- 转化路径：1) 效率提升（周期缩短）→ 2) 吞吐提升（单位时间交付更多）→ 3) 业务结果（上线更快、事故更少、收入/体验改善）；每一环都要能验证。
- 度量方法：用「反事实」估算——对比 AI 引入前后的同口径吞吐与质量，控制外部因素；避免把「业务自然增长」算成 AI 功劳。
- 追问钩子：为什么「省了人时」不等于「省了成本」？——如果省下的时间没有被重新利用（人闲置或做低价值事），成本并未真正下降；价值兑现依赖资源再配置。

```javascript
// 业务价值 = 效率提升 × 转化系数（是否被 reinvest）
function businessValue({ hoursSaved, reinvestRatio, valuePerHour }) {
  const reinvested = hoursSaved * reinvestRatio;
  return { reinvestedHours: reinvested, value: reinvested * valuePerHour };
}
console.log(businessValue({ hoursSaved: 100, reinvestRatio: 0.2, valuePerHour: 500 }).value);
// 10000：仅 20% 省下时间转化为交付，价值需按转化率折算
console.log(businessValue({ hoursSaved: 100, reinvestRatio: 0, valuePerHour: 500 }).value === 0);
```
