---
title: [NODE-400] Node 服务的搜索与过滤接口（深分页/竞态/复杂筛选）设计要点
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-400：搜索与过滤接口设计要点
**答**:
- 分页协议：cursor 分页（base64 编码游标：排序值 + id tiebreaker）替代 offset（深分页性能崩塌 NODE-337）；游标无状态可分享；变更插入不导致重复/漏数据（offset 的经典问题）。
- 过滤协议：筛选条件结构化（field=op:value 或 JSON filter 对象 + schema 校验）、白名单可过滤字段（防任意列查询拖库）、复杂筛选（区间/多值/嵌套）语法明确写文档（NODE-399）。
- 排序与一致性：排序字段白名单（防注入 NODE-354）+ 稳定排序（tiebreaker 保证翻页顺序一致）；总数估算（大结果集 count 优化：estimated 或 "1000+" 语义）。
- 性能：筛选组合多时走搜索引擎（NODE-387）而非 SQL 拼接；热门筛选组合缓存（NODE-353 singleflight）；超时保护（复杂查询 3s 超时降级简化查询）。
- 竞态配合：前端筛选竞态防护（ARC-383 AbortController），服务端响应带请求上下文（前端校验是否过期）。
```javascript
// cursor 分页实现
function encodeCursor(row) { return base64(JSON.stringify([row.created_at, row.id])); }
async function list({ filter, cursor, limit = 20 }) {
  const [createdAt, id] = cursor ? JSON.parse(atob(cursor)) : [null, null];
  const where = cursor
    ? 'where (created_at, id) < ($1, $2)' : 'where created_at < now() - interval \'0 day\'';
  const rows = await db.query(`select * from goods ${where} order by created_at desc, id desc limit ${limit + 1}`);
  return { items: rows.slice(0, limit),
    nextCursor: rows.length > limit ? encodeCursor(rows[limit - 1]) : null };
}
```
