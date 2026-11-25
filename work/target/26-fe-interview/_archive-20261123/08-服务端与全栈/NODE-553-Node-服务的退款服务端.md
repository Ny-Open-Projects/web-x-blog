---
title: [NODE-553] Node 服务的退款服务端（拆分退/渠道退/冲正）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-553：退款服务端
**答**:
- 退款模型：退款单（原支付单 → 退款记录：金额/渠道/状态）——拆分退（多渠道组合支付按原路各自退 ARC-625）、部分退（多次退款累计 ≤ 已付）、冲正（积分/优惠连带退还——退款联动规则）。
- 状态机：申请 → 处理中 → 渠道处理中 → 成功/失败——渠道异步回执驱动（query 兜底轮询——渠道且回调 ARC-542 思路）；失败重试（渠道失败 → 自动重试 N 次 → 人工通道）。
- 资金一致性：退款与余额/积分同事务冲正（退到余额——钱包入账同事务）、退款限额校验（可退金额 = 已付 - 已退——条件更新防超退）。
- 幂等：退款单幂等（同售后单唯一）、渠道退款幂等键（渠道侧防重复退）。
- 对账：退款对账（渠道退款单 vs 平台退款单——在途退款（渠道处理中）的对账容差窗口——时效差是常态，超时效才告警）。
```javascript
async function refund(refundId) {
  const r = await refundRepo.get(refundId);
  if (r.state === 'done') return done(r);                        // 幂等
  const res = await adapter(r.channel).refund({ amount: r.amount, outRefundNo: r.id,
    idempotencyKey: r.id });
  await refundRepo.updateState(r.id, mapState(res));             // 统一状态机
  if (res.state === 'success') await settleToWallet(r);          // 退余额同事务冲正
}
```
