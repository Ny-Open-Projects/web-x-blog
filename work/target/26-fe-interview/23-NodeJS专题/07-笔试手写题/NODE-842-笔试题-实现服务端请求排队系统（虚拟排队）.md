---
title: [NODE-842] 笔试题——实现服务端虚拟排队（令牌发放 + 放行速率）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-842：手写虚拟排队

**需求与边界**：
- 需求：服务端排队（SCN-联想-855 服务端版）——① 排队登记（Redis ZSET 位置——SCN-联想-855 排队页服务端）；② 放行速率（令牌桶恒速放行——系统容量匹配，SCN-NODE-641）；③ 位置查询与 ETA（SCN-联想-855）；④ 排队 token 生命周期（SCN-联想-890 续期/过期）。
- 边界：① 排队公平性（先到先得——ZSET score 时间戳）；② 超时退出（token 过期自动移除——SCN-联想-890）；③ 放行速率动态调整（下游容量——SCN-NODE-699）。

**答**：
```javascript
async function joinQueue(activityId, userId) {
  const key = `queue:${activityId}`;
  const added = await redis.zadd(key, Date.now(), userId);   // 先到先得（score 时间戳）
  if (!added) return { position: await rank(key, userId) };   // 重复登记：返回位置
  await redis.setex(`qt:${userId}`, 600, signToken(userId));  // token（SCN-联想-890 10min）
  return { position: await rank(key, userId) };
}
// 放行（令牌桶恒速——SCN-NODE-641）
cron('*/500ms', async () => {
  const permits = await tokenBucket.take(rate = capacityPerSec);
  const next = await redis.zrange(`queue:${activityId}`, 0, permits - 1);
  next.forEach(u => { redis.publish(`admit:${activityId}`, u); removeQueue(u); });   // 放行通知
});
function position(userId) {                            // ETA（SCN-联想-855）
  return { pos: rank(userId), eta: rank(userId) / capacityPerSec * 1000 };
}
```

**评分点**:
- ZSET 先到先得（公平性——score 时间戳）。
- 令牌桶恒速放行（下游容量匹配——SCN-NODE-641/699）。
- token 生命周期（10min 过期——SCN-联想-890）。
- 位置/ETA 查询（SCN-联想-855 排队页服务端）。
