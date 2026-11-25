---
title: [NODE-337] Node 服务的 MySQL 索引与慢查询治理如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-337：Node 服务的 MySQL 索引与慢查询治理
**答**:
- 治理闭环：慢查询日志（long_query_time=1s）→ 定期归集（pt-query-digest 聚合指纹）→ 归因（EXPLAIN）→ 修复（索引/改写）→ 回归验证。指标：慢查询数趋势、TopN 指纹消除率。
- EXPLAIN 关注：type（ALL 全表扫是红旗）、rows 估算 vs 实际偏差、Extra（Using filesort/temporary）、索引是否命中最左前缀。
- 常见修复模式：函数包裹列导致索引失效（改为范围条件）、隐式类型转换（varchar 列 vs 数字参数）、深分页（cursor/keyset 分页替代 OFFSET 10万）、大 IN 拆批、JOIN 小表驱动大表。
- 读写分离下的坑：写后立即读走主库（同一连接或 GTID 等待），否则读到复制延迟的旧值（ARC-460 涉账场景红线）。
- 上线卡口：新 SQL 上线前 EXPLAIN 评审（字段变更走 DDL 评审），索引变更在线执行（PT-OSC/GTID）。
```sql
-- 深分页修复
SELECT * FROM orders WHERE id > :lastId ORDER BY id LIMIT 50;      -- keyset 分页
-- 索引失效修复
-- 坏: WHERE DATE(created_at) = '2026-11-19'
-- 好: WHERE created_at >= '2026-11-19 00:00:00' AND created_at < '2026-11-20 00:00:00'
```
