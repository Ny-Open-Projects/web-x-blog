---
title: [NODE-565] Node 服务的签到与任务系统（频控/补签/奖励）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-565：签到与任务系统
**答**:
- 签到模型：日历签到（业务日切——时区 ARC-481）、连续签到（连签计数——断签重置规则）、补签（补签卡——扣卡补签事务）。
- 防作弊：签到频控（同日一次——业务日唯一索引幂等）、异常模式（定点秒签/多设备同签——风控标记 NODE-456）、时间信任（服务端时间权威——客户端时钟不可信）。
- 任务系统：任务定义（每日任务/新手任务——任务配置版本化）、完成判定（事件驱动：浏览/下单/分享——事件幂等计入 NODE-488）、奖励发放（积分/券——联动对应服务 NODE-550/556 幂等发放）。
- 性能：签到热点（整点集中签到——热点账户拆分 ARC-520/预聚合计数）、任务列表批量（用户任务面板一次查询聚合）。
- 一致性：连签计数与日历对齐（跨月连签规则）、补签不破坏原日幂等（补签独立流水标记）。
```javascript
// 签到（业务日幂等）
const bizDay = bizDayOf(serverNow(), 'Asia/Shanghai');           // 业务日切
await db.tx(t => {
  await t.query(`insert into checkin(uid, biz_day) values($1,$2)
    on conflict (uid, biz_day) do nothing`, [uid, bizDay]);     // 业务日唯一
  await streak.inc(uid, bizDay);                                 // 连签（断签规则）
  await points.grant(uid, rewardFor(streak), { src: `checkin:${bizDay}` });
});
```
