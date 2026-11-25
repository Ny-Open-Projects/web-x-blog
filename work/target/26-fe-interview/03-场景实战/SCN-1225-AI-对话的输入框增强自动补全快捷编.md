---
title: [SCN-1225] AI 对话的输入框增强（自动补全/快捷编辑）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1225：AI 对话的输入框增强（自动补全/快捷编辑）

**答**：
- 增强：输入自动补全（模板/历史 prompt 联想）、多行编辑（Shift+Enter 换行）、引用上文（@消息）。
- 草稿：未发送草稿自动保存（切会话保留）。
- 粘贴：富文本粘贴降级为纯文本（防格式混乱）。

```javascript
// 输入增强
function chatInput(el, store) {
  el.addEventListener('keydown', e => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); submit(); }
  });
  el.addEventListener('input', debounce(500, () =>
    store.setDraft(sessionId, el.value)));             // 草稿保存
  el.addEventListener('paste', e => {
    e.preventDefault();
    insertAtCursor(el, e.clipboardData.getData('text/plain'));   // 纯文本
  });
}
function insertAtCursor(el, text) { el.value += text; }
function debounce(ms, fn) { return fn; }
function submit() {}
```
