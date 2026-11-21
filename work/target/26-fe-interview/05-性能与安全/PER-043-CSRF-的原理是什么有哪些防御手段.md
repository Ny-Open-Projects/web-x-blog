---
title: [PER-043] CSRF 的原理是什么？有哪些防御手段？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-043：CSRF 的原理是什么？有哪些防御手段？

**答**：
- 原理：浏览器自动携带 cookie，攻击者诱导已登录用户在恶意页面发起跨站请求（表单/图片/自动提交），服务器无法区分是用户本人操作。
- **CSRF Token**：登录后下发随机 token，写请求必须带 token，攻击者站点读不到本站 cookie 也就拿不到 token（服务端校验）。
- **SameSite cookie**：`SameSite=Lax/Strict` 让跨站请求不携带 cookie，现代浏览器默认 Lax，是成本最低的防御。
- 辅助：校验 `Origin/Referer`；GET 只读不写；写请求要求二次验证（验证码/密码）。

```javascript
// 前端封装：写请求统一携带 CSRF token，服务端校验 token 才放行
function getCookie(name) {
  return document.cookie.split('; ').reduce((r, c) => {
    const [k, v] = c.split('=');
    return k === name ? decodeURIComponent(v) : r;
  }, '');
}

async function request(url, options = {}) {
  return fetch(url, {
    ...options,
    credentials: 'same-origin', // 不跨站携带 cookie
    headers: {
      'Content-Type': 'application/json',
      'X-CSRF-Token': getCookie('csrf_token'), // 攻击者站点拿不到该 token
      ...(options.headers || {})
    }
  });
}
// 配套：cookie 下发时设置 SameSite=Lax 或 Strict；服务端同时校验 Origin/Referer
```
