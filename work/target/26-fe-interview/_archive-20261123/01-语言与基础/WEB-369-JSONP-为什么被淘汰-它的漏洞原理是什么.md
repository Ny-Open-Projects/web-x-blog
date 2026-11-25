---
title: [WEB-369] JSONP 为什么被淘汰？它的漏洞原理是什么？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-369：JSONP 为什么被淘汰？它的漏洞原理是什么？
**答**：
- JSONP 利用 <script> 不受同源限制，回调函数包数据执行；只能 GET、无法处理错误、依赖服务端拼接。
- 两大漏洞：回调名可控 → 服务端把恶意输入拼进 JS 上下文；响应可被任意站点引用 → 数据接口变公开接口（CSRF/信息泄露）。
- 现在 CORS 全覆盖 + CSP 默认禁 inline，JSONP 没有存在必要；面试考它是为了理解同源策略演化。

```javascript
// 反面示例：/api/user?callback=USER_CB → USER_CB({"name":"..."})
// 漏洞1: callback=alert(1)//  → 服务端原样拼接执行任意 JS
// 漏洞2: 任何站点 <script src="https://api.com/api/user?callback=x"> 偷数据
const safe = () => fetch('/api/user', { credentials: 'include' })
  .then(r => r.json());  // CORS 替代
console.log('JSONP = 同源策略的旁路，CORS 出现后废弃');
```
