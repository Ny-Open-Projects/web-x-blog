---
title: [WEB-363] 允许用户上传 SVG 为什么是 XSS 风险？怎么防？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-363：允许用户上传 SVG 为什么是 XSS 风险？怎么防？
**答**：
- SVG 是 XML，可内嵌 <script>、事件属性、foreignObject+HTML，直接访问该文件 URL 即在同源执行脚本。
- 防御组合：独立文件域（或独立域名）隔离同源、服务端 sanitize SVG（去 script/事件/外链）、加 CSP sandbox 响应头、Content-Type: image/svg+xml 仍会执行所以必须净化。
- 同理警惕：HTML 上传、PDF 内嵌 JS、EPUB 等富格式。

```javascript
// 服务端净化 SVG
const clean = svg => svg
  .replace(/<script[\s\S]*?<\/script>/gi, '')
  .replace(/ on\w+="[^"]*"/gi, '')
  .replace(/javascript:/gi, '');
// 更稳妥: 上传到 static.cdn.com 独立域，主域 Cookie 不带过去
console.log('独立域 + 净化 + CSP 三选一都要有，最好全上');
```
