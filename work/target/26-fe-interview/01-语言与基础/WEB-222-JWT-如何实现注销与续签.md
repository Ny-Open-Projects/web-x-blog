---
title: [WEB-222] JWT 如何实现注销与续签？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 面试题
---

## WEB-222：JWT 如何实现注销与续签？

**答**：
- JWT 无状态的核心矛盾：签发后服务端无法撤回，注销/踢人都要引入状态。
- 注销方案：黑名单（注销时把 jti 写入 Redis，TTL=剩余有效期，校验时查黑名单）；或改用「短 access + 长 refresh」模式，注销只废 refresh。
- 续签标准做法：access token 有效期短（15min），refresh token 长且仅用于换新 access；换发时轮换 refresh token（旧的作废，防止重放）。
- 静默续签：前端拦截 401 → 用 refresh 换新 → 重放原请求；并发请求要共享同一次换新（Promise 复用），否则并发全 401。
- 滑动过期变体：每次校验通过时若剩余有效期 < 一半，响应头带新 token，前端替换存储。

```javascript
// 401 拦截静默续签（axios）
let refreshing = null;
axios.interceptors.response.use(null, async (err) => {
  if (err.response?.status !== 401) throw err;
  refreshing ??= axios.post('/auth/refresh', { refreshToken: store.refresh })
    .finally(() => (refreshing = null));       // 并发请求共用同一次换新
  const { data } = await refreshing;
  store.token = data.accessToken;
  err.config.headers.Authorization = `Bearer ${store.token}`;
  return axios.request(err.config);            // 重放原请求
});
```
