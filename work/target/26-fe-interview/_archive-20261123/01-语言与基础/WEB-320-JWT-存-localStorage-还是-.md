---
title: [WEB-320] JWT 存 localStorage 还是 Cookie？怎么权衡？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 面试题
---

## WEB-320：JWT 存 localStorage 还是 Cookie？怎么权衡？
**答**：
- localStorage：不受 CSRF 影响、跨域 API 方便；但任何 XSS 都能偷走 token，且无法自动带上跨站请求。
- HttpOnly Cookie：XSS 读不到，天然随请求携带；但要防 CSRF（SameSite=Strict/Lax + CSRF token），且跨域配置繁琐。
- 工程折中常见：access token 内存/HttpOnly 短效 Cookie，refresh token 走严格 SameSite Cookie；同时把 XSS 防线（CSP）当作根本。

```javascript
const tradeoffs = {
  localStorage: { xss: '可被读', csrf: '免疫', sso: '手工带' },
  httpOnlyCookie: { xss: '读不到', csrf: '需 SameSite+token', sso: '自动携带' },
};
const pick = (threat) => threat === 'csrf-high' ? 'localStorage' : 'httpOnlyCookie';
console.log('主流：HttpOnly + SameSite=Strict 存 refresh，内存存 access');
```
