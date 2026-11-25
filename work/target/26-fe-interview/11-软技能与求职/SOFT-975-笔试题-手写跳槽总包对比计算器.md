---
title: [975] 笔试手写：实现跳槽总包的三年现金流对比计算
date: 2026-11-17
categories: [软技能与求职]
tags: [前端面试, 面试题, 跳槽策略]
type: 面试题
---

## 975：笔试手写：实现跳槽总包的三年现金流对比计算

**答**：实现 compare3y(cur, next)：cur = { base, bonusRate, stock: { annual } }；next = { base, bonusRate, stock: { annual, cliffMonths }, signon: { amount, spreadMonths } }。按 36 个月逐月现金流计算两边总收入：股票按年额逐月摊入（next 在 cliff 月内为 0），signon 在 spreadMonths 内摊入。返回 { cur3y, next3y, delta }（取整）。

```js
function compare3y(cur, next) {
  let curSum = 0, nextSum = 0;
  for (let m = 1; m <= 36; m++) {
    curSum += cur.base + cur.base * cur.bonusRate / 12;
    if (cur.stock) curSum += cur.stock.annual / 12;
    nextSum += next.base + next.base * next.bonusRate / 12;
    if (m > (next.stock?.cliffMonths ?? 0)) nextSum += (next.stock?.annual ?? 0) / 12;
    if (m <= (next.signon?.spreadMonths ?? 0))
      nextSum += next.signon.amount / next.signon.spreadMonths;
  }
  return { cur3y: Math.round(curSum), next3y: Math.round(nextSum),
    delta: Math.round(nextSum - curSum) };
}
const cur = { base: 30000, bonusRate: 0.1, stock: { annual: 120000 } };
const next = { base: 36000, bonusRate: 0.15, stock: { annual: 180000, cliffMonths: 12 },
  signon: { amount: 60000, spreadMonths: 6 } };
console.log(compare3y(cur, next));
// cur3y = (30000+3000+10000)*36 = 1548000
// next3y = (36000+5400)*36 + 180000*2 + 60000 = 1489560
```

**评分点**：
- 逐月现金流模型正确（月薪+月摊奖金+月摊股票）
- cliff 处理：cliff 月内股票为 0，之后正常摊入
- signon 摊入 spreadMonths
- 能讨论：现司未 vest 股票的 forfeit 应作为跳槽隐性成本计入 delta、bonus 实际发放节奏与逐月摊的差异

