---
title: [SCN-027] 富文本编辑器的内容会回显给其他用户，如何防 XSS？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-027：富文本编辑器的内容会回显给其他用户，如何防 XSS？
**答**：
- 原则：富文本绝不能 v-html / innerHTML 直出用户输入，必须在入库前或渲染前做白名单过滤。
- 用 DOMPurify：默认清除 script 与事件属性，通过 ALLOWED_TAGS / ALLOWED_ATTR 只放行业务需要的标签，并禁掉 javascript: 等危险协议。
- 纵深防御：后端同样过滤一遍，页面加 CSP 响应头，即使漏过滤也难以执行外域脚本。

```javascript
import DOMPurify from 'dompurify';

// 白名单过滤：只保留业务允许的标签与属性
function sanitizeRichText(dirty) {
  return DOMPurify.sanitize(dirty, {
    ALLOWED_TAGS: ['p', 'br', 'b', 'i', 'u', 'img', 'a', 'ul', 'ol', 'li', 'span'],
    ALLOWED_ATTR: ['href', 'src', 'alt', 'class', 'target'],
    FORBID_ATTR: ['style', 'onerror', 'onclick'],   // 内联样式与事件属性一律禁掉
    ALLOWED_URI_REGEXP: /^(?:https?|mailto):/i,     // 禁 javascript: 等危险协议
  });
}

// Vue 中回显：<div v-html="sanitizeRichText(article.content)"></div>
// 约定：v-html 绑定的内容必须永远是过滤后的，原始内容不进入状态树
```
