---
title: [NODE-869] 笔试题——实现优惠叠加计算器（服务端权威 + 校验）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-869：手写优惠计算

**需求与边界**：
- 需求：优惠叠加（SCN-联想-854/804）——① 优惠叠加规则（互斥/可叠加——规则表，SCN-联想-804 裁剪）；② 服务端权威计算（SCN-联想-854）；③ 计算的可解释（每项优惠的金额拆分——用户可见拆分）；④ 精度（整数分——SCN-FIN-538）。
- 边界：① 优惠互斥规则（满减与折扣互斥——规则引擎，SCN-NODE-686）；② 拆分精度（优惠分摊到行——尾差处理——SCN-FIN-538 整数分）；③ 优惠的防刷（发放限流——SCN-联想-854）。

**答**：
```javascript
const STACK_RULES = { fullReduction: { exclusiveWith: ['discount'] }, coupon: { stackable: true } };
function calcDiscounts(order, coupons) {
  let remaining = order.totalFen;
  const applied = [], breakdown = [];
  const eligible = coupons.sort(byPriority)            // 优先级（SCN-联想-854）
    .filter(c => !conflictsWith(c, applied, STACK_RULES));   // 互斥规则（SCN-NODE-686）
  for (const c of eligible) {
    const cut = c.calc(remaining);                     // 服务端权威计算（SCN-联想-854）
    if (cut <= 0) continue;
    applied.push(c); breakdown.push({ coupon: c.id, cut });
    remaining -= cut;
  }
  const split = splitToFen(breakdown, order.items);    // 分摊到行 + 尾差（SCN-FIN-538）
  return { totalCut: order.totalFen - remaining, breakdown: split, applied };
}
// 尾差处理：最后一行吸收尾差（保证 Σ行优惠 = 总优惠——SCN-FIN-538 精度）
```

**评分点**:
- 服务端权威计算（SCN-联想-854）。
- 互斥规则表 + 优先级（SCN-NODE-686 规则引擎联动）。
- 行级分摊 + 尾差吸收（SCN-FIN-538 整数分精度）。
- 计算可解释（breakdown 用户可见）。
