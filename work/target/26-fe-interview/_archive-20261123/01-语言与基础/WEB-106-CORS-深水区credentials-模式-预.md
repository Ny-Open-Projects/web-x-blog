---
title: [WEB-106] CORS 深水区：credentials 模式、预检缓存与 Max-Age 细节？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-106：CORS 深水区：credentials 模式、预检缓存与 Max-Age 细节？
**答**：
- credentials 三档：`omit`（默认不带 cookie）、`same-origin`（仅同源带）、`include`（跨域也带）；一旦 include，服务端不能回 `Access-Control-Allow-Origin: *`，必须回显具体 Origin 并加 `Access-Control-Allow-Credentials: true`。
- 预检（OPTIONS）不是每次都发：浏览器按 `Access-Control-Max-Age` 缓存预检结果，期间同 URL 同头的请求直接放行；Chrome 硬上限 7200 秒（2 小时），Firefox 更长。
- 带 credentials 的响应必须显式暴露才能被 JS 读到：`Access-Control-Allow-Headers/Expose-Headers` 同理，非简单头（如 Authorization、自定义头）会触发预检。
- 调试要点：Service Worker 与重定向都可能让预检失效；`Access-Control-Allow-Origin` 回显 Origin 时要小心任意反射造成的安全回退。

```javascript
// 跨域携带 cookie 的标准三件套
fetch('https://api.example.com/me', {
  method: 'POST',
  credentials: 'include',                    // 1. 前端显式开启跨域凭证
  headers: { 'Content-Type': 'application/json', 'X-Custom-Trace': 'abc' }, // 2. 自定义头触发预检
  body: JSON.stringify({ id: 1 }),
});
// 3. 服务端必须返回：
// Access-Control-Allow-Origin: https://www.example.com   （不能是 *）
// Access-Control-Allow-Credentials: true
// Access-Control-Allow-Headers: Content-Type, X-Custom-Trace
// Access-Control-Max-Age: 7200    （预检结果缓存 2 小时，减少 OPTIONS 请求）
```
