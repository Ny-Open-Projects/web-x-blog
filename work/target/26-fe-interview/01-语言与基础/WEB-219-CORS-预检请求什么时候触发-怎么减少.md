---
title: [WEB-219] CORS 预检请求什么时候触发？怎么减少？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP]
type: 面试题
---

## WEB-219：CORS 预检请求什么时候触发？怎么减少？

**答**：
- 触发条件（三选一即预检）：非简单方法（PUT/DELETE/PATCH/CONNECT 等）、非简单头（带了 Authorization、自定义头如 X-Token）、非简单 Content-Type（只有 text/plain、multipart/form-data、application/x-www-form-urlencoded 简单）。
- 预检 = 先发 OPTIONS 询问，带 Access-Control-Request-Method/Headers，服务端允许后真实请求才发出。
- 减少预检的手段：服务端设置 `Access-Control-Max-Age`（缓存预检结果，Chrome 上限 7200s）；避免无谓的自定义头；Content-Type 用简单类型序列化；同域下用 Nginx 反代把 API 收进同源，彻底消灭 CORS。
- 常见坑：预检请求不会带自定义头和 cookie，服务端鉴权中间件要放行 OPTIONS；Authorization 头永远触发预检（不在简单头白名单里）。

```javascript
// 简单请求（不预检）
fetch('https://api.other.com/data', { method: 'POST' }); // 无自定义头 → 简单

// 触发预检
fetch('https://api.other.com/data', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json', 'X-Token': 'abc' }, // 两个触发点
});
// 服务端（Express）
app.options('/data', (req, res) => {
  res.set({
    'Access-Control-Allow-Origin': 'https://app.com',
    'Access-Control-Allow-Headers': 'Content-Type, X-Token',
    'Access-Control-Max-Age': '86400',
  }).sendStatus(204);
});
```

**追问**：

1. 为什么 OPTIONS 预检请求不带 cookie 和自定义头？ → 规范如此，预检只用于探测服务端能力；所以鉴权中间件若拦截所有请求，必须先放行 OPTIONS 再鉴权。
2. `Access-Control-Max-Age` 设得很大有什么副作用？ → 缓存期内改了允许的方法或头不会生效，前端会一直按旧策略发请求；Chrome 上限 2 小时，要权衡。
3. 为什么带 `Authorization` 头一定触发预检？ → 它不在 CORS 安全头白名单里（只有 Accept、Accept-Language、Content-Language 和受限的 Content-Type），任何非白名单头都触发预检。
