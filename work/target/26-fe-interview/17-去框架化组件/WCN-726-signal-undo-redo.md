---
title: [WCN-726] 如何用 Signals 设计一个可撤销/重做的操作历史（undo/redo）？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-726：如何用 Signals 设计一个可撤销/重做的操作历史（undo/redo）？

**答**：
- 结论：把每次状态变更记录为「补丁（oldValue→newValue）」压入 past 栈；undo 时反向应用补丁并压入 future 栈，redo 反之；用 signal 暴露 canUndo/canRedo。
- 关键：只对「用户意图」记录历史而非每次细粒度赋值，用 batch 把一次操作合并为一条；限制栈深度防内存膨胀。
- 追问钩子：异步操作（如保存成功）如何纳入历史？考察「乐观更新 + 失败回滚」与历史栈的协同。

```javascript
function createHistory(initial) {
  const past = signal([]), future = signal([]), state = signal(initial.value);
  function apply(patch, dir) { state.value = dir === 'do' ? patch.next : patch.prev; }
  function commit(next) {
    past.value = [...past.value, { prev: state.value, next }];
    future.value = [];
    state.value = next;
  }
  function undo() {
    const p = past.value.pop();
    if (!p) return;
    apply(p, 'undo'); future.value = [...future.value, p];
  }
  function redo() {
    const p = future.value.pop();
    if (!p) return;
    apply(p, 'redo'); past.value = [...past.value, p];
  }
  return { state, commit, undo, redo, canUndo: () => past.value.length > 0 };
}
console.log(typeof createHistory);
```
