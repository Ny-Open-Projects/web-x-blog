---
title: [MFW-804] Server Action 里既要写库又要调外部 API（优惠券/支付），先后顺序怎么定
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-804：Server Action 里既要写库又要调外部 API（优惠券/支付），先后顺序怎么定

**答**：
- 结论：没有完美顺序，只有「哪种失败可补偿」：先本地提交后调外部→外部失败需补偿（发券回滚/冲正）；先调外部后本地提交→本地失败需撤销外部（退款），后者代价更高。
- 推荐：本地事务作为事实源先提交，外部调用走 Outbox 异步可靠送达 + 幂等键，把「外部一定成功」从事务里剥离。
- 追问钩子：什么时候必须先调外部？——外部是唯一权威且不可补偿（第三方扣款），此时本地只记「待确认」状态，用状态机 + 对账收敛。

```javascript
// 顺序 A（推荐）：本地先提交，外部走可靠异步
async function placeOrder(input) {
  'use server';
  const tx = await db.begin();
  try {
    const order = await tx.insert('orders', input);
    await tx.insert('outbox', { type: 'COUPON', orderId: order.id }); // 同事务
    await tx.commit();                            // 事实源已落库
    return { orderId: order.id, state: 'ACCEPTED' }; // 立即受理
  } catch (e) { await tx.rollback(); throw e; }
}

// 顺序 B（谨慎）：外部先，本地后 —— 本地失败要补偿外部
async function placeOrderStrict(input) {
  const pay = await payment.charge(input);        // 外部权威
  try { return await db.orders.create({ ...input, payId: pay.id }); }
  catch (e) { await payment.refund(pay.id); throw e; } // 补偿：退款
}
// 原则：把不可补偿的外部操作放在最后，并用状态机兜底对账
```
