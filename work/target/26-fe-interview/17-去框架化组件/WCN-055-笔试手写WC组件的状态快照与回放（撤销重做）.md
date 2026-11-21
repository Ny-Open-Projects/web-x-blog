---
title: [WCN-055] 笔试：手写 WC 组件的状态快照与撤销重做（undo/redo）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Web Components]
type: 笔试题
---

## WCN-055：笔试：手写 WC 组件的状态快照与撤销重做

**题目**：为一个画板 WC 实现 `pushSnapshot(state)`、`undo()`、`redo()`：① 栈上限 50，超出丢弃最旧；② undo 后产生新状态时清除 redo 分支；③ 相邻相同状态不重复入栈（浅比较）；④ 暴露 `canUndo/canRedo` 与 `change` 事件（detail.action）；⑤ `state` 结构为 `{ shapes: [...], color }`，用结构化克隆而非 JSON 深拷贝对比。

**答**：

```javascript
class SnapshotStack {
  #undo = []; #redo = []; #cap = 50;
  pushSnapshot(state) {
    const last = this.#undo.at(-1);
    if (last && eq(last, state)) return false;      // 相邻相同不重复
    this.#undo.push(clone(state));
    if (this.#undo.length > this.#cap) this.#undo.shift(); // 超限丢最旧
    this.#redo = [];                                 // 新分支清除 redo
    return true;
  }
  undo(current) {
    if (!this.#undo.length) return null;
    this.#redo.push(clone(current));                 // 当前态进 redo 栈
    return clone(this.#undo.pop());                  // 返回上一态
  }
  redo(current) {
    if (!this.#redo.length) return null;
    this.#undo.push(clone(current));
    return clone(this.#redo.pop());
  }
  get canUndo() { return this.#undo.length > 1; }    // 栈底是初始态，不可撤销
  get canRedo() { return this.#redo.length > 0; }
}
function clone(s) { return structuredClone(s); }
function eq(a, b) { return JSON.stringify(a) === JSON.stringify(b); } // 简化浅对比口径

// 组件集成
class MiniBoard extends HTMLElement {
  #stack = new SnapshotStack();
  commit(state) {
    if (this.#stack.pushSnapshot(state)) this.#emit('commit');
    this.#render(state);
  }
  undo() {
    const prev = this.#stack.undo(this.#state());
    if (prev) { this.state = prev; this.#render(prev); this.#emit('undo'); }
  }
  redo() {
    const next = this.#stack.redo(this.#state());
    if (next) { this.state = next; this.#render(next); this.#emit('redo'); }
  }
  get canUndo() { return this.#stack.canUndo }
  get canRedo() { return this.#stack.canRedo }
  #state() { return this.state ?? { shapes: [], color: '#000' }; }
  #emit(action) {
    this.dispatchEvent(new CustomEvent('board-change',
      { bubbles: true, composed: true, detail: { action, canUndo: this.canUndo, canRedo: this.canRedo } }));
  }
  #render(s) { /* 按 s.shapes/s.color 重绘影子树 */ }
}
customElements.define('mini-board', MiniBoard);
```

**评分点**：
- 双栈模型正确：undo 把当前态压 redo 栈、redo 反向；新 push 清空 redo（分支语义）。
- 容量上限与"栈底不可撤销"的 canUndo 口径。
- 相邻去重避免无效快照堆积；structuredClone 保结构安全（JSON 也可，需说明取舍）。
- change 事件携带 action 与 canUndo/canRedo，便于工具栏联动。
