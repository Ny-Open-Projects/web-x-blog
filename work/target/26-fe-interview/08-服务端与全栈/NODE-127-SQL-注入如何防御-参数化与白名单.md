---
title: [NODE-127] SQL 注入如何防御（参数化与白名单）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-127：SQL 注入如何防御（参数化与白名单）？
**答**：
- 注入本质：用户输入被拼进 SQL 语法层；防御本质：**数据与语法分离**——参数化让值永远只当数据。
- 占位符 `?`/`$1` 是正解；ORM 默认参数化，但 `raw query` 仍是高危点（Prisma 用 tagged template 自动参数化）。
- 动态部分（排序字段/表名）不能用占位符 → **白名单映射**，不在名单内的直接拒绝或回退默认值。
- 纵深：最小权限账号（业务库禁 DDL/DROP）、错误信息不回显 SQL、审计日志记录可疑输入。

```javascript
// 反例：字符串拼接 = 注入入口
// db.query(`SELECT * FROM users WHERE name = '${req.body.name}'`);
// 输入 ' OR '1'='1 → 拖库；输入 '; DROP TABLE users; -- → 破坏

// 正例一：占位符参数化
const rows = await db.query(
  'SELECT id, name FROM users WHERE name = ? AND status = ?',
  [req.body.name, 1],
);

// 正例二：动态排序字段白名单映射
const SORTABLE = { created: 'created_at', price: 'price', sales: 'sales' };
const col = SORTABLE[req.query.sort] ?? 'created_at'; // 白名单外回退默认
const dir = req.query.order === 'asc' ? 'ASC' : 'DESC';
const sql = `SELECT id, price FROM goods ORDER BY ${col} ${dir} LIMIT ?`;
await db.query(sql, [Number(req.query.limit ?? 20)]);  // 数值参数化

// 正例三：Prisma raw query 用 tagged template（自动参数化，非字符串拼接）
await prisma.$queryRaw`SELECT id FROM users WHERE name = ${name}`;
```
