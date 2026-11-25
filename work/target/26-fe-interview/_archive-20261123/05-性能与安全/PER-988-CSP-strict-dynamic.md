---
title: [PER-988] CSP strict-dynamic 与 nonce 的组合如何工作
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-988：CSP strict-dynamic 与 nonce 的组合如何工作

**答**：
- nonce 模式：每次响应生成随机 nonce，只有带该 nonce 的脚本可执行，彻底封死注入的内联脚本。
- strict-dynamic：信任通过 nonce 脚本动态创建的脚本（document.createElement 注入），解决第三方加载器（GTM 等）的合规问题，同时浏览器自动忽略 allowlist。
- 迁移路径：Report-Only 先跑两周收集违反报告 → 修补 → 强制开启；老代码 allowlist 与 strict-dynamic 不可混用（后者会忽略前者）。
- 坑：缓存了 nonce 的页面（CDN 缓存 HTML）导致 nonce 复用失效——nonce 页面必须 no-store 或按请求生成。

```javascript
// Express 中间件：每请求 nonce
app.use((req, res, next) => {
  res.locals.nonce = crypto.randomBytes(16).toString('base64');
  res.setHeader('Content-Security-Policy',
    `script-src 'nonce-${res.locals.nonce}' 'strict-dynamic'; ` +
    `object-src 'none'; base-uri 'none'`);
  next();
});
// 模板：<script nonce="<%= nonce %>">app.js 加载器</script>
// 加载器动态注入的第三方脚本自动被 strict-dynamic 信任
```
