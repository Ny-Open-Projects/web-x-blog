---
title: [PER-990] CORS 的深水点：预检、凭据与缓存陷阱
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-990：CORS 的深水点：预检、凭据与缓存陷阱

**答**：
- 简单请求直接发送；带自定义头/PUT 等触发 OPTIONS 预检，预检响应 Access-Control-Allow-* 决定是否放行。
- 凭据模式（credentials: include）要求服务器 ACAO 指定确切来源（不可 *）+ ACAC: true，且 Origin 必须在白名单——动态回显 Origin 是高危配置。
- 缓存陷阱：浏览器缓存预检结果（ACMaxAge），服务端策略变更后旧缓存仍放行；跨域响应若被 CDN 缓存且带 ACAO: *，会污染其他来源。
- 深水：ACAO 与 Vary: Origin——CDN 缓存跨域响应必须带 Vary: Origin，否则 A 域的缓存响应配 B 域的 ACAO 造成混乱或泄露。

```javascript
// 安全的 CORS 中间件
const WHITELIST = ['https://shop.example.com', 'https://m.example.com'];
app.use((req, res, next) => {
  const origin = req.headers.origin;
  if (WHITELIST.includes(origin)) {
    res.setHeader('Access-Control-Allow-Origin', origin);   // 精确回显
    res.setHeader('Vary', 'Origin');                        // CDN 缓存隔离
    res.setHeader('Access-Control-Allow-Credentials', 'true');
  }
  if (req.method === 'OPTIONS') {
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, X-Trace');
    res.setHeader('Access-Control-Max-Age', '600');
    return res.end();
  }
  next();
});
```
