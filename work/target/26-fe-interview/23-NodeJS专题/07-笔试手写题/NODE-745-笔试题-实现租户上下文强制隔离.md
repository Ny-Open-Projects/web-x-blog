---
title: [NODE-745] 笔试题——实现租户上下文强制隔离（ALS + 审计）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-745：手写租户隔离

**需求与边界**：
- 需求：多租户强制隔离（SCN-NODE-678）——① ALS 注入 tenantId（SCN-NODE-730 上下文）；② 查询自动注入租户条件（SQL 重写或 ORM scope）；③ 无租户条件审计（缺 tenant_id 的查询告警——漏过滤防线）；④ 跨租户显式通道（白名单 + 审计）。
- 边界：① SQL 重写的可靠性（正则 vs AST——AST 更可靠但复杂；简化为「约定 API 层强制 + DB 行级校验双保险」）；② 租户上下文缺失拒绝（无 tenantId 的查询直接拒绝——fail-closed）；③ 批量任务的租户传递（队列消息携带——SCN-NODE-730 边界）。

**答**：
```javascript
const tenantCtx = new AsyncLocalStorage();
app.use((req, res, next) => tenantCtx.run({ tenant: req.headers['x-tenant-id'] }, next));
// 查询包装：强制注入 + 审计
function tQuery(sql, params) {
  const tenant = tenantCtx.getStore()?.tenant;
  if (!tenant) throw new Error('TENANT_CTX_MISSING');   // fail-closed：无上下文拒绝
  const wrapped = withTenantCondition(sql, tenant);     // WHERE tenant_id = $N 注入
  const plan = explainHasTenantFilter(wrapped);
  if (!plan) alert({ type: 'MISSING_TENANT_FILTER', sql: wrapped });   // 审计
  return db.query(wrapped, [...params, tenant]);
}
// 跨租户显式通道（白名单 + 审计）
async function crossTenantQuery(sql, { operator, reason }) {
  audit({ operator, reason, sql });                     // 审计留痕（SCN-OPS-609）
  return db.query(sql);
}
```

**评分点**:
- fail-closed（无上下文拒绝——SCN-NODE-678 安全默认值）。
- 强制注入 + 审计双保险（ORM scope + 查询审计）。
- 跨租户显式通道（白名单 + 审计——做对默认做错声明）。
- 批量任务租户传递（ALS 边界——SCN-NODE-730）。
