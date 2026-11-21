---
title: [NODE-164] 设计一个支付回调处理（重试/幂等/对账）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-164：设计一个支付回调处理（重试/幂等/对账）？
**答**：
- 处理四步：**验签**（防伪造，raw body 校验）→ **幂等**（状态机 CAS：PENDING→PAID 只会成功一次，重复回调直接 ACK）→ **同事务发后续事件**（outbox，NODE-146）→ **按协议应答**（success 停止重试，5xx 触发渠道退避重试）。
- 重试是渠道行为：设计要主动配合——处理失败返回 5xx 让渠道重试，但下游事件必须幂等。
- 对账兜底：每日 T+1 拉渠道账单 vs 本地流水 diff，差异生成工单；掉单场景（回调丢了）靠**主动查单**补偿。
- 红线：回调处理必须快（渠道有超时），重活（发货/通知）一律异步化。

```javascript
app.post('/pay/callback', express.raw({ type: '*/*' }), async (ctx) => {
  const evt = JSON.parse(ctx.request.body);
  if (!verifySignature(ctx.request.body, ctx.get('x-signature'), PAY_SECRET)) {
    return ctx.throw(401);                                   // 1. 验签
  }
  const handled = await db.$transaction(async (tx) => {
    const updated = await tx.payment.updateMany({            // 2. 幂等：CAS 状态机
      where: { orderId: evt.orderId, status: 'PENDING' },
      data: { status: 'PAID', paidAt: new Date(), channelTradeNo: evt.tradeNo },
    });
    if (updated.count === 0) return false;                   // 重复回调
    await tx.outbox.create({                                 // 3. 同事务发事件
      data: { bizId: evt.orderId, payload: JSON.stringify(evt) },
    });
    return true;
  });
  ctx.status = 200; ctx.body = 'success';                    // 4. ACK 停止渠道重试
});
// 主动查单兜底掉单：每 5min 扫 PENDING 超过 10min 的单，调渠道查单接口对齐状态
// 对账：T+1 账单 diff → 差异表 → 财务工单
```
