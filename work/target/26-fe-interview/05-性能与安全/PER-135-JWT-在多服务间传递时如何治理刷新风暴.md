---
title: [PER-135] JWT 在多服务间传递时如何治理刷新风暴？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-135：JWT 在多服务间传递时如何治理刷新风暴？

**答**：
- 风暴场景：token 过期瞬间，页面同时挂起的几十个请求全部 401，各自触发 refresh，刷新接口被打爆且部分成功部分失败。
- 治理三件套：**单飞**（全局共享一个进行中的 refresh Promise，所有 401 等同一个）、**跨标签页协调**（BroadcastChannel 通知其他页复用新 token，不重复刷）、**失败退避**（刷新失败统一登出，禁止循环重试）。
- 请求队列：401 的请求暂存队列，token 刷新后原样重放一次（标记 `__retried` 防二次循环）。
- 多服务传递：网关统一验签后向下游透传用户上下文头，下游只信任网关，不重复解析 JWT 里的权限。

```javascript
// 刷新风暴治理：单飞 + 跨标签页协调 + 失败统一登出
let refreshing = null; // 单飞：并发 401 只发一次 refresh

export async function refreshOnce() {
  refreshing ??= fetch('/api/auth/refresh', { method: 'POST', credentials: 'include' })
    .then((r) => (r.ok ? r.json() : Promise.reject(r.status)))
    .finally(() => setTimeout(() => (refreshing = null), 1000)); // 1s 内的重试合并
  return refreshing;
}

const bc = new BroadcastChannel('auth'); // 跨标签页：一页刷新成功，其余页复用
bc.onmessage = (e) => {
  if (e.data.type === 'refreshed') setToken(e.data.token);
  if (e.data.type === 'logout') location.assign('/login');
};

axios.interceptors.response.use(null, async (err) => {
  const cfg = err.config;
  if (err.response?.status !== 401 || cfg.__retried) throw err;
  cfg.__retried = true; // 防二次循环
  try {
    const { token } = await refreshOnce(); // 50 个并发请求共享同一个 Promise
    bc.postMessage({ type: 'refreshed', token });
    cfg.headers.Authorization = `Bearer ${token}`;
    return axios(cfg); // 暂存的请求原样重放一次
  } catch {
    bc.postMessage({ type: 'logout' }); // 失败统一登出，禁止循环重试
    throw err;
  }
});
```
