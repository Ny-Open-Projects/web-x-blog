---
title: [NODE-122] 慢查询如何定位与索引优化（EXPLAIN 实战）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-122：慢查询如何定位与索引优化（EXPLAIN 实战）？
**答**：
- 定位链路：慢查询日志（`long_query_time` 阈值）→ `EXPLAIN` 看执行计划 → 加索引 → 复查 EXPLAIN 验证。
- EXPLAIN 三看：`type`（ALL 全表扫必须消灭）、`rows`（预估扫描行数）、`Extra`（filesort/temporary 是坏信号）。
- 联合索引原则：**等值列在前、范围与排序列在后**，最左前缀生效；索引失效三坑：函数包裹列、隐式类型转换、前导 `%` 模糊。
- 应用层配合：` Seconds_Behind_Master` 监控复制延迟；SQL 上线前用真实数据量 explain，不做拍脑袋索引。

```sql
-- 1. 打开慢查询日志
SET GLOBAL slow_query_log = ON;
SET GLOBAL long_query_time = 0.2;

-- 2. 问题 SQL：全表扫描 + filesort
EXPLAIN SELECT id, amount FROM orders
WHERE user_id = 42 AND status = 1
ORDER BY created_at DESC LIMIT 20;
-- type=ALL  Extra=Using filesort → 必须建联合索引

-- 3. 联合索引：等值列在前，排序列在后
ALTER TABLE orders ADD INDEX idx_user_status_created (user_id, status, created_at);

-- 4. 复查：type=ref，rows 从百万级降到 20，P99 800ms → 5ms
EXPLAIN SELECT id, amount FROM orders
WHERE user_id = 42 AND status = 1
ORDER BY created_at DESC LIMIT 20;

-- 索引失效示例：
-- WHERE DATE(created_at) = '2026-11-01'   函数包裹 → 改范围查询
-- WHERE user_id = '42'                    隐式转换 → 保持类型一致
-- WHERE title LIKE '%关键词%'             前导模糊 → 全文索引/ES
```
