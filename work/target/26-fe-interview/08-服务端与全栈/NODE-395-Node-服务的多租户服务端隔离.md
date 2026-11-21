---
title: [NODE-395] Node 服务的多租户服务端数据隔离如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-395：多租户服务端数据隔离
**答**:
- 隔离模型谱系：独立库（强隔离、成本高，大客户）、独立 schema（中）、共享表 + tenant_id（主流，成本最低）。选择按租户规模分层：大客户独立库、中小共享。
- 共享表方案的强制防线：所有表带 tenant_id + 所有查询自动注入条件（ORM 全局 scope/repository 层强制，禁裸查询）+ 组合唯一索引（tenant_id + 业务键）+ 行级安全（PG RLS 数据库层兜底——应用 bug 也不会串户）。
- 租户上下文传播：请求进入解析租户（域名/JWT claim）→ AsyncLocalStorage 保存 → repository 自动取用（NODE-292）；缓存 key 带租户（NODE-383）；MQ 消息带租户上下文。
- 大租户治理：慢查询按租户归因（大租户拖累共享库 → 迁独立库）、租户级限流（一个租户的批量任务不影响他人）。
- 泄漏测试：串户专项测试（A 租户上下文访问 B 租户 ID 必须返回 not found）进回归。
```javascript
// 请求级租户上下文 + 自动注入
const als = new AsyncLocalStorage();
function tenantRepo(table) {
  return {
    async find(id) {
      const t = als.getStore().tenant;
      return db.query(`select * from ${table} where id=$1 and tenant_id=$2`, [id, t.tenantId]);
    }
  };
}
// PG RLS 兜底：ALTER TABLE orders ENABLE ROW LEVEL SECURITY;
// CREATE POLICY t ON orders USING (tenant_id = current_setting('app.tenant')::uuid);
```
