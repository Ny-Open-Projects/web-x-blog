---
title: [ALG-199] 画板要支持 Ctrl+Z / Ctrl+Y 撤销重做；全局弹窗要支持"后开的在上层、Esc 只关最顶层"。两类栈如何设计？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-199：画板要支持 Ctrl+Z / Ctrl+Y 撤销重做；全局弹窗要支持"后开的在上层、Esc 只关最顶层"。两类栈如何设计？
**答**：命令栈（undo/redo）：每条命令封装 `{ do, undo }`；execute 时执行并压 undo 栈、清空 redo 栈（新分支）；undo 弹栈执行 undo 并压入 redo 栈；redo 反向。O(1) 每步，内存 O(limit)。弹窗栈（z-order）：open 压栈并按栈深分配 zIndex（保证后开在上）；全局 Esc 监听只 `closeTop()`，焦点管理同理——永远操作栈顶。两者本质都是"操作序列 + 只在栈顶进出"。

```javascript
// 命令栈：撤销重做
class CommandHistory {
  constructor(limit = 50) { this.undoStack = []; this.redoStack = []; this.limit = limit; }
  execute(cmd) {                          // cmd: { do(), undo() }
    cmd.do();
    this.undoStack.push(cmd);
    if (this.undoStack.length > this.limit) this.undoStack.shift(); // 容量上限
    this.redoStack = [];                  // 新操作使 redo 分支失效
  }
  undo() { const c = this.undoStack.pop(); if (c) { c.undo(); this.redoStack.push(c); } }
  redo() { const c = this.redoStack.pop(); if (c) { c.do(); this.undoStack.push(c); } }
}
// 弹窗栈：z-order 与 Esc 只关最顶层
class ModalStack {
  constructor() { this.stack = []; }
  open(modal) {
    this.stack.push(modal);
    modal.el.style.zIndex = 1000 + this.stack.length; // 后开必在上层
  }
  closeTop() { const m = this.stack.pop(); m?.onClose(); }
}
// 全局 Esc：document.addEventListener('keydown', e => e.key === 'Escape' && modalStack.closeTop())
```
