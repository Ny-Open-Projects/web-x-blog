---
title: [SCN-721] 用户旅程级 SLA（下单全链路）怎么定义与看板呈现？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-721：用户旅程级 SLA 怎么定义？
**答**：
- 旅程建模：把「下单成功」拆成步骤链（浏览→加购→结算→支付→结果页），每步有 SLI 与权重；旅程 SLI = 各步成功率的加权组合或端到端转化漏斗达成率。
- 断点归因：旅程达成率下降时自动定位「哪一步掉了」（漏斗步间转化率对比基线），比单页面指标更贴近业务损失。
- 呈现：旅程漏斗图 + 每步达标率色块；异常步骤直接链接到该页面的详细看板。
- 权重口径：按业务价值（支付步权重高于浏览）由业务方定且版本化。
- 追问钩子：旅程级和页面级指标冲突时信谁——旅程级是业务真实结果（页面快但旅程转化降 = 有隐藏断点），以旅程级为北极星、页面级为诊断线索。

```javascript
const journey = {
  name: '下单', steps: [
    { key: 'browse', weight: 0.1, slo: 0.995 },
    { key: 'cart', weight: 0.1, slo: 0.995 },
    { key: 'checkout', weight: 0.3, slo: 0.99 },
    { key: 'pay', weight: 0.5, slo: 0.995 },
  ],
};
function journeyHealth(steps) {
  const funnel = steps.map(s => s.successRate);
  const drops = funnel.map((r, i) => r - (funnel[i + 1] ?? r));   // 步间掉落
  const anomaly = drops.findIndex((d, i) => d > steps[i].baselineDrop * 1.5);
  return {
    overall: funnel.reduce((s, r, i) => s + r * steps[i].weight, 0),   // 加权
    bottleneck: anomaly >= 0 ? steps[anomaly].key : null,    // 断点归因
  };
}
```
