---
title: [NODE-283] 消息幂等消费的实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-283：消息幂等消费的实现？
**答**:
- at-least-once 语义下重复消息必然出现——消费端幂等是标配。
- 方案一：唯一键去重表（消息 id 唯一索引，重复插入报错即跳过）；方案二：状态机幂等（订单只能从 paid → shipped，重复消息落回退路径）；方案三：Redis SETNX 短 TTL 去重（轻量但可能丢——不作为唯一防线）。
- 组合：Redis 快筛（挡 99% 重复）+ DB 唯一键兜底（剩余 1%）。
- 消费顺序：同 key 顺序敏感的业务（订单状态流）按分区 key 保证（Kafka）或 BullMQ 按 group 串行。

```javascript
// 幂等消费（Redis 快筛 + DB 兜底）
async function consume(msg) {
  const ok = await redis.set(`dedup:${msg.id}`, 1, { nx: true, ex: 86400 });
  if (!ok) return;                                  // 重复：直接跳过
  try {
    await db.transaction(async (tx) => {
      await tx.execute('INSERT INTO consumed (msg_id) VALUES (?)', [msg.id]);   // 唯一索引兜底
      await apply(msg, tx);                          // 状态机更新
    });
  } catch (e) {
    if (isDuplicateKey(e)) return;                   // 兜底命中：并发重复
    await redis.del(`dedup:${msg.id}`);              // 失败释放，允许重试
    throw e;
  }
}
```
