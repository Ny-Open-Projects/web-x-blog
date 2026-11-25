---
title: [AGT-438] 笔试题——实现 Text2SQL 安全执行管线（生成+校验+只读+熔断）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-438：手写 ChatBI 管线：DSL 生成、静态校验、只读执行、行级权限注入

**需求与边界**：
- 输入：自然语言问题、表 schema、指标口径、用户 ACL；输出：SQL+结果+口径说明。
- 边界要求：① SQL 静态校验（只读白名单：仅 SELECT；禁 DML/多语句/注释注入）；② 行级权限条件强制注入（覆盖模型生成）；③ LIMIT 强制与超时；④ 口径歧义触发澄清（AGT-431 联动）。

**答**：
```javascript
async function chatBI(question, { schema, metrics, acl, db }) {
  // 1. 解析与澄清
  const plan = await llm(`解析为 {metric, dims, timeRange, filters}。
    指标口径: ${JSON.stringify(metrics)}`, question);
  if (plan.ambiguous) return { clarify: plan.options };
  // 2. 生成 SQL
  let sql = await llm2sql(plan, schema);
  // 3. 静态校验
  const stripped = sql.replace(/--.*|\/\*[\s\S]*\*\//g, '').trim();
  if (!/^select\b/i.test(stripped) || /;|into\s|update\b|delete\b|drop\b/i.test(stripped))
    return { error: '非只读 SQL，拒绝执行', sql };
  // 4. 行级权限强制注入（WHERE 追加，覆盖模型输出）
  sql = injectACL(sql, acl);                    // e.g. AND dept_id IN (...)
  // 5. LIMIT 强制 + 只读连接执行
  if (!/limit\s+\d+/i.test(stripped)) sql += ' LIMIT 1000';
  const rows = await db.run(sql, { readOnly: true, timeout: 5000 });
  return { sql, rows: rows.slice(0, 50),
    caliber: metrics[plan.metric]?.desc ?? '标准口径',
    asOf: new Date().toISOString() };
}
function injectACL(sql, acl) {
  // 简化：在最外层包一层权限过滤
  return `SELECT * FROM (${sql}) t WHERE t.dept_id IN (${acl.join(',')})`;
}
// 口径歧义：metrics 中同名多口径 → clarify 列出让用户选。
```

**评分点**:
- 静态校验完整：只读白名单、多语句/注释注入拦截、LIMIT 强制。
- 行级权限强制包裹注入（不信任模型生成的 WHERE）。
- 口径歧义澄清（AGT-431 联动），结果带口径说明与 asOf 时间戳。
- 只读连接+超时双保险，数字全部来自查询引擎（防幻觉计算）。
