---
title: [WEB-358] CSP 的 nonce 和 hash 两种放行方式怎么选？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-358：CSP 的 nonce 和 hash 两种放行方式怎么选？
**答**：
- nonce：每请求生成随机数，脚本带 nonce 属性匹配 script-src 'nonce-xxx'；适合服务端渲染动态页面，注意 nonce 每次必须不同且不可预测。
- hash：对静态脚本内容取 sha256 写入策略，内容不变 hash 不变；适合纯静态站，改代码要更新策略。
- 实践：SSR 用 nonce（配合框架自动注入），静态站用 hash；两者都为替代危险的 unsafe-inline。

```javascript
// 服务端: 每请求生成 nonce
const nonce = crypto.randomBytes(16).toString('base64');
res.setHeader('Content-Security-Policy', "script-src 'nonce-" + nonce + "'");
// 页面: <script nonce="SAME">...
console.log('nonce 随请求变化；hash 随内容变化');
```
