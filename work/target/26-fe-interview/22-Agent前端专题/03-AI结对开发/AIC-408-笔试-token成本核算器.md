---
title: [AIC-408] 笔试：实现带缓存折扣的 token 成本核算器。
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-408：笔试：实现带缓存折扣的 token 成本核算器。
**答**：计价：输入非缓存 $3/M tokens，缓存命中 $0.3/M，输出 $6/M。实现 `cost(model, {in, cached, out})`，保留 6 位小数（美元），并输出按任务类型聚合的 `summary(records)`。

```javascript
const PRICE = { in: 3, cached: 0.3, out: 6 }; // $ / 1M tokens
function cost(usage) {
  const { in: i = 0, cached = 0, out = 0 } = usage;
  const usd = (i * PRICE.in + cached * PRICE.cached + out * PRICE.out) / 1e6;
  return Number(usd.toFixed(6));
}
function summary(records) {
  const by = new Map();
  for (const r of records) {
    const s = by.get(r.taskType) ?? { n: 0, usd: 0 };
    s.n++; s.usd += cost(r.usage);
    by.set(r.taskType, s);
  }
  return [...by].map(([k, v]) => ({ taskType: k, requests: v.n, usd: +v.usd.toFixed(4) }));
}
console.log(cost({ in: 1_000_000, cached: 500_000, out: 100_000 })); // 3.9
console.log(summary([
  { taskType: 'review', usage: { in: 1e6, out: 1e5 } },
  { taskType: 'review', usage: { in: 1e6, out: 1e5 } },
])); // review: 2 requests, usd 7.2

```

**评分点**：
- 三档单价分别计价再相加——缓存部分不能重复计全价。
- 精度处理：浮点误差用整数微美元或 fixed+parseFloat 处理。
- summary 聚合按 taskType 分组求和与请求数。
- 负数/缺省字段防御。
