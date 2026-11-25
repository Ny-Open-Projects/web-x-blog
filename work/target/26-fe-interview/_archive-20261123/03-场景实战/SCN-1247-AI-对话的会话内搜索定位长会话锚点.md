---
title: [SCN-1247] AI 对话的会话内搜索定位（长会话锚点）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1247：AI 对话的会话内搜索定位（长会话锚点）

**答**：
- 定位：长会话内搜索（关键词高亮+滚动定位），时间轴跳转（按时间锚点）。
- 结构：会话大纲（问题列表侧栏）一键跳转（长会话导航）。
- 体验：搜索结果上下文展开（定位后前后文可见）。

```javascript
// 会话大纲
function sessionOutline(messages) {
  const questions = messages.filter(m => m.role === 'user');
  return questions.map(q => ({
    id: q.id, brief: q.content.slice(0, 40),
    index: messages.indexOf(q),
    jump: () => scrollToMsg(q.id),
  }));
}
```
