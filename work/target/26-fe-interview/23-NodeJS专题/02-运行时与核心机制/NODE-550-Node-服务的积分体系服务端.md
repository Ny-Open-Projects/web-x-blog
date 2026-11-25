---
title: [NODE-550] Node 服务的积分体系（发放/消耗/对账）服务端如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-550：积分体系服务端
**答**:
- 模型：积分账户（余额）+ 流水（每笔变动：来源/数量/关联业务单——ARC-460 涉账铁律：余额与流水同源、服务端裁决）。
- 发放链路：事件驱动发放（订单完成/签到——事件消费幂等发放 NODE-488）、发放幂等（业务单号唯一索引——同订单不重复发）、批量发放（活动集中发放——异步任务限速 NODE-437）。
- 消耗链路：扣减事务（余额不足拒绝 + 条件更新 NODE-412）、过期机制（积分有效期——过期批量任务 + 到期提醒）、冻结语义（下单预扣积分——成功扣/失败解冻——两阶段）。
- 对账：日对账（流水累计 vs 余额快照——差异告警分级 NODE-538）、与外部积分互通（兑换第三方积分——外部对账双源）。
- 防刷：积分获取风控（异常获取模式：高频签到作弊——风控扣回与封禁 NODE-456）、积分作为资产的审计（变动审计留痕 NODE-442）。
```javascript
// 积分发放（事件幂等）
async function onOrderPaid(e) {
  const pts = rule.calc(e);
  await db.tx(t => {
    await t.query(`insert into points_flow(order_id, uid, delta) values($1,$2,$3)
      on conflict (order_id) do nothing`, [e.orderId, e.uid, pts]); // 幂等：订单唯一
    await t.query(`update points_account set balance = balance + $1
      where uid = $2`, [pts, e.uid]);                             // 同事务改余额
  });
}
```
