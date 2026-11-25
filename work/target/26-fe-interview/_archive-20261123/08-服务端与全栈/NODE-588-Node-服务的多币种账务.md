---
title: [NODE-588] Node 服务的多币种账务（记账/换汇/损益）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-588：多币种账务
**答**:
- 记账原则：原币记账（每笔交易记原币金额+币种——不预先换汇）+ 换汇显式（换汇作为独立账务事件：源币种出、目标币种入、汇率记录——损益可追溯）、汇总换算（报表按记账汇率折算——汇率版本化快照）。
- 换汇链路：锁定汇率（交易时锁定——支付按锁定汇率 ARC-569）、换汇损益（买入价/卖出价差——汇率波动损益单独科目）、汇率来源（多渠道汇率——聚合与缓存、汇率异常告警）。
- 一致性：币种精度（各币种 minor units——日元 0 位 ARC-569）、跨币种对账（各币种独立对账——不混算）、总账平衡（复式记账下多币种——折算后平衡校验）。
- 退款币种：原币退款（ARC-569 原路——换汇损失规则显式）。
- 审计：汇率来源审计（每次换汇记录汇率来源与时间——可复核）、损益报表（换汇损益独立报表）。
```javascript
// 换汇账务事件
async function exchange(from, to, rate) {
  await ledger.tx(t => {
    t.debit({ account: from.account, amount: from.amount, currency: from.currency });
    t.credit({ account: to.account, amount: to.amount, currency: to.currency });
    t.record({ type: 'fx', rate, source: rateSource, spread: spreadOf(rate) }); // 损益追溯
  });
}
```
