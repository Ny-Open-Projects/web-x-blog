---
title: [NODE-175] 设计一个 RBAC 权限服务（表结构/缓存/接口）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-175：设计一个 RBAC 权限服务（表结构/缓存/接口）？
**答**：
- 经典五表：user、role、permission + user_role、role_permission；权限点命名 `资源:动作`（order:read）。
- 鉴权流程：登录时 JOIN 五表拉全量权限码 → 缓存 Redis（TTL 5min）→ 中间件声明式校验 `hasPerm('order:read')`。
- 缓存失效：角色权限变更发 `perm.changed` 事件，各服务删除对应缓存，秒级生效。
- 双重越权防御：功能权限（能否调接口）+ 资源权限（这条数据是不是你的，SQL where 加 owner 条件）——只做前者是常见漏洞。

```sql
CREATE TABLE role (id BIGINT PRIMARY KEY, code VARCHAR(32) UNIQUE, name VARCHAR(64));
CREATE TABLE permission (id BIGINT PRIMARY KEY, code VARCHAR(64) UNIQUE,
  resource VARCHAR(64), action VARCHAR(16));
CREATE TABLE user_role (user_id BIGINT, role_id BIGINT, PRIMARY KEY (user_id, role_id));
CREATE TABLE role_permission (role_id BIGINT, permission_id BIGINT, PRIMARY KEY (role_id, permission_id));
-- 全量权限查询：user_role JOIN role_permission JOIN permission WHERE user_id = ?
```

```javascript
const hasPerm = (code) => async (ctx, next) => {
  const cacheKey = `perms:${ctx.state.uid}`;
  let codes = JSON.parse((await redis.get(cacheKey)) ?? 'null');
  if (!codes) {
    codes = await loadPermsFromRbac(ctx.state.uid);  // 五表 JOIN
    await redis.setex(cacheKey, 300, JSON.stringify(codes));
  }
  if (!codes.includes(code)) ctx.throw(403, `missing ${code}`);
  await next();
};
router.get('/admin/orders', hasPerm('order:read'), listOrders);   // 声明式挂权限点
// 权限变更：mq.publish('perm.changed', { uid }) → 各服务 DEL perms:uid
```
