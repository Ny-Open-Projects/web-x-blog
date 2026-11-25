---
title: [SCN-1217] AI 对话的移动端适配（键盘/长文/横竖屏）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1217：AI 对话的移动端适配（键盘/长文/横竖屏）

**答**：
- 键盘：软键盘弹起输入框跟随（visualViewport 适配 418）、滚动到底（新消息）。
- 长文：长回复折叠（展开全文）、代码块横向滚动。
- 横屏：iPad 横屏双栏（会话列表+对话）。

```javascript
// 移动端对话
function mobileChatAdapt(vv, chatEl) {
  vv.addEventListener('resize', () => {
    chatEl.style.height = `${vv.height - headerH()}px`;   // 键盘适配
    scrollToBottom(chatEl);
  });
  return {
    longReply: { foldPx: 600, expand: true },
    landscape: matchMedia('(orientation: landscape)').matches ? 'two-col' : 'single',
  };
}
function headerH() { return 56; }
function scrollToBottom(el) { el.scrollTop = el.scrollHeight; }
```
