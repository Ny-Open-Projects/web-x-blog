---
title: [WEB-333] 多租户系统前端怎么隔离 token 与数据缓存？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 面试题
---

## WEB-333：多租户系统前端怎么隔离 token 与数据缓存？
**答**：
- token 按 租户+用户 维度命名空间化存储（如 sw:key=tenant:token），切租户先清当前租户的请求缓存与 store。
- 请求层自动注入当前租户 header（X-Tenant-Id），路由层把租户编码进路径 /t/:tenantId 防串。
- 坑：WebSocket、轮询、Service Worker 缓存都持有旧租户上下文，切租户要全量重建；indexedDB 同样要按租户分库。

```javascript
const storageKey = (t) => 'token:' + t;
function switchTenant(from, to) {
  cache.clear();                 // 请求缓存
  store.reset();                 // pinia 状态
  ws.reconnect(withToken(storageKey(to)));
  sw.postMessage({ type: 'PURGE', tenant: from });
  setHeader('X-Tenant-Id', to);
}
console.log('租户隔离 = 存储、连接、缓存三处都要隔离');
```
