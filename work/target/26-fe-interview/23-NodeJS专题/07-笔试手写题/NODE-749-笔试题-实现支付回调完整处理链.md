---
title: [NODE-749] 笔试题——实现支付回调完整处理链（验签→幂等→事务→ack）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-749：手写支付回调链

**需求与边界**：
- 需求：支付回调完整链（SCN-NODE-683）——① 验签（静默拒绝）；② 幂等（渠道流水号唯一约束）；③ 终态守卫（version 单调——SCN-FIN-548）；④ 本地消息表（业务+消息同事务——SCN-NODE-653）；⑤ 快速 ack（<100ms——渠道重发防御）。
- 边界：① 验签失败静默（SCN-联想-814 平静原则）；② 处理超时降级（先落库 ack——业务异步补处理，SCN-NODE-683 入口最小化）；③ 回调与查询双通道（回调丢失 → 主动查询兜底——SCN-FIN-511 对账）。

**答**：
```javascript
app.post('/cb/pay/:channel', rawBody, async (req, res) => {
  const t0 = Date.now();
  if (!verifySign(req.channel, req.rawBody, req.headers)) {
    telemetry.push({ type: 'SIGN_FAIL', channel: req.channel });
    return res.status(400).end();                      // 验签失败静默（SCN-联想-814）
  }
  const evt = parse(req.rawBody);
  try {
    const status = await db.transaction(async (tx) => {
      const ins = await tx.query(`INSERT INTO pay_cb (ch_no, payload) VALUES ($1,$2)
        ON CONFLICT (ch_no) DO NOTHING RETURNING id`, [evt.chNo]);   // 幂等：唯一约束
      if (!ins.rowCount) return 'DUPLICATE';           // 重复：返回成功（渠道停发）
      const updated = await tx.query(`UPDATE orders SET status = 'PAID', version = version + 1
        WHERE order_id = $1 AND status IN ('CREATED','PAYING') RETURNING version`, [evt.orderId]);   // 终态守卫
      if (updated.rowCount) await tx.insertOutbox('pay.success', evt);   // 本地消息表
      return updated.rowCount ? 'APPLIED' : 'STALE';   // 终态后回调：不改变（SCN-FIN-548）
    });
    report({ channel: req.channel, status, ms: Date.now() - t0 });
    res.ok();                                          // 快速 ack（<100ms——SCN-NODE-683）
  } catch (e) {                                        // 处理超时：落原始报文 ack + 异步补处理
    await db.query('INSERT INTO cb_raw (payload) VALUES ($1)', [req.rawBody]);
    res.ok();                                          // 先 ack（渠道停止重发）
    queue.add('cb-reprocess', req.rawBody);            // 异步补处理
  }
});
```

**评分点**:
- 验签静默 + 幂等唯一约束（SCN-联想-814 / SCN-NODE-655）。
- version 终态守卫（乱序回调不改变状态——SCN-FIN-548）。
- 本地消息表同事务（业务+消息原子——SCN-NODE-653）。
- 超时降级链（落原始报文 ack + 异步补处理——处理入口最小化）。
