---
title: [SCN-1241] AI 对话的引用上文（@提及与锚定）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1241：AI 对话的引用上文（@提及与锚定）

**答**：
- 锚定：引用历史某条回答（锚定上下文）——后续问题基于锚定内容回答。
- 渲染：引用卡片（原消息摘要+跳转）。
- 实现：锚定消息 id 注入上下文（模型可见范围控制）。

```javascript
// 消息锚定
function anchorMessage(anchorId, question) {
  const anchor = messages.get(anchorId);
  return {
    payload: { anchor: anchor.content, question,
      scope: '基于锚定内容回答' },
    ui: { card: summarize(anchor), jump: () => scrollToMsg(anchorId) },
  };
}
function scrollToMsg(id) { return true; }
function summarize(m) { return m.content.slice(0, 80); }
```
