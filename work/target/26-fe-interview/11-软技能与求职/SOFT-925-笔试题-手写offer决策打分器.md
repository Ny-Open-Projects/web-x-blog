---
title: [925] 笔试手写：实现加权多 offer 对比打分器
date: 2026-11-17
categories: [软技能与求职]
tags: [前端面试, 面试题, 跳槽策略]
type: 面试题
---

## 925：笔试手写：实现加权多 offer 对比打分器

**答**：实现 rankOffers(offers, weights)：offers 为 { name, dims: { cash, growth, risk, life } }[]（各维度 0~10 分），weights 为 { cash: 0.4, ... }。计算每个 offer 加权总分（保留 2 位），按总分降序输出 [{ name, total }]；维度缺失按 0 分处理并标注 warnings。

```js
function rankOffers(offers, weights) {
  return offers.map(o => {
    let total = 0; const missing = [];
    for (const [k, w] of Object.entries(weights)) {
      const v = o.dims[k];
      if (v === undefined) { missing.push(k); continue; } // 缺维度按0
      total += v * w;
    }
    return { name: o.name, total: +total.toFixed(2), missing };
  }).sort((a, b) => b.total - a.total);
}
const w = { cash: 0.4, growth: 0.3, risk: 0.2, life: 0.1 };
console.log(rankOffers([
  { name: 'A', dims: { cash: 9, growth: 7, risk: 6, life: 5 } },
  { name: 'B', dims: { cash: 8, growth: 9, risk: 7 } },   // life 缺失
], w));
// [ { name:'A', total: 7.2 }, { name:'B', total: 7.3, missing:['life'] } ]
```

**评分点**：
- 加权计算与降序排序正确；缺失维度按 0 处理且记录 missing（决策透明）
- 精度处理统一
- 能讨论：权重应由决策者自定（先定权重再看数据防倒推）、缺失维度补估 vs 置零的决策含义

