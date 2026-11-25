---
title: [SCN-1208] AI 对话的思考过程（Reasoning）展示
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1208：AI 对话的思考过程（Reasoning）展示

**答**：
- 展示：reasoning 模型的思考过程（thinking 流式）——折叠区展示（默认收起）。
- 区分：思考 token 与回答 token 分流渲染（事件类型区分）。
- 性能：思考流只更新折叠区摘要（避免大量 DOM）。

```javascript
// 思考流分流
function chatStreamHandler(event) {
  if (event.type === 'thinking')
    return { area: 'thinking', delta: event.delta };   // 折叠区
  if (event.type === 'content')
    return { area: 'answer', delta: event.delta };
  if (event.type === 'tool')
    return { area: 'tool', delta: event.delta };
}
// thinking 区默认收起，实时更新"思考中...（N 字）"摘要
```
