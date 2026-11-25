---
title: [WEB-145] JWT 应该存哪里？Access + Refresh 双 Token 怎么落地？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-145：JWT 应该存哪里？Access + Refresh 双 Token 怎么落地？
**答**：
- 存 localStorage：任何 XSS 都能偷走 token，风险最高；存 HttpOnly Cookie：JS 读不到，但需配 CSRF 防护与 SameSite。
- 双 Token 模式：Access Token 短期（15 分钟）随请求走；Refresh Token 长期（7-30 天）只用于换新 Access，且只发给鉴权接口。
- 401 后自动刷新：并发请求要合并成一次 refresh（请求队列/单飞），刷新成功后重放排队请求，失败则踢回登录。
- Refresh Token 应做轮换（每次使用即作废换新）并保留服务端吊销能力，弥补 JWT 无法主动失效的问题。

```javascript
// axios 拦截器：401 时刷新 token，并把并发请求排队后重放
let refreshing = null;
api.interceptors.response.use(null, async (error) => {
  if (error.response?.status !== 401) throw error;
  refreshing = refreshing || refreshToken();           // 多个 401 只触发一次刷新
  try {
    const { accessToken } = await refreshing;
    setAuthHeader(accessToken);
    return api(error.config);                          // 重放原请求
  } catch (e) {
    await logout();                                    // refresh 也失效，踢回登录
    throw e;
  } finally {
    refreshing = null;
  }
});
async function refreshToken() {
  // Refresh Token 走 HttpOnly Cookie，仅此一个接口可用
  const res = await fetch('/api/auth/refresh', { method: 'POST', credentials: 'include' });
  if (!res.ok) throw new Error('refresh failed');
  return res.json();
}
```

**追问**：

1. 刷新接口本身返回 401，拦截器会怎样？ → 会再次进入 401 分支，形成无限递归刷新；必须把 refresh 请求排除在拦截器之外，或加 `_retry` 标记只重放一次。
2. 并发 401 时 `refreshing` 变量会有竞争吗？ → JS 单线程下赋值本身安全，但 `finally` 里置 null 的时机很关键：若在等待者恢复前清空，后续 401 会再发起一次刷新。
3. Refresh Token 轮换后，旧 token 被人重放怎么发现？ → 服务端记录 token 家族，已使用过的 refresh 再次出现即判定盗用，吊销整条链并强制重新登录。
