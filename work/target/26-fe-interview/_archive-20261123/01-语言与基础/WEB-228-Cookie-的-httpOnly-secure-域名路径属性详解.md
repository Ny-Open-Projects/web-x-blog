---
title: [WEB-228] Cookie 的 HttpOnly/Secure/Domain/Path 属性详解
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP]
type: 面试题
---

## WEB-228：Cookie 的 HttpOnly/Secure/Domain/Path 属性详解

**答**：
- HttpOnly：JS 的 document.cookie 读不到，专防 XSS 偷 session——登录态 cookie 必加。
- Secure：只在 HTTPS 下发送，防明文网络嗅探。
- Domain：不设默认为当前域（host-only）；设 `.example.com` 则所有子域共享。注意子域 cookie 可被父域设置覆盖的风险（cookie tossing）。
- Path：限定发送路径，安全价值低（JS 仍可绕过），主要用于隔离。
- Max-Age/Expires：会话 cookie（关浏览器即失效）与持久 cookie。
- 组合建议：`HttpOnly; Secure; SameSite=Lax` 是 session cookie 标配；CSRF token 类需 JS 读取则不能 HttpOnly。

```javascript
// 服务端 Set-Cookie 完整示例
res.setHeader('Set-Cookie',
  'sess=abc123; Max-Age=604800; Domain=.example.com; Path=/; ' +
  'HttpOnly; Secure; SameSite=Lax');

// 前端可见性对比
console.log(document.cookie); // 看不到 sess，只能看到未 HttpOnly 的 cookie
```
