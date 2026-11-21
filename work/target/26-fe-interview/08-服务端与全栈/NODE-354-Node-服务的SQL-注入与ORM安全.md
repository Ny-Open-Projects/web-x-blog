---
title: [NODE-354] Node 服务的 SQL 注入防护与 ORM 安全边界
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-354：SQL 注入防护与 ORM 安全边界
**答**:
- 防线一：参数化查询是唯一正解（pg 参数占位 / mysql2 prepare）——用户输入永远走参数，不进 SQL 字符串拼接。
- ORM 边界：Sequelize/Prisma 默认安全，但 raw query（sequelize.literal / $queryRaw）与排序/表名白名单失效是主要事故点——动态排序字段必须白名单映射，动态表名禁止。
- like 注入：参数化防不了通配符语义注入（% _），用户输入进 like 前转义通配符。
- 权限纵深：应用 DB 账号最小权限（业务账号不给 DDL/删表权限）、生产禁 root；SQL 审计（高危语句告警：无 where 的 update/delete）。
- 其他注入同类项：NoSQL 注入（Mongo 直接把 req.body 当 query——$gt 对象注入，须 schema 清洗）、命令注入（exec 拼接用户输入 → execFile 参数数组）、路径穿越（文件名拼接 ../，用白名单或 id 映射）。
```javascript
// 参数化 + 白名单排序
const SORTABLE = { time: 'created_at', price: 'price' };
const col = SORTABLE[req.query.sort] ?? 'created_at';            // 白名单映射
const rows = await pg.query(
  `SELECT * FROM goods WHERE category = $1 AND name LIKE $2 ORDER BY ${col} DESC LIMIT $3`,
  [cat, `%${escapeLike(kw)}%`, 20]);                             // like 通配符转义
// MongoDB: db.users.find({ user: sanitize(schema.parse(req.body.user)) })  // 防对象注入
```
