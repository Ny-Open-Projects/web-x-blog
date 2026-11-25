---
title: [NODE-193] 设计一个签到与积分服务（bitmap/连续签到）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-193：设计一个签到与积分服务（bitmap/连续签到）？
**答**：
- bitmap 签到：1 用户 1 月 31 bit ≈ 4 字节，亿级用户内存可扛；`SETBIT day-1 1` 签到，`BITCOUNT` 月度统计。
- 连续签到：从当天往回 `GETBIT` 数到第一个 0；奖励规则（连 7 天翻倍）在服务端判定，不在客户端。
- 补签：指定位 `SETBIT` + 补签卡扣减，扣卡与置位要同事务（或本地消息表 NODE-146）。
- 积分：append-only 流水表 + 余额缓存，对账以流水为准。

```javascript
const key = (uid, ym) => `sign:${uid}:${ym}`;

async function checkin(uid) {
  const ym = dayjs().format('YYYYMM');
  const day = dayjs().date();                         // 1~31
  const isNew = (await redis.setbit(key(uid, ym), day - 1, 1)) === 0;
  if (!isNew) return { ok: false, msg: 'already' };
  let streak = 0;
  for (let i = day - 1; i >= 1; i--) {                // 从昨天往回数
    if (await redis.getbit(key(uid, ym), i - 1)) streak++;
    else break;
  }
  const points = streak + 1 >= 7 ? 10 : 1;            // 连签 7 天奖励
  await addPoints(uid, points, `checkin:${ym}:${day}`);
  return { ok: true, streak: streak + 1, points };
}
// 补签：SETBIT 指定位 + 补签卡原子扣减
// 月视图：GET 整月 bitmap 返回前端按位渲染
```
