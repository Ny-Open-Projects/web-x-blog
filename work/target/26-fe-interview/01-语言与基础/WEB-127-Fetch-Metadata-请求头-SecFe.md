---
title: [WEB-127] Fetch Metadata 请求头（Sec-Fetch-*）如何用于请求隔离？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-127：Fetch Metadata 请求头（Sec-Fetch-*）如何用于请求隔离？
**答**：
- 浏览器自动附带只读头：`Sec-Fetch-Site`（none/same-origin/same-site/cross-site，谁发起的）、`Sec-Fetch-Mode`（navigate/cors/no-cors 等）、`Sec-Fetch-Dest`（目标上下文 document/script/img 等）、`Sec-Fetch-User`。
- 价值：服务端第一次能"零成本"判断请求的真实语境，替代易被伪造的 Referer/Origin 组合判断，防 CSRF、防资源热链、防跨站表单攻击。
- 典型策略：`cross-site + navigate` 的 POST 拒绝（CSRF）；`Dest: document` 且 `Site: cross-site` 的嵌套请求拒绝（防嵌入）。
- 注意：Sec-Fetch-* 由浏览器强制，JS 无法伪造；非浏览器客户端没有这些头，需另行认证。

```javascript
// Node/Express 中间件：基于 Fetch Metadata 的资源隔离
app.use((req, res, next) => {
  const site = req.headers['sec-fetch-site'];   // none | same-origin | same-site | cross-site
  const mode = req.headers['sec-fetch-mode'];   // navigate | cors | no-cors ...
  const dest = req.headers['sec-fetch-dest'];   // document | script | image ...

  if (req.method === 'POST' && site === 'cross-site') {
    return res.status(403).end('CSRF 防护：拒绝跨站 POST');     // 1. 防 CSRF
  }
  if (dest === 'document' && site === 'cross-site') {
    return res.status(403).end('禁止被跨站 iframe 嵌套');        // 2. 防点击劫持
  }
  if (mode === 'no-cors' && dest !== 'image') {
    return res.status(403).end('禁止 no-cors 窃取数据');         // 3. 防侧信道
  }
  next();
});
```
