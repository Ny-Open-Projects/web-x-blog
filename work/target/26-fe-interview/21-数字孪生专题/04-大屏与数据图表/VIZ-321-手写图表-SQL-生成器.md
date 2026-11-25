---
title: [VIZ-321] 手写图表 SQL 生成器：从配置到查询（笔试）
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-321：手写图表 SQL 生成器：从配置到查询（笔试）

**答**：
- 题目：BI 图表配置（维度/指标/过滤/排序）→ 安全 SQL 生成（参数化防注入、白名单字段）。复用 HW-303/304 思想。
- 思路：配置结构化（非自由文本 SQL）→ 模板化生成（字段白名单、值参数化、聚合函数白名单）；防注入：标识符转义 + 值占位符。
- 评分点：白名单字段；参数化值；聚合白名单。

```javascript
const ALLOWED_AGGS = new Set(['sum', 'avg', 'count', 'max', 'min']);
const ALLOWED_FIELDS = new Set(['date', 'region', 'amount', 'user_id']);   // 字段白名单
function buildChartSQL(config) {
  const dims = config.dimensions.filter(d => ALLOWED_FIELDS.has(d))
    .map(d => `"${d.replace(/"/g, '')}"`);                  // 标识符转义
  const metrics = config.metrics.map(m => {
    if (!ALLOWED_AGGS.has(m.agg)) throw new Error('agg-not-allowed');
    if (!ALLOWED_FIELDS.has(m.field)) throw new Error('field-not-allowed');
    return `${m.agg}("${m.field}") AS "${m.alias ?? m.agg}_${m.field}"`;
  });
  const where = config.filters.map((f, i) => {             // 值参数化
    if (!ALLOWED_FIELDS.has(f.field)) throw new Error('field-not-allowed');
    return `"${f.field}" ${f.op} $${i + 1}`;
  });
  return {
    sql: `SELECT ${[...dims, ...metrics].join(', ')} FROM data_table ` +
      (where.length ? `WHERE ${where.join(' AND ')}` : '') +
      (dims.length ? ` GROUP BY ${dims.map((_, i) => i + 1).join(', ')}` : ''),
    params: config.filters.map(f => f.value),              // 参数化值（防注入）
  };
}
```
