---
title: [NODE-554] Node 服务的结算服务（账期/分账/出账）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-554：结算服务
**答**:
- 结算模型：账期（订单完成 → 结算周期 → 生成结算单：收入 - 扣项（佣金/退款/罚扣）= 应结——明细构成可追溯 ARC-612）、分账（多角色拆分规则引擎——规则配置化版本化）。
- 结算流程：定时结算任务（NODE-437 编排：账期到期 → 汇总 → 生成结算单 → 审核（大额人工复核）→ 打款/入钱包）、结算幂等（账期+商家唯一——重跑不重复出账）、冲正（结算后发现错账 → 冲销单——负向流水，不修改已出结算单）。
- 一致性：结算金额与流水对账（结算单 = 流水聚合——差异告警）、结算与钱包/银行通道的对账（打款回执核对）。
- 例外治理：扣项争议（商家申诉——申诉工单 → 调整单（带审批））、罚扣规则透明（每笔扣项带依据引用）。
- 观测：结算时效（账期到出账的时长）、结算差错率（冲销单占比——质量指标）。
```javascript
// 账期结算任务
async function settle(merchantId, period) {
  const flows = await ledgerRepo.byPeriod(merchantId, period);   // 流水聚合
  const bill = computeBill(flows, rules.current(merchantId));    // 佣金/扣项规则版本化
  await db.tx(t => insertSettlement(t, { merchantId, period, ...bill,
    idempotencyKey: `${merchantId}:${period}` }));               // 账期唯一幂等
  if (bill.net > LARGE) await reviewQueue.push(bill);            // 大额人工复核
  else await payout(bill);
}
```
