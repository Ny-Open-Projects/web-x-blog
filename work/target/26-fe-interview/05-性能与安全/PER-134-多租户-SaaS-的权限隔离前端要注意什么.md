---
title: [PER-134] 多租户 SaaS 的权限隔离前端要注意什么？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-134：多租户 SaaS 的权限隔离前端要注意什么？

**答**：
- 三原则：**缓存键带租户**（权限/配置缓存的 key 必须含 tenantId，否则 A 租户权限泄漏给 B 租户）、**请求头带租户**（服务端仍要以会话为准校验用户确属该租户）、**切换租户全量清理**（权限缓存、本地存储、内存状态、Cookie）。
- 租户切换后最稳的做法是**整页 reload**，避免各模块内存里残留跨租户状态（列表筛选、草稿、WebSocket 订阅）。
- 租户上下文用单一 source of truth（URL 域名或子路径 > Cookie > 内存），禁止每个模块自己维护一份。
- 越权测试进 CI：用 A 租户会话请求 B 租户资源 ID，必须 403/404。

```javascript
// 多租户隔离三原则：缓存键带租户、请求头带租户、切换全量清理
let tenantId = 't_1001';
let permCache = new Map(); // key 必须含租户，否则跨租户泄漏

export async function loadPermissions() {
  const key = `${tenantId}:perms`;
  if (permCache.has(key)) return permCache.get(key);
  const list = await fetch(`/api/iam/permissions?tenant=${tenantId}`, {
    headers: { 'X-Tenant-Id': tenantId }, // 仅作路由提示，服务端以会话校验归属
  }).then((r) => r.json());
  permCache.set(key, list);
  return list;
}

export async function switchTenant(next) {
  if (next === tenantId) return;
  tenantId = next;
  permCache.clear();                                   // 权限缓存全清
  localStorage.removeItem(`${tenantId}:draft`);        // 清跨租户草稿
  socket?.close();                                     // 断开旧租户的长连接
  document.cookie = 'tenant=; Max-Age=0; path=/';      // 清租户 Cookie
  await loadPermissions();
  location.reload();                                   // 兜底整页重载，清空全部内存状态
}
```
