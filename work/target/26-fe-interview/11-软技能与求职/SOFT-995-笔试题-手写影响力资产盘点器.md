---
title: [995] 笔试手写：实现季度影响力资产的统计与评级
date: 2026-11-17
categories: [软技能与求职]
tags: [前端面试, 面试题, 影响力经营]
type: 面试题
---

## 995：笔试手写：实现季度影响力资产的统计与评级

**答**：实现 impact(assets)：assets 为 { type: 'ref'|'adopt'|'share'|'mentor', count }[]。权重 ref=3, adopt=5, share=1, mentor=4；总分 = Σ count*weight；评级：>=100 'strong'，>=60 'growing'，>=20 'seed'，否则 'seedling'。输出 { total, level, breakdown }（breakdown 为各 type 加权贡献占比，保留 3 位，零贡献类型不给占比；total 为 0 时 breakdown 为空对象）。

```js
const W = { ref: 3, adopt: 5, share: 1, mentor: 4 };
function impact(assets) {
  let total = 0; const contrib = {};
  for (const a of assets) {
    const w = W[a.type] ?? 0;
    const c = (a.count || 0) * w;
    contrib[a.type] = (contrib[a.type] || 0) + c;
    total += c;
  }
  const breakdown = {};
  if (total > 0) {
    for (const [k, v] of Object.entries(contrib)) {
      if (v > 0) breakdown[k] = +(v / total).toFixed(3);
    }
  }
  const level = total >= 100 ? 'strong' : total >= 60 ? 'growing'
    : total >= 20 ? 'seed' : 'seedling';
  return { total, level, breakdown };
}
console.log(impact([{ type: 'adopt', count: 4 }, { type: 'share', count: 10 }]));
// total 30, level 'seed', breakdown { adopt: 0.667, share: 0.333 }
```

**评分点**：
- 权重表与总分计算正确；未知 type 权重按 0（鲁棒）
- breakdown 只给正贡献类型，total 为 0 时除零保护
- 评级区间边界（>=）语义一致
- 能讨论：盘点的用途（季度自查看趋势）、权重随职业阶段调整（早期 share 便宜、后期 adopt 才值钱）

