---
title: [PER-1248] 如何设计"性能对外承诺"（SLA 对客户/合作方）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1248：如何设计"性能对外承诺"（SLA 对客户/合作方）

**答**：
- 场景：B 端客户对嵌入页有性能要求（加载 < 3s）——SLA 是商务条款也是工程约束。
- 定义：可测量的承诺（指标/口径/测量环境/分位数）+ 未达标补偿。
- 工程：SLA 指标独立监控（客户视角环境）、违约告警、月度 SLA 报告自动生成。
- 注意：承诺要留余量（P75 承诺 2.5s 内部目标 2.2s），避免频繁违约。

```javascript
// SLA 监控
const SLA = { embedLoad: { metric: 'LCP', quantile: 'P75', target: 3000 } };
function slaReport(month, records) {
  const rows = records.filter(r => r.month === month);
  const p75 = quantile(rows.map(r => r.lcp), 0.75);
  const breaches = rows.filter(r => r.lcp > SLA.embedLoad.target * 1.5).length;
  return { month, p75, target: SLA.embedLoad.target,
    met: p75 <= SLA.embedLoad.target,
    breachRate: +(breaches / rows.length * 100).toFixed(2) + '%' };
}
function quantile(a, q) { const s = [...a].sort((x, y) => x - y);
  return s[Math.floor(s.length * q)] ?? 0; }
```
