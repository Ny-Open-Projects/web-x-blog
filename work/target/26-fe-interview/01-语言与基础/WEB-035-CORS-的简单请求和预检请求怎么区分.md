---
title: [WEB-035] CORS 的简单请求和预检请求怎么区分？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-035：CORS 的简单请求和预检请求怎么区分？
**答**：
- 简单请求：方法为 GET/HEAD/POST，且 Content-Type 限于 text/plain、multipart/form-data、application/x-www-form-urlencoded，不带自定义头。
- 不满足以上条件即触发预检：浏览器先发 OPTIONS 请求询问服务器是否允许，通过后才发真实请求。
- 预检由浏览器自动完成，前端无感知；预检结果可被缓存（`Access-Control-Max-Age`），减少 OPTIONS 次数。
- 触发预检的常见原因：`Content-Type: application/json`、携带 `Authorization`、自定义业务头。

```javascript
// 简单请求：Content-Type 为表单编码，不触发预检
fetch('https://api.example.com/form', {
  method: 'POST',
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  body: 'a=1&b=2', // 需要服务器返回 Access-Control-Allow-Origin
});

// 非简单请求：application/json + 自定义头，先发 OPTIONS 预检
fetch('https://api.example.com/data', {
  method: 'PUT',
  headers: {
    'Content-Type': 'application/json', // 触发预检的条件一
    'X-Request-Id': 'abc',              // 自定义头，触发预检的条件二
  },
  body: JSON.stringify({ ok: true }),
});
```
