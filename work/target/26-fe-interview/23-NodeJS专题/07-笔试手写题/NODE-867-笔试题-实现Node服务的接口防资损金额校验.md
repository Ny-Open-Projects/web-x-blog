---
title: [NODE-867] 笔试题——实现接口防资损金额校验（双源比对）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-867：手写金额校验

**需求与边界**：
- 需求：防资损校验（SCN-联想-520/854）——① 金额双源校验（提交金额 vs 服务端计算——SCN-联想-520 双源）；② 优惠叠加校验（服务端算优惠——SCN-联想-854 前端不算价）；③ 金额突变监控（订单金额分布——SCN-联想-900 分布突变）；④ 校验失败阻断 + 审计（资损防御——SCN-联想-854 防线）。
- 边界：① 服务端权威计算（优惠/价格——SCN-联想-854）；② 校验失败的错误语义（客户端可修 vs 系统异常——SCN-NODE-676 分级）；③ 金额精度（整数分——SCN-FIN-538）。

**答**：
```javascript
async function verifyAmount(order) {
  const expected = await priceService.calculate(order);   // 服务端权威计算（SCN-联想-854）
  const actual = parseFen(order.clientAmount);         // 客户端提交（整数分——SCN-FIN-538）
  if (actual !== expected.fen) {                       // 双源校验（SCN-联想-520）
    audit({ type: 'AMOUNT_MISMATCH', orderId: order.id, expected: expected.fen, actual });
    return { blocked: true, expected: expected.fen,   // 阻断 + 返回正确金额
      code: 'AMOUNT_MISMATCH', retryable: true };     // 客户端可修（SCN-NODE-676 分级）
  }
  const promoCheck = await verifyPromotions(order);    // 优惠叠加校验（SCN-联想-854 服务端算）
  return { blocked: false, verified: { promo: promoCheck.passed } };
}
// 金额分布突变监控（SCN-联想-900）
monitor.amountDistribution(orderAmounts, { chiThreshold: 50 });
```

**评分点**:
- 服务端权威计算（前端不算价——SCN-联想-854）。
- 双源校验 + 整数分（SCN-联想-520/538）。
- 金额分布突变监控（SCN-联想-900 卡方）。
- 校验失败分级（客户端可修——SCN-NODE-676）。
