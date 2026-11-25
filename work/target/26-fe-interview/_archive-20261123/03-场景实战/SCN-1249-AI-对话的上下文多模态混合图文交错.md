---
title: [SCN-1249] AI 对话的上下文多模态混合（图文交错对话）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1249：AI 对话的上下文多模态混合（图文交错对话）

**答**：
- 混合：图文交错（用户发图提问，模型图文混合回复）渲染顺序保持。
- 实现：消息 content 数组（text/image 段），渲染按序。
- 复制：图文混合复制（图片链接+文本）。

```javascript
// 图文混合
function renderMixed(content) {                       // content: [{ type, ... }]
  return content.map(c => c.type === 'text'
    ? `<p>${escapeHtml(c.text)}</p>`
    : `<img src="${c.url}" alt="${c.alt ?? ''}">`).join('');
}
// 模型回复顺序：文本段落与图表交替，保持语义连贯
```
