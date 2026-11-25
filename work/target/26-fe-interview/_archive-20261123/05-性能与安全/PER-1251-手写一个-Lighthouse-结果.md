---
title: [PER-1251] 手写一个 Lighthouse 结果解析器：提取审计项并生成门禁判定
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1251：手写一个 Lighthouse 结果解析器：提取审计项并生成门禁判定

**答**：
- 需求：实现 parseLighthouse(report, budgets)。report 为 LH JSON（categories.performance.score 0~1，audits: { id: { numericValue, score } }）；budgets 为 { lcp: ms, cls: number, perfScore: 0~1 }；判定每项 pass/fail，输出 { pass, items }（含 value/limit/delta）。
- 边界：report 缺 category 视为 fail（数据异常）；cls 用 audits cumulative-layout-shift 的 numericValue；score 为 null 按 0 处理。
- 评分点：审计提取；缺省兜底；delta 计算；全过判定

```javascript
function parseLighthouse(report, budgets) {
  const audits = report.audits ?? {};
  const lcp = audits['largest-contentful-paint']?.numericValue ?? Infinity;
  const cls = audits['cumulative-layout-shift']?.numericValue ?? Infinity;
  const score = report.categories?.performance?.score ?? 0;
  const items = [
    { id: 'lcp', value: lcp, limit: budgets.lcp },
    { id: 'cls', value: cls, limit: budgets.cls },
    { id: 'perfScore', value: score, limit: budgets.perfScore },
  ].map(i => ({ ...i, delta: +(i.value - i.limit).toFixed(4),
    pass: i.value <= i.limit }));
  return { pass: items.every(i => i.pass), items };
}
```
