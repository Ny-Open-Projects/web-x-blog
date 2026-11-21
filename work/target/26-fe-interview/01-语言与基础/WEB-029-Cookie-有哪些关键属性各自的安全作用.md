---
title: [WEB-029] Cookie 有哪些关键属性？各自的安全作用？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-029：Cookie 有哪些关键属性？各自的安全作用？
**答**：
- `Domain`/`Path` 控制作用域：Cookie 会随同域及父域请求自动携带，主域相同子域共享 Cookie。
- `Expires`/`Max-Age` 控制生命周期，不设置则是会话 Cookie，关浏览器即失效。
- `HttpOnly` 禁止 JS 读取，防 XSS 偷取；`Secure` 只在 HTTPS 发送。
- `SameSite` 控制跨站携带，Lax 默认防大部分 CSRF；`Max-Age` 单位是秒。

```http
# 服务端下发的 Set-Cookie 完整示例
Set-Cookie: session_id=abc123; Domain=.example.com; Path=/; Max-Age=86400; HttpOnly; Secure; SameSite=Lax
```

```javascript
// JS 只能读写未加 HttpOnly 的 Cookie；工具函数务必 encodeURIComponent 防特殊字符
function setCookie(name, value, { maxAge = 3600, path = '/' } = {}) {
  document.cookie = `${encodeURIComponent(name)}=${encodeURIComponent(value)}; max-age=${maxAge}; path=${path}; SameSite=Lax`;
}
function getCookie(name) {
  const pair = document.cookie
    .split('; ')
    .find((row) => row.startsWith(encodeURIComponent(name) + '='));
  return pair ? decodeURIComponent(pair.split('=')[1]) : null;
}
setCookie('theme', 'dark');
console.log(getCookie('theme')); // dark；session_id 若是 HttpOnly，这里拿到 null
```
