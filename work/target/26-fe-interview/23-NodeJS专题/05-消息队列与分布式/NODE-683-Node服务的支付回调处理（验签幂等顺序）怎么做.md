---
title: [NODE-683] 支付回调处理（验签/幂等/乱序）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-683：支付回调怎么做？
**答**：
- 验签：回调验签（渠道签名算法——防伪造回调）；签名校验失败不处理（静默 4xx——不给探测者信息，SCN-联想-814 平静原则）。
- 幂等：回调重发（渠道 at-least-once——幂等键 = 渠道流水号唯一约束，SCN-NODE-655 存储层幂等）；重复回调返回成功（渠道停止重发）。
- 乱序与终态：回调可能乱序（成功先于退款通知）——version/ts 单调守卫（SCN-FIN-548 状态机渲染）；终态后回调不改变状态（终态幂等）。
- 处理时序：验签 → 幂等检查 → 业务处理（本地事务：订单状态 + 消息表——SCN-NODE-653 本地消息表）→ 快速 ack（渠道超时会重发——处理要快或异步化）。
- 追问钩子：为什么回调处理要「快速 ack + 异步业务」——渠道回调有超时（通常几秒），超时渠道重发（风暴）；同步做重业务（发货/积分）会超时——回调只做「验签+幂等+落库+投递 MQ」毫秒级，重业务由 MQ 消费异步做——回调入口的职责最小化是支付稳定性的关键。

```javascript
app.post('/pay/callback', async (req, res) => {
  if (!verifySign(req.body)) return res.status(400).end();       // 验签失败静默
  const dup = await db.query('SELECT 1 FROM cb WHERE ch_no=$1', [req.body.chNo]);
  if (dup.rowCount) return res.ok();                   // 幂等：重复回调返回成功
  await db.transaction(async (tx) => {
    await tx.insertCb(req.body);                       // 回调落库
    await tx.insertOutbox({ topic: 'pay.success', payload: req.body });   // 本地消息表
  });
  res.ok();                                            // 快速 ack（重业务异步）
});
```
