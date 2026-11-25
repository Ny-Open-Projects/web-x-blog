---
title: [NODE-556] Node 服务的优惠券服务端（发放/核销/分摊）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-556：优惠券服务端
**答**:
- 模型：券模板（规则：门槛/面额/适用范围/叠加规则/有效期）+ 用户券（领取 → 使用/过期——用户券状态机）。发放：活动发放（配额限量——库存原子扣减防超发 NODE-412）、定向发放（人群圈选批量——异步任务）、兑换码（防爆破——码表哈希）。
- 核销：下单用券（预核销 → 订单支付成功核销 / 订单关闭退回——两阶段冻结语义 ARC-551）、核销幂等（券状态条件更新：used 前置态才可核销）、分摊（跨店满减按比例分摊到商品行——分摊算法服务端，明细可解释 ARC-644）。
- 可用性判断：券选择器（NODE-600）服务端计算（叠加规则/互斥规则引擎——规则版本化）。
- 对账与防刷：发用对账（发放量 vs 核销量 vs 过期量——流水对账）、薅券风控（批量领券模式识别 NODE-456）、成本对账（营销预算消耗——券核销金额统计）。
- 过期：过期批量任务（定时——过期券状态翻转 + 到期前提醒任务）。
```javascript
// 领券（库存原子）
const ok = await redis.eval(DECR_LUA, 1, `coupon:stock:${tplId}`);   // 限量原子扣
if (!ok) throw new SoldOut();
await db.tx(t => t.query(`insert into user_coupon(tpl_id, uid, state) values($1,$2,'valid')
  on conflict (tpl_id, uid) do nothing`, [tplId, uid]));             // 每人限领幂等
// 核销：update user_coupon set state='used' where id=$1 and state='frozen'  —— 条件更新
```
