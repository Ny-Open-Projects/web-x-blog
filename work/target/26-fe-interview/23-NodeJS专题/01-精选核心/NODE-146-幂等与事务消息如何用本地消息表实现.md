---
title: [NODE-146] 幂等与事务消息如何用"本地消息表"实现？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-146：幂等与事务消息如何用"本地消息表"实现？
**答**：
- 问题："DB 写成功但 MQ 发送失败"会造成数据不一致；本地消息表把"发消息"变成**与业务同库同事务的写一行**，把分布式问题降级为本地事务。
- 流程：业务写 + outbox 写在同一个事务 → Relay 定时扫 `status=0` 投递 → 成功置 1，失败指数退避重试，超限进死信人工处理。
- 多实例并发扫描要加分布式锁（NODE-123）；投递是**至少一次**语义，消费端必须按 biz_id 幂等去重（NODE-076）。
- 表设计核心索引：`(status, next_retry_at)` 复合索引让扫描高效；payload 存完整消息体，重试不依赖上游状态。

```javascript
// outbox(id, biz_id, payload, status[0待投递/1成功/2死信], retry, next_retry_at)
async function createOrderTx(order) {
  const conn = await mysql.getConnection();
  try {
    await conn.beginTransaction();
    await conn.query('INSERT INTO orders (id, uid, amount) VALUES (?, ?, ?)',
      [order.id, order.uid, order.amount]);                          // 业务写
    await conn.query(
      'INSERT INTO outbox (biz_id, payload, status) VALUES (?, ?, 0)',
      [order.id, JSON.stringify({ event: 'order.created', order })]); // 同事务写消息
    await conn.commit();
  } catch (e) { await conn.rollback(); throw e; }
  finally { conn.release(); }
}

// Relay：定时扫描投递（多实例需先抢分布式锁）
setInterval(async () => {
  const got = await redis.set('lock:outbox-relay', '1', 'PX', 50_000, 'NX');
  if (!got) return;
  const rows = await db.query(
    'SELECT * FROM outbox WHERE status = 0 AND next_retry_at <= NOW() LIMIT 100');
  for (const row of rows) {
    try {
      await mq.publish('order.events', row.payload);
      await db.query('UPDATE outbox SET status = 1 WHERE id = ?', [row.id]);
    } catch {
      await db.query(`UPDATE outbox SET retry = retry + 1,
        next_retry_at = DATE_ADD(NOW(), INTERVAL 30 SECOND),
        status = IF(retry >= 5, 2, 0) WHERE id = ?`, [row.id]);
    }
  }
}, 1000);
```

---

## 十八、微服务与协作

## 追问（补充）

**追问**：

1. Relay 高频扫表把 DB 拖慢怎么办 → 只走 (status, next_retry_at) 覆盖索引、每批 200 条、按 id 游标翻页而不是 offset，扫空后 sleep 200ms 再扫，多实例再加分布式锁保证同一时刻只有一个 Relay 在跑，避免空转打满 IO。
2. 投递成功但置 status=1 失败，下一轮重复投递会出问题吗 → 不会，靠消费端按 biz_id 幂等去重直接 ACK，生产者只保证至少一次，绝不指望它做到恰好一次。
3. outbox 表无限增长怎么治理 → 成功记录保留 7 天后归档或按天分区直接 drop 分区，删除也走小批量，避免一条大 DELETE 长时间锁表。
