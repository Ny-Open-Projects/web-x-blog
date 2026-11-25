---
title: [NODE-733] 笔试题——实现 outbox 投递器（本地消息表扫描）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-733：手写 outbox 投递器

**需求与边界**：
- 需求：本地消息表投递（SCN-NODE-653）——① 扫描未投递消息（FOR UPDATE SKIP LOCKED——多实例不重复投）；② 投递成功标记（幂等——SCN-NODE-655）；③ 失败退避重试（次数上限——超限告警人工）；④ 顺序保证（同聚合的事件按序——分片按聚合 ID）。
- 边界：① SKIP LOCKED（多实例并发扫描不重复——SCN-FIN-755 同构）；② 投递至少一次（消费端幂等——SCN-NODE-651）；③ 批量投递性能（batch + 部分失败处理）。

**答**：
```javascript
async function outboxFlusher({ batch = 100 } = {}) {
  const rows = await db.query(`SELECT * FROM outbox WHERE delivered = false
    ORDER BY id LIMIT $1 FOR UPDATE SKIP LOCKED`, [batch]);   // 多实例不重复
  for (const row of rows) {
    try {
      await mq.publish(row.topic, row.payload, { key: row.aggId });   // 同聚合同分区（顺序）
      await db.query('UPDATE outbox SET delivered = true, delivered_at = now() WHERE id = $1', [row.id]);
    } catch (e) {
      const attempts = row.attempts + 1;
      if (attempts > 10) {                             // 超限告警人工
        await db.query('UPDATE outbox SET dead = true WHERE id = $1', [row.id]);
        alert({ type: 'OUTBOX_DEAD', id: row.id, topic: row.topic });
      } else
        await db.query('UPDATE outbox SET attempts = $1, next_retry = now() + interval $2 WHERE id = $3',
          [attempts, backoff(attempts), row.id]);      // 退避重试
    }
  }
}
cron('*/2s', outboxFlusher);                           // 2s 扫描（秒级延迟）
```

**评分点**:
- FOR UPDATE SKIP LOCKED（多实例并发不重复投——SCN-FIN-755）。
- 同聚合 ID 分区 key（事件顺序保证——SCN-NODE-651）。
- 退避重试 + 超限死信告警（人工兜底）。
- 投递成功幂等标记（断点续投——进程重启不重复）。
