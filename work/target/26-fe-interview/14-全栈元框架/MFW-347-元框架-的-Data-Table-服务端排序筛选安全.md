---
title: [MFW-347→MFW-347] 服务端排序筛选的安全白名单（注入与枚举面）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-347：排序筛选安全

**答**:
- 攻击面一：orderBy 直拼（`?sort=price;DROP` 或 private 字段排序探测——salary desc 按响应差异推断数据）——白名单映射（sortKey→列枚举表，未知 key 400）
- 攻击面二：filter 操作符过宽（regex 注入 ReDoS/范围查询全表）——操作符枚举（eq/in/lt 白名单）+ 值 schema + 深分页锁（offset ≤ 1000 或强制 cursor）
- 枚举面收敛：可排序/可筛选字段集 = 「对外契约字段表」（与 MFW-318 payload 字段审计同源——出口与查询能力同一张表治理）
- 性能护栏：复合过滤器强制走覆盖索引（EXPLAIN 门禁进 CI——新筛选项上线前explain计划审查）

```javascript
const SORTABLE = { price: 'price_cents', created: 'created_at' }   // 契约字段表
if (!(qs.sort in SORTABLE)) return 400
const col = SORTABLE[qs.sort]
sql`ORDER BY ${sql.ident(col)} ${dir === 'asc' ? sql`ASC` : sql`DESC`}`   // 白名单标识符+方向枚举
// filter: op ∈ {eq,in,lt,gt} 且 field ∈ FILTABLE 且 offset≤1000
```
