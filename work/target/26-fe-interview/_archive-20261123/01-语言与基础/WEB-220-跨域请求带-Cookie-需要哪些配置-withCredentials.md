---
title: [WEB-220] 跨域请求带 Cookie 需要哪些配置？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP]
type: 面试题
---

## WEB-220：跨域请求带 Cookie 需要哪些配置？

**答**：
- 前端：`fetch(url, { credentials: 'include' })` 或 axios `withCredentials: true`（XHR 同理）。
- 服务端：`Access-Control-Allow-Origin` 必须是具体域名，不能为 `*`（浏览器规定带凭据时禁止通配）；`Access-Control-Allow-Credentials: true`。
- Cookie 本身：Set-Cookie 时 SameSite=None + Secure 才允许跨站携带（现代浏览器默认 Lax 会拦截）。
- 常见排查顺序：报错「credential 模式不能为 include 时不能设 *」→ 改具体域名；cookie 没带上 → 检查 SameSite；Set-Cookie 被丢 → 跨域响应没有 expose 该头（用 DevTools Network 确认响应头是否到达）。

```javascript
// 前端
fetch('https://api.other.com/me', { credentials: 'include' });

// 服务端（Express）三件套
app.use('/api', (req, res, next) => {
  res.set('Access-Control-Allow-Origin', 'https://app.example.com'); // 具体
  res.set('Access-Control-Allow-Credentials', 'true');
  next();
});
// 注意：多域名场景按 Origin 白名单动态回写，而不是写死或写 *
```
