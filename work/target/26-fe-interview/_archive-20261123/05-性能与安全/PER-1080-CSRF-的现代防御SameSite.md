---
title: [PER-1080] CSRF 的现代防御：SameSite 之外还需要什么
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1080：CSRF 的现代防御：SameSite 之外还需要什么

**答**：
- SameSite=Lax/Strict 已覆盖大部分 CSRF（跨站表单/图片触发），但旧浏览器与 GET 链接场景仍有缺口。
- Token 防御：CSRF token（双提交 cookie 或服务端 session 绑定）；关键写操作加自定义头（X-Requested-With，跨站表单发不出）。
- Origin/Referer 校验：服务端校验 Origin 白名单，比 token 更简单可靠。
- 深水：登录态用 Bearer（Header 携带）天然免疫 CSRF，但要防 XSS 窃取——CSRF 与 XSS 防御是互补关系。

```javascript
// 双提交 CSRF token
const CSRF = crypto.randomUUID();
document.cookie = `csrf=${CSRF}; SameSite=Lax`;      // cookie 一份
// 请求时 header 再带一份，服务端比对
fetch('/api/order', { method: 'POST',
  headers: { 'X-CSRF-Token': CSRF, 'Content-Type': 'application/json' },
  body: JSON.stringify(payload) });
// 服务端：
// if (req.cookies.csrf !== req.headers['x-csrf-token']) return 403;
```
