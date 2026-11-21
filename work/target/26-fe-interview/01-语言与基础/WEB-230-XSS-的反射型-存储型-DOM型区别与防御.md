---
title: [WEB-230] XSS 的反射型、存储型、DOM 型区别与防御
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-230：XSS 的反射型、存储型、DOM 型区别与防御

**答**：
- 反射型：恶意脚本在 URL 参数中，服务端把它拼进响应页面（搜索回显），需诱导点击链接，一次性。
- 存储型：脚本存进数据库（评论区 `<img onerror=...>`），所有访问者中招，危害最大。
- DOM 型：纯前端问题——`innerHTML`、`location.hash` 等把不可信数据直接写入 DOM，不经过服务端，静态站点也会中。
- 防御分层：框架默认转义（React/Vue 文本插值）是第一道；确需 HTML 时用 DOMPurify 白名单净化；URL 用 encodeURIComponent；富文本服务端再滤一遍；CSP 兜底限制脚本来源。
- 高频误区：转义输入不如转义输出（不同输出上下文 HTML 属性/JS 字符串/CSS 转义规则不同）；`innerHTML = DOMPurify.sanitize(...)` 才安全。

```javascript
// 三种典型注入点
const name = new URLSearchParams(location.search).get('name');
el.innerHTML = name;                       // DOM XSS!
el.textContent = name;                     // 安全：纯文本

// 富文本白名单净化
import DOMPurify from 'dompurify';
el.innerHTML = DOMPurify.sanitize(dirtyHtml, {
  ALLOWED_TAGS: ['b', 'i', 'a', 'img'],
  ALLOWED_ATTR: ['href', 'src', 'alt'],
});
```
