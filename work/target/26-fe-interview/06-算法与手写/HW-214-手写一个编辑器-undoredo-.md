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
    this.undoStack = []; this.redoStack = []; this.limit = limit; this.mergeMs = mergeMs;
    this.last = null;
  }
  push(op) {
    const now = Date.now();
    const top = this.undoStack.at(-1);
    if (top && top.type === op.type && now - top.t < this.mergeMs) {
      const prevInv = top.inverse, prevAfter = top.after;
      top.inverse = () => { op.inverse(); prevInv(); };   // 合并：新逆操作先执行
      top.after = () => { prevAfter(); op.after(); };
      top.t = now;
    } else {
      this.undoStack.push({ ...op, t: now });
      if (this.undoStack.length > this.limit) this.undoStack.shift();
    }
    this.redoStack = [];                           // 新操作清空 redo
    this.last = op.cursor;
  }
  undo() {
    const op = this.undoStack.pop();
    if (!op) return null;
    op.inverse();                                  // 执行逆操作
    this.redoStack.push(op);
    return op.cursor;                              // 光标恢复
  }
  redo() {
    const op = this.redoStack.pop();
    if (!op) return null;
    op.after();
    this.undoStack.push(op);
    return op.cursorAfter;
  }
}
```

## 补充：评分点与变体

**评分点**：

- push 新操作时立刻清空 redo 栈，否则 redo 会把旧分支重放到已分叉的历史上
- 合并条件要同时看时间窗与命令类型，只看 500ms 会把「加粗」和「输入」误并成一个单元
- undo 后用 inverse 里带的 cursor 恢复位置，取当前光标会把位置停在错误处
- 栈满淘汰最旧时若存在快照基准，要同步修正深度计数，否则 undo 深度与实际不符

**变体与延伸**：

1. 异步操作（先请求后插入）如何进栈 → 请求成功后才 push，或先 push 一个 pending 单元再回填结果
2. 协同场景下本地 undo 会撤到别人吗 → 只撤自己的 op，按作者过滤定位，不能简单弹栈顶
3. 合并窗口跨过一次保存怎么办 → 在保存点插入不可合并的 barrier 单元，窗口遇到 barrier 即重置
