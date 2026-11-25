---
title: [PER-1063] 跨域与性能的交叉问题：CORS 预检的缓存优化
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1063：跨域与性能的交叉问题：CORS 预检的缓存优化

**答**：
- 预检成本：每次跨域复杂请求多一个 OPTIONS RTT；弱网下显著拖慢。
- 优化：Access-Control-Max-Age 缓存预检（浏览器上限各不同，Chrome 7200s）；减少自定义头（能进简单请求就不预检）。
- 设计层面：同域部署 API（同源无预检）、网关统一域名、BFF 收敛跨域点。
- 度量：Network 面板统计 OPTIONS 请求数占比，高的说明头设计有问题。

```javascript
// 预检优化清单
const GOOD = {
  'Access-Control-Max-Age': '7200',                  // 预检缓存 2h
  'Access-Control-Allow-Methods': 'GET, POST',       // 收窄方法
  'Access-Control-Allow-Headers': 'Content-Type',    // 少自定义头
};
// 业务侧配合：把 X-Trace 等自定义头合并进 body 或 query，
// 让请求变为"简单请求"彻底跳过 OPTIONS
```
