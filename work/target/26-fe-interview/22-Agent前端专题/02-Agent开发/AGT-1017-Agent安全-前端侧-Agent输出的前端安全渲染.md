---
title: [1017] 前端渲染 Agent 输出有哪些安全点
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 前端安全]
type: 面试题
---

## 1017：前端渲染 Agent 输出有哪些安全点

**答**：
- Agent 输出当不可信 HTML 处理：markdown 渲染必须白名单标签（禁 script/iframe/事件属性），链接协议白名单（禁 javascript:/data:），这是 Agent 场景 XSS 的主战场。
- 代码块渲染：高亮库注入的 HTML 也要过 sanitizer；「复制代码」按钮复制原文（去转义），展示与复制分离。
- 流式渲染的特有风险：半截 markdown 可能意外形成标签（如未闭合的 <img onerror=...），流式期间先按纯文本渲染或每帧 sanitize 后再插入。
- 追问钩子：为什么 dangerouslySetInnerHTML 前必须 sanitize 两次（生成时 + 渲染时）？——防线分离：生成侧防注入源头，渲染侧防「上游已被污染」（如检索内容带毒）。

```ts
import DOMPurify from 'dompurify';
function renderAgentOutput(md) {
  const html = mdToHtml(md);
  return DOMPurify.sanitize(html, {
    ALLOWED_TAGS: ['p','code','pre','a','ul','li','table','img','h1','h2','h3'],
    ALLOWED_ATTR: ['href','src','alt','class'],
    ALLOWED_URI_REGEXP: /^(https?:|mailto:)/,     // 禁 javascript:/data:
  });
}
// 流式期间：逐帧 sanitize，半截标签也不会执行
stream.on('delta', d => el.innerHTML = renderAgentOutput(accumulated += d));
```
