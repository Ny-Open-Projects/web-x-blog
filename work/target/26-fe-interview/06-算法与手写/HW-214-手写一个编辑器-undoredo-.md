---
title: [HW-214] 手写一个编辑器 undo/redo 命令栈：批量操作合并与选区恢复
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-214：手写一个编辑器 undo/redo 命令栈：批量操作合并与选区恢复

**答**：
- 需求：实现 EditorHistory：push({inverse, after, cursor})（inverse 为回退操作），undo/redo（上限 100 条）；连续同源操作合并（如同一次连打 500ms 内合并为一个单元）；undo 后光标恢复到操作前位置。
- 边界：redo 栈在 push 新操作时清空；合并条件（时间窗+同命令类型）可配置；栈满淘汰最旧。
- 评分点：光标恢复；合并窗口；redo 清空时机。

```javascript
class EditorHistory {
  constructor({ limit = 100, mergeMs = 500 } = {}) {
    this.undo = []; this.redo = []; this.limit = limit; this.mergeMs = mergeMs;
    this.last = null;
  }
  push(op) {
    const now = Date.now();
    const top = this.undo.at(-1);
    if (top && top.type === op.type && now - top.t < this.mergeMs) {
      top.inverse = [...op.inverse, ...top.inverse];   // 合并：新逆操作在前
      top.t = now;
    } else {
      this.undo.push({ ...op, t: now });
      if (this.undo.length > this.limit) this.undo.shift();
    }
    this.redo = [];                                // 新操作清空 redo
    this.last = op.cursor;
  }
  undo() {
    const op = this.undo.pop();
    if (!op) return null;
    op.inverse();                                  // 执行逆操作
    this.redo.push(op);
    return op.cursor;                              // 光标恢复
  }
  redo() {
    const op = this.redo.pop();
    if (!op) return null;
    op.after();
    this.undo.push(op);
    return op.cursorAfter;
  }
}
```
