---
title: [MFW-811] Server Action 的幂等键与业务写入不在同一事务，会出现什么双写问题
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-811：Server Action 的幂等键与业务写入不在同一事务，会出现什么双写问题

**答**：
- 结论：幂等记录必须与业务写入「同事务提交」，否则并发重试会在「查幂等表(不存在)→执行业务」窗口内 double-execute。
- 方案：用 DB 唯一约束 + INSERT ON CONFLICT DO NOTHING 把「检查+占位」原子化；命中冲突时读已完成结果直接回放。
- 追问钩子：为什么不能只用 Redis SETNX？——跨存储无法与 DB 事务原子提交；Redis 占位成功但 DB 写失败时，幂等键已占住，业务永远不执行。

```javascript
// ❌ 危险：先查 Redis 幂等键，再写 DB —— 两步非原子
async function bad(reqId) {
  if (await redis.get(reqId)) return;
  await redis.set(reqId, '1');                     // 占位
  await db.orders.create(/* ... */);               // 若这里失败，键已占死
}

// ✅ 正确：幂等记录与业务写入同一本地事务
async function good(reqId, order) {
  'use server';
  const tx = await db.begin();
  try {
    const inserted = await tx.insert('idem', { key: reqId, state: 'pending' })
                               .onConflict('key').doNothing();
    if (!inserted) {                               // 重复请求
      const row = await tx.one('SELECT result,state FROM idem WHERE key=?', [reqId]);
      await tx.commit();
      return row.state === 'done' ? row.result : { retry: true };
    }
    const result = await tx.insert('orders', order);
    await tx.exec('UPDATE idem SET state=?, result=? WHERE key=?',
                  ['done', JSON.stringify(result), reqId]);
    await tx.commit();                              // 幂等与业务原子提交
    return result;
  } catch (e) { await tx.rollback(); throw e; }
}
```
