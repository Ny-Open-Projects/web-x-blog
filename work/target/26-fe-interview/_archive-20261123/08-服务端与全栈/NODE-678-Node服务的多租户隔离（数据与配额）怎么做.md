---
title: [NODE-678] 多租户隔离（数据/配额/噪声）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-678：多租户隔离怎么做？
**答**：
- 数据隔离三级：行级隔离（tenant_id 列 + 强制过滤——ORM 全局 scope 防漏，SCN-FIN-493 租户隔离校验同源）、schema 级（每租户 schema——中等强度）、库级（独立 DB——最强最贵）；按租户规模分层（大租户独立库、小租户行级）。
- 租户上下文贯穿：ALS（SCN-NODE-645）承载 tenantId——所有查询自动带租户过滤（middleware 注入 + ORM scope 强制）；漏过滤的防线（查询无 tenant_id 条件即告警——lint/运行时审计）。
- 配额隔离：租户级限流/配额（SCN-NODE-641 分维度限流）；噪声隔离（大租户慢查询不拖垮共享 DB——连接池分池，SCN-NODE-643 池隔离）。
- 跨租户操作的防护：管理后台的跨租户查询显式授权（白名单通道——默认不可能跨租户）。
- 追问钩子：为什么「ORM 全局 scope 强制过滤」优于「每个查询手动带 tenant_id」——手动带依赖开发者记忆（漏一处即数据越权——事故不可逆）；全局 scope 在 ORM 层强制注入（漏不掉），跨租户操作必须显式绕过（绕过点即审计点）——把安全默认值做进框架，让「做对是默认、做错需声明」。

```javascript
// ALS 承载 tenantId + ORM scope 强制
als.run({ tenantId: req.headers['x-tenant'] }, () => next());
db.addScope('tenant', { where: { tenantId: als.getStore().tenantId } });
db.query = withTenantScope(db.query);                  // 全局强制注入
// 审计：无租户条件查询告警
db.on('query', q => { if (!q.sql.includes('tenant_id') && !isWhitelisted(q)) alert('MISSING_TENANT_FILTER'); });
```
