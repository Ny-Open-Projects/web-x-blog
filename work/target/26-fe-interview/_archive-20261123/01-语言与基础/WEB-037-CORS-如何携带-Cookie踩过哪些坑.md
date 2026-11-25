---
title: [WEB-037] CORS 如何携带 Cookie？踩过哪些坑？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-037：CORS 如何携带 Cookie？踩过哪些坑？
**答**：
- 前端 `fetch` 要设 `credentials: 'include'`（axios 设 `withCredentials: true`），XHR 默认同源才带。
- 服务端必须同时满足三点：`Access-Control-Allow-Credentials: true`、`Allow-Origin` 为具体源（不能是 `*`）、`Allow-Headers` 不能是 `*`。
- Cookie 的 SameSite 也可能拦截：第三方站点接口要跨站携带时 Cookie 需 `SameSite=None; Secure`。
- 典型坑：后端配了 `*`，前端加了 include，浏览器报 "credential mode ... cannot use wildcard"。

```javascript
// 前端：跨源请求携带 Cookie 的正确写法
fetch('https://api.example.com/profile', {
  method: 'GET',
  credentials: 'include', // 关键：跨源也要带上目标域的 Cookie
})
  .then((r) => r.json())
  .then(console.log);

// axios 全局配置
// axios.defaults.withCredentials = true;
```

```javascript
// 服务端三件套缺一不可（否则浏览器拦截响应）
app.get('/profile', (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', 'https://app.example.com'); // 1. 具体源
  res.setHeader('Access-Control-Allow-Credentials', 'true');               // 2. 允许凭据
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');           // 3. 不能用 *
  res.json({ id: 1 });
});
```
