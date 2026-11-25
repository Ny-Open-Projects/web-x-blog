---
title: [V3-440] 笔试：手写 confirm 的 Promise 化封装（含快捷键与焦点管理）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-440：笔试：手写 confirm 的 Promise 化封装（含快捷键与焦点管理）
**答**：实现 `confirm(options) → Promise<boolean>`：挂载弹窗组件，Esc 取消、Enter 确认；打开时焦点移到确认按钮（a11y）；弹窗关闭后移除组件并清理事件；重复调用允许多个并存（各自独立 promise）。

```javascript
let container
function confirm({ title, content, confirmText = '确定', cancelText = '取消' }) {
  container ||= document.createElement('div')
  document.body.appendChild(container)
  return new Promise(resolve => {
    const app = createApp(ConfirmDialog, {
      title, content, confirmText, cancelText,
      onResult: (ok) => { resolve(ok); app.unmount(); if (!container.childNodes.length) container.remove() }
    })
    const inst = app.mount(container)
    // ConfirmDialog 内部：
    // onMounted: nextTick(() => confirmBtnRef.value?.focus())
    // onKeydown: Esc -> onResult(false); Enter -> onResult(true)
  })
}
```
**评分点**：
- Promise 生命周期闭环（resolve 后 unmount）。
- 快捷键处理（Esc/Enter）与焦点管理（a11y）。
- 事件清理与容器按需移除。
- 多实例并存（每次 createApp 独立或组件数组管理，说出其一）。
