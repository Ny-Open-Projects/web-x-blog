---
title: [WCN-432] 笔试：实现元素的 renderDSD（SSR 输出声明式 shadow）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-432：笔试：实现元素的 renderDSD（SSR 输出声明式 shadow）。
**题目**：`renderDSD(props)`：输出 `<ds-x><template shadowrootmode="open">样式+内容</template>…</ds-x>`；props 转义（XSS）；数据注入 data-state（base64 JSON）供水合恢复。

```javascript
const esc = s => String(s).replace(/[&<>"']/g, c =>
  ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
function renderDSD(props) {
  const state = Buffer.from(JSON.stringify({ sku: props.sku })).toString('base64');
  return `<ds-goods sku="${esc(props.sku)}" data-state="${state}">` +
    `<template shadowrootmode="open"><style>.p{color:var(--ds-price)}</style>` +
    `<b class="p">${esc(props.title)}</b></template></ds-goods>`;
}

```

**评分点**：
- HTML 转义（escapeHtml 全部插值）。
- 模板结构与服务端/客户端渲染同源（同一 bodyHtml 函数）。
- data-state 序列化（base64 JSON）+ 白名单字段。
- 输出单行压缩（体积）。
