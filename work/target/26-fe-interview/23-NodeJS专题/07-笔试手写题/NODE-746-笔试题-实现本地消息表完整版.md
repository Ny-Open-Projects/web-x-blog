---
title: [NODE-746] 笔试题——实现本地消息表完整版（同事务写入 + 顺序投递）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-746：手写本地消息表

**需求与边界**：
- 需求：事务内写消息表（SCN-NODE-653/733）——① 业务写入与消息写入同事务（原子性核心）；② 投递器 SKIP LOCKED 多实例（SCN-NODE-733）；③ 顺序投递（同聚合 ID 按序——分区 key）；④ schema 版本（事件演进——SCN-NODE-713）。
- 边界：① 消息表膨胀治理（已投递清理——TTL）；② 消费端幂等（at-least-once——SCN-NODE-651）；③ 死信（SCN-NODE-733 超限告警）。

**答**：
```javascript
// 1. 同事务写入（原子性核心）
await db.transaction(async (tx) => {
  await tx.query('INSERT INTO orders ...', [order]);
  await tx.query(`INSERT INTO outbox (topic, agg_id, payload, schema_ver)
    VALUES ('order.created', $1, $2, 'v2')`, [order.id, JSON.stringify(event)]);   // 同事务
});
// 2. 投递器（SCN-NODE-733 SKIP LOCKED + 顺序）
async function flush() {
  const rows = await db.query(`SELECT * FROM outbox WHERE delivered = false
    AND next_retry <= now() ORDER BY agg_id, id LIMIT 100 FOR UPDATE SKIP LOCKED`);
  for (const r of rows)
    try { await mq.publish(r.topic, { ...JSON.parse(r.payload), _ver: r.schemaVer },
      { key: r.agg_id });                                   // 同聚合同分区（顺序）
      markDelivered(r.id); }
    catch (e) { markRetry(r, e); }                     // 退避/死信（SCN-NODE-733）
}
// 3. 清理（膨胀治理）
cron('0 3 * * *', () => db.query(
  `DELETE FROM outbox WHERE delivered = true AND delivered_at < now() - interval '7 days'`));
```

**评分点**:
- 同事务写入（原子性——本地消息表的核心价值）。
- SKIP LOCKED 多实例 + 同聚合顺序（分区 key——SCN-NODE-733）。
- schema 版本携带（事件演进——SCN-NODE-713 消费者兼容）。
- 已投递清理（表膨胀治理）。
