---
title: [NODE-195] 设计一个投票服务（防刷/统计/防提前开票）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-195：设计一个投票服务（防刷/统计/防提前开票）？
**答**：
- 幂等：`HSETNX poll:voted:{pollId} uid optionId` 一人一票原子判重；重复投票直接拒绝。
- 防刷四层：登录态 → 设备指纹 → IP 频控（NODE-132）→ 敏感活动行为验证码/实名；后台做速率突增告警与同 IP 段聚类。
- 统计：`HINCRBY` 计数 + 异步落库；UV 用 HyperLogLog；**防提前开票**：结果接口带开关，截止前只返回脱敏聚合或拒绝。
- 数据可审计：每票流水入库（uid/option/ip/ts），争议时可回放校正计数。

```javascript
async function vote(uid, pollId, optionId) {
  const isNew = await redis.hsetnx(`poll:voted:${pollId}`, uid, optionId); // 幂等判重
  if (!isNew) return { ok: false, msg: 'voted' };
  if (await riskBlocked(uid, pollId)) {               // 风控复核不过 → 撤销计数
    await redis.hdel(`poll:voted:${pollId}`, uid);
    return { ok: false, msg: 'risk' };
  }
  await redis.hincrby(`poll:count:${pollId}`, optionId, 1);
  await voteQueue.add('persist', { pollId, uid, optionId }); // 异步落库流水
  return { ok: true };
}

app.get('/api/poll/:id/result', async (ctx) => {
  const poll = await db.poll.findUnique({ where: { id: ctx.params.id } });
  if (poll.hideUntilResult && Date.now() < poll.endAt) {
    return (ctx.body = { hidden: true, endAt: poll.endAt });  // 防提前开票
  }
  ctx.body = await redis.hgetall(`poll:count:${poll.id}`);
});
```
