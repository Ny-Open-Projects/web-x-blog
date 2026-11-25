---
title: [1227] 笔试手写：实现影子流量的胜率与显著性简化判定
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, 评测]
type: 笔试题
---

## 1227：笔试手写：实现影子流量的胜率与显著性简化判定

**需求**：实现 shadowWinRate(pairs)：pairs 为 { intent, winner: 'cand'|'prod'|'tie' }[]。输出 { overall: cand 胜率（tie 不计入分母，3 位）, byIntent, sufficient: 样本量是否 >= 每意图 30（不足列 intent） }。

```js
function shadowWinRate(pairs, minPerIntent = 30) {
  const byIntent = {};
  for (const p of pairs) {
    const g = (byIntent[p.intent] ??= { cand: 0, decided: 0 });
    if (p.winner === 'cand') g.cand++;
    if (p.winner !== 'tie') g.decided++;          // tie 不进分母
  }
  const bi = {};
  const insufficient = [];
  for (const [k, v] of Object.entries(byIntent)) {
    bi[k] = { winRate: v.decided ? +(v.cand / v.decided).toFixed(3) : null, n: v.decided };
    if (v.decided < minPerIntent) insufficient.push(k);
  }
  const total = pairs.filter(p => p.winner !== 'tie').length;
  const candWins = pairs.filter(p => p.winner === 'cand').length;
  return { overall: total ? +(candWins / total).toFixed(3) : null,
    byIntent: bi, insufficient };
}
const pairs = [
  { intent: 'qa', winner: 'cand' }, { intent: 'qa', winner: 'prod' },
  { intent: 'qa', winner: 'tie' }, { intent: 'code', winner: 'cand' },
];
console.log(shadowWinRate(pairs, 5));
// overall 0.667；qa 0.5（n=2 <5 -> insufficient ['qa']）
```

**评分点**：
- tie 不进分母（胜率语义正确）
- 样本充分性检查（minPerIntent——不足禁下结论）
- 除零 null 保护
- 能讨论：胜率到灰度提权的联动、显著性的进阶（二项检验）

