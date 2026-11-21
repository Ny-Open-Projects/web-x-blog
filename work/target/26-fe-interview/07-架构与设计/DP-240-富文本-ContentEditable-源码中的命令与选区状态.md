---
title: [DP-240] 源码识别：富文本编辑器源码中的命令与选区状态机？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-240：源码识别：富文本编辑器源码中的命令与选区状态机？
**答**:
- 命令模式（核心）：execCommand 换成自己的事务（transaction）：insertText/toggleBold 都是命令对象，编辑器历史栈存事务序列（ProseMirror/Slate 同构）。
- 选区状态机：selection 变化（selectionchange 事件）驱动 UI 状态（工具栏激活态），选区是"独立于文档的可观察状态"。
- 备忘录：每次事务后存 doc snapshot 或逆向事务（undo stack），协作者用 OT/CRDT 合并事务。
- 识别要点：能解释"输入法 IME 期间不能派发事务"（compositionstart/end 是特殊状态）——中文输入场景的坑。

```javascript
// 富文本事务（源码级简化）
class Editor {
  history = []; future = [];
  apply(transaction) {                                   // 命令模式
    const inverse = transaction.invert(this.doc);        // 逆向命令（备忘录）
    this.doc = transaction.apply(this.doc);
    this.history.push({ t: transaction, inv: inverse });
    this.future = [];                                    // 新输入清空 redo
    this.emitter.emit('update', this.doc);
  }
  undo() { const e = this.history.pop(); if (!e) return;
    this.doc = e.inv.apply(this.doc); this.future.push(e.t); }   // 逆命令回滚
  redo() { const t = this.future.pop(); if (!t) return; this.apply(t); }
}
// 选区观察：document.addEventListener('selectionchange', () => {
//   const sel = getSelection(); toolbar.setActive(queryBold(sel)) })   —— 选区驱动 UI 状态
// IME：compositionstart → 暂停事务派发；compositionend → 整段输入作为一个事务（防拆散拼音）
```
