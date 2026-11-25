---
title: [1060] 笔试手写：实现版本对比的 Elo 积分与排名
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, 评测, Elo]
type: 笔试题
---

## 1060：笔试手写：实现版本对比的 Elo 积分与排名

**答**：实现 elo(games, k=32, base=1500)：games 为 { a, b, winner: 'a'|'b'|'tie' }[]（胜负对打分）。实现积分更新（预期胜率 E = 1/(1+10^((Rb-Ra)/400))），tie 双方各得期望值的一半差值；返回按积分降序的排名 [{ name, rating }]（初始 1500）。

```js
function elo(games, k = 32, base = 1500) {
  const r = {};
  const E = (ra, rb) => 1 / (1 + 10 ** ((rb - ra) / 400));
  const upd = (n, d) => (r[n] ??= base) + (r[d] === undefined ? 0 : 0);
  for (const g of games) {
    (r[g.a] ??= base); (r[g.b] ??= base);
    const expA = E(r[g.a], r[g.b]);
    const sa = g.winner === 'a' ? 1 : g.winner === 'b' ? 0 : 0.5;
    r[g.a] += k * (sa - expA);
    r[g.b] += k * ((1 - sa) - (1 - expA));
  }
  return Object.entries(r)
    .map(([name, rating]) => ({ name, rating: Math.round(rating) }))
    .sort((x, y) => y.rating - x.rating);
}
console.log(elo([
  { a: 'v1', b: 'v2', winner: 'a' }, { a: 'v1', b: 'v2', winner: 'b' },
  { a: 'v1', b: 'v2', winner: 'tie' },
])); // v1 约 1509, v2 约 1491
```

**评分点**：
- 期望胜率公式与 400 分母正确（最容易写错）
- tie 的 sa=0.5 处理，双方对称更新
- 动态初始化（首次出现的选手 base 分）
- 能讨论：k 值含义（新版本可设大 k 快速收敛）、样本量不足时排名置信度低（配对比较次数应均衡）

