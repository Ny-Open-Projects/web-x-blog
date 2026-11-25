---
title: [FRP-347] 框架无关的认证与 Token 管理
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## FRP-347：框架无关的认证与 Token 管理

**答**：
- 内核职责：token 存储（内存 + 刷新机制）、刷新单飞（互斥，多页面/框架共享一次刷新）、过期检测（定时 + 401 触发）——纯 JS 无框架
- 刷新单飞的跨框架价值：React 页面与 Vue 页面（微前端）同时 401 → 一次刷新全端生效——无内核则双刷新（一个 token 覆盖另一个）
- 请求层注入：fetch 包装（Authorization header + 401 重放）——框架无关；各框架数据层自动受益
- 广播：新 token 广播给所有 tab（BroadcastChannel）——跨 tab + 跨框架一致
- 安全边界：token 不进 localStorage（XSS 面）——内存 + HttpOnly refresh cookie 的组合；iframe/微前端场景的 storage 隔离

```javascript
export function createAuth({ refresh }) {
  let token = null, refreshing = null;
  async function getToken() {
    if (token) return token;
    refreshing ??= refresh().then((t) => { token = t; bc.postMessage({ type: 'token', t }); return t; })
      .finally(() => refreshing = null);            // 单飞
    return refreshing;
  }
  async function fetchWithAuth(input, init = {}) {
    const res = await fetch(input, { ...init, headers: { ...init.headers, Authorization: `Bearer ${await getToken()}` } });
    if (res.status === 401) { token = null; return fetchWithAuth(input, init); }  // 刷新重放
    return res;
  }
  bc.onmessage = ({ data }) => data.type === 'token' && (token = data.t);   // 跨 tab 同步
  return { fetchWithAuth, logout: () => { token = null; } };
}
```
