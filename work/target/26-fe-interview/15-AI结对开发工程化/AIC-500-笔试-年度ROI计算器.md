---
title: [AIC-500] 笔试：AI 工程化年度 ROI 终算。
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-500：笔试：AI 工程化年度 ROI 终算。
**题目**：输入成本 `{tools, api, headcountMonths}`（人力月成本单价 rate）与收益 `{cycleSavedHours, hourlyRate, avoidedHires}`（每避免一次招聘价值 hireValue）。ROI = (收益 - 成本) / 成本。输出 `{cost, benefit, roi, verdict}`（roi > 0.3 为 positive）。

```javascript
function roi({ tools, api, headcountMonths, rate }, { cycleSavedHours, hourlyRate, avoidedHires, hireValue }) {
  const cost = tools + api + headcountMonths * rate;
  const benefit = cycleSavedHours * hourlyRate + avoidedHires * hireValue;
  const r = cost ? (benefit - cost) / cost : 0;
  return { cost, benefit, roi: +r.toFixed(2),
           verdict: r > 0.3 ? 'positive' : r > 0 ? 'marginal' : 'negative' };
}
console.log(roi(
  { tools: 20_000, api: 30_000, headcountMonths: 6, rate: 30_000 },
  { cycleSavedHours: 2000, hourlyRate: 150, avoidedHires: 1, hireValue: 500_000 }));
// cost 230k，benefit 800k → roi 2.48 positive

```

**评分点**：
- 成本三部分完整（人力隐性成本别漏）。
- 收益换算公式明确（小时 × 时薪 + avoided × 单价）。
- ROI 公式与阈值判定。
- 负 ROI 也要如实输出（不做美化）。
