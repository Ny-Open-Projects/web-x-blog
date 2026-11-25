---
title: [SCN-1244] AI 产品的无障碍（读屏与键盘导航对话）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1244：AI 产品的无障碍（读屏与键盘导航对话）

**答**：
- 读屏：流式输出 aria-live 更新（节流播报），消息角色标注（role 属性）。
- 键盘：消息快捷键（上条/下条/复制/重生成），焦点管理。
- 动效：打字机动效对 reduced-motion 降级（1231）。

```javascript
// 无障碍对话
function a11yChat(streamEl) {
  return {
    live: streamEl.setAttribute('aria-live', 'polite'),
    role: m => m.role === 'user' ? '你' : '助手',
    keys: { ArrowUp: 'prev-message', c: 'copy', r: 'regen' },
    reduced: matchMedia('(prefers-reduced-motion: reduce)').matches,
  };
}
```
