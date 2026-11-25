---
title: [SCN-1205] AI 回复的代码块渲染与复制体验
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1205：AI 回复的代码块渲染与复制体验

**答**：
- 渲染：代码块语法高亮（highlight.js/Prism 按语言）、行号、复制按钮（一键复制整块）。
- 流式：代码块流式期间显示"生成中"标记，闭合后完整高亮。
- 长代码：超长代码折叠（展开查看）+ 横向滚动。

```javascript
// 代码块渲染
function codeBlock(code, lang) {
  return {
    html: highlight(code, lang),
    actions: { copy: () => navigator.clipboard.writeText(code),
      collapse: code.split('\n').length > 20 },
    streaming: false,
  };
}
function highlight(code, lang) { return `<pre><code>${escapeHtml(code)}</code></pre>`; }
function escapeHtml(s) { return s.replace(/&/g, '&amp;').replace(/</g, '&lt;'); }
```
