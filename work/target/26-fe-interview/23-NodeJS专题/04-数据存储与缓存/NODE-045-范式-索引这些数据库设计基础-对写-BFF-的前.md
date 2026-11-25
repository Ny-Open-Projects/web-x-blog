---
title: [NODE-045] 范式、索引这些数据库设计基础，对写 BFF 的前端有什么意义？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-045：范式、索引这些数据库设计基础，对写 BFF 的前端有什么意义？
**答**：
- BFF 不是只搬运数据：**慢 SQL 会拖垮 BFF 的超时预算**。前端工程师要能读懂执行计划、知道为什么列表页要分页要索引。
- 范式（1NF 原子性/2NF 消除部分依赖/3NF 消除传递依赖）：OLTP 遵循 3NF 减少冗余；但 BFF 常接触的**读密集报表/详情页反而要反范式**（冗余字段、宽表），用空间换 join。
- 索引要点：最左前缀（联合索引 `(uid, status, created_at)` 查 `uid+status` 才生效）、覆盖索引免回表、`LIKE '%x'` 不走索引、`ORDER BY` 与索引顺序一致避免 filesort、区分度低的列（如性别）建索引意义小。

```sql
-- BFF 接口"我的订单列表"背后的 SQL 与索引设计
-- SELECT id, status, amount, created_at FROM orders
-- WHERE uid = 42 AND status = 'paid'
-- ORDER BY created_at DESC LIMIT 20 OFFSET 0;

-- 联合索引：等值列在前，排序列在后
ALTER TABLE orders ADD INDEX idx_uid_status_created (uid, status, created_at);
-- EXPLAIN 确认：type=ref, key=idx_uid_status_created, Extra 无 filesort

-- 深分页优化：OFFSET 100000 会扫描并丢弃 10 万行，改用游标分页
-- SELECT id, status, amount FROM orders
-- WHERE uid = 42 AND id < 987654      -- 上一页最后一条的 id（游标）
-- ORDER BY id DESC LIMIT 20;
```

```javascript
// BFF 侧配合：游标分页 + 强制 LIMIT 上限
app.get('/api/orders', async (ctx) => {
  const { cursor, size = 20 } = ctx.query;
  const pageSize = Math.min(parseInt(size), 50);   // 钳制上限，防一次拉全表
  const rows = await query(
    `SELECT id, status, amount, created_at FROM orders
     WHERE uid = ? ${cursor ? 'AND id < ?' : ''} ORDER BY id DESC LIMIT ?`,
    cursor ? [ctx.state.user.uid, Number(cursor), pageSize] : [ctx.state.user.uid, pageSize],
  );
  ctx.body = { data: rows, nextCursor: rows.length === pageSize ? rows[rows.length - 1].id : null };
});
```

---

## 七、BFF 架构
