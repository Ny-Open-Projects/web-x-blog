---
title: [WEB-368] CORS 预检请求（OPTIONS）是怎么缓存的？Max-Age 有什么讲究？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-368：CORS 预检请求（OPTIONS）是怎么缓存的？Max-Age 有什么讲究？
**答**：
- 非简单请求先发 OPTIONS 预检（带 Access-Control-Request-Method/Headers），服务器返回允许范围，通过才发真实请求。
- 预检结果可缓存：Access-Control-Max-Age: 86400，浏览器对同 URL 的后续预检免发；Chrome 上限约 2h，Firefox 24h。
- 注意：Max-Age 缓存按 URL 粒度；GET 简单请求不触发预检，带自定义头（如 Authorization 之外的自定义 token 头）就会触发。

```javascript
// 预检响应
// Access-Control-Allow-Origin: https://app.com
// Access-Control-Allow-Methods: GET, POST
// Access-Control-Allow-Headers: X-Token
// Access-Control-Max-Age: 86400
const needsPreflight = (req) =>
  !['GET', 'HEAD', 'POST'].includes(req.method)
  || Object.keys(req.headers).some(h => !simpleHeaders.includes(h));
console.log('带 X-Token 头 → 必预检 → 配 Max-Age 省往返');
```
