---
title: [WEB-036] 服务端如何正确配置 CORS？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-036：服务端如何正确配置 CORS？
**答**：
- 必须回 `Access-Control-Allow-Origin`（不能是无凭据场景下随意用 `*` 与 credentials 混用）；带凭据时必须回具体源。
- 预检请求要在 OPTIONS 里返回 `Allow-Methods`、`Allow-Headers`，并处理 `Access-Control-Max-Age` 缓存预检结果。
- `Access-Control-Expose-Headers` 控制前端能读到哪些自定义响应头。
- 动态回显 Origin 且加白名单校验，比写死 `*` 安全；切忌"把请求头原样反射回来"却不校验。

```javascript
// Express 手写 CORS 中间件（也可用 cors 包，原理一致）
const whitelist = ['https://app.example.com', 'https://admin.example.com'];

app.use((req, res, next) => {
  const origin = req.headers.origin;
  if (whitelist.includes(origin)) {
    res.setHeader('Access-Control-Allow-Origin', origin); // 带凭据时必须回具体源
    res.setHeader('Access-Control-Allow-Credentials', 'true');
    res.setHeader('Vary', 'Origin'); // 缓存按 Origin 区分，防止 CDN 串源
  }
  if (req.method === 'OPTIONS') {
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization, X-Request-Id');
    res.setHeader('Access-Control-Max-Age', '86400'); // 预检结果缓存一天，减少 OPTIONS
    return res.status(204).end();
  }
  next();
});
```
