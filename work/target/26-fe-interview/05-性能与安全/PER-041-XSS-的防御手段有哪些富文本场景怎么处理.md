---
title: [PER-041] XSS 的防御手段有哪些？富文本场景怎么处理？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-041：XSS 的防御手段有哪些？富文本场景怎么处理？

**答**：
- 纯文本输出：HTML 实体转义 `& < > " '`，或使用框架默认转义（React 的 JSX、Vue 的插值）。
- 富文本必须渲染 HTML 时：用 **DOMPurify** 这类白名单过滤库清洗后再插入，绝不要自己写黑名单正则替换。
- 配合纵深防御：CSP 限制脚本来源、`HttpOnly` 让 JS 读不到 cookie、输入侧做长度与格式校验。
- 常见误区：`v-html`、`dangerouslySetInnerHTML` 直接渲染接口数据，等于放弃框架的转义保护。

```javascript
// 纯文本场景：HTML 实体转义
function escapeHTML(str = '') {
  const map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' };
  return String(str).replace(/[&<>"']/g, (ch) => map[ch]);
}
el.textContent = escapeHTML(userInput); // textContent 本身不解析 HTML，双保险

// 富文本场景：白名单过滤，而不是黑名单替换
import DOMPurify from 'dompurify';

const dirty = '<img src=x onerror=alert(1)><b>hello</b>';
const clean = DOMPurify.sanitize(dirty, { ALLOWED_TAGS: ['b', 'i', 'p', 'a'] });
el.innerHTML = clean; // => <b>hello</b>，onerror 脚本已被剥离
```
