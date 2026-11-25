---
title: [NODE-355] Node 服务的响应头安全与 SSR/XSS 服务端防线如何配置？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-355：响应头安全与服务端 XSS 防线
**答**:
- 服务端安全头清单（Helmet 类中间件统一出口）：CSP（ARC-155 前端配合）、X-Content-Type-Options: nosniff、X-Frame-Options/CSP frame-ancestors（防点击劫持）、Referrer-Policy、HSTS（HTTPS 强制 + preload）、Permissions-Policy。
- SSR XSS 防线：模板引擎自动转义（EJS <%- 是洞，只用于可信 HTML）；服务端插值数据 JSON 序列化防 </script> 逃逸（JSON.stringify 后替换 < 为 \\u003c）；富文本输出走净化白名单（与前端同源规则）。
- 状态外注：window.__INITIAL__ 注入前做类型清洗（不接受任意对象直插）。
- API 层：下载响应防 MIME 混淆、JSONP 禁用、open redirect（Location 拼接用户输入 → 白名单域校验）。
- 验证：安全头基线做成集成测试断言（每个响应断言关键头存在），CSP 违规报告接监控。
```javascript
// SSR 数据注入防逃逸
const safe = JSON.stringify(state).replace(/</g, '\\u003c');     // 防 </script> 断开
res.render('app', { initial: safe });
// 安全头
app.use(helmet({
  contentSecurityPolicy: { directives: { defaultSrc: ["'self'"], scriptSrc: ["'self'", "'nonce-{NONCE}'"] } },
  hsts: { maxAge: 31536000, includeSubDomains: true }
}));
```
