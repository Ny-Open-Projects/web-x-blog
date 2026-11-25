---
title: [NODE-029] 模板渲染（SSR 输出）与前端框架 SSR 有何不同？如何实现？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-029：模板渲染（SSR 输出）与前端框架 SSR 有何不同？如何实现？
**答**：
- 传统模板渲染：服务端把数据填进模板（EJS/Handlebars/Pug）输出**完整 HTML 字符串**，浏览器一次拿到可渲染的文档；逻辑在服务端，前端只做少量交互（jQuery 时代）。
- React/Vue SSR：服务端执行**组件代码**生成 HTML（`renderToString`/`renderToPipeableStream`），还要下发 hydration 数据让客户端"复活"为可交互应用——多了 hydrate 步骤与双份执行。
- 生产要点：模板缓存（编译一次多次渲染）、HTML 转义防 XSS（`<%= %>` 转义 vs `<%- %>` 原样输出）、大页面用流式模板减少 TTFB。

```javascript
// 极简模板引擎（替换 {{var}} 与 {{#each}}）
function render(template, data) {
  return template
    .replace(/\{\{#each (\w+)\}\}([\s\S]*?)\{\{\/each\}\}/g, (_, key, body) =>
      (data[key] || []).map((item) => body.replace(/\{\{(\w+)\}\}/g, (__, k) => escapeHtml(String(item[k])))).join(''))
    .replace(/\{\{(\w+)\}\}/g, (_, key) => escapeHtml(String(data[key] ?? '')));
}
function escapeHtml(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

const tpl = fs.readFileSync('list.html', 'utf8'); // <h1>{{title}}</h1>{{#each users}}<li>{{name}}</li>{{/each}}
const http = require('node:http');
http.createServer((req, res) => {
  const data = { title: '用户列表 <script>alert(1)</script>', users: [{ name: 'Alice' }, { name: 'Bob' }] };
  res.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
  res.end(render(tpl, data)); // title 中的 script 被转义，防存储型 XSS
}).listen(3000);
```
