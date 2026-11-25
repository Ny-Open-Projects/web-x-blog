---
title: [WEB-229] token 存 localStorage 还是 Cookie？XSS 风险对比
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-229：token 存 localStorage 还是 Cookie？XSS 风险对比

**答**：
- localStorage：读写方便、跨域请求无需配置，但 XSS 能直接 `localStorage.getItem('token')` 拿走，且持久化到被清除为止。
- HttpOnly Cookie：JS 读不到，XSS 偷不到；但自动携带带来 CSRF 面（用 SameSite 缓解），且跨站 API 调用配置繁琐。
- 关键认知：XSS 存在时，无论存哪都能「以用户身份发请求」——偷走 token 只是收益更高。根治靠 CSP、输入过滤、框架默认转义，而非存储位置。
- 实践折中：access token 放内存（页面刷新丢，靠 refresh token 静默续期），refresh token 放 HttpOnly Cookie——最小化暴露窗口。

```javascript
// 内存存 token + HttpOnly refresh 的模式
let accessToken = null; // 只在内存，XSS 抓不到持久副本
async function authedFetch(url, opts = {}) {
  accessToken ??= await axios.post('/auth/token')   // 用 HttpOnly cookie 换
    .then(r => r.data.access);
  const res = await fetch(url, {
    ...opts,
    headers: { ...opts.headers, Authorization: `Bearer ${accessToken}` },
  });
  if (res.status === 401) { accessToken = null; return authedFetch(url, opts); }
  return res;
}
```
