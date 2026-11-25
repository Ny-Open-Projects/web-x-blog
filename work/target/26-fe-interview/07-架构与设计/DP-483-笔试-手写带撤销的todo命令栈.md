---
title: [DP-483] 笔试：手写命令模式（撤销/重做/合并）
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 笔试题, 设计模式]
type: 笔试题
---

## DP-483：笔试：手写命令模式

**答**：实现编辑器的命令历史 `CommandHistory`：① Command：{ execute, undo, label, merge? }；② execute：执行 + 入 undo 栈 + 清空 redo 栈；③ undo/redo：对称移动栈指针；④ 合并协议：连续同类命令（500ms 内的输入）merge 成一条（不堆撤销点）；⑤ 上限与瘦身：栈上限 100——溢出丢最旧；命令只存 diff 不存全量（内存管理）；⑥ golden 断言：undo 后 redo 应恢复一致。写出实现与测试要点。

```javascript
class CommandHistory {
  #undo = []; #redo = []; #capacity = 100; #lastAt = 0;
  execute(cmd, now = Date.now()) {
    // 合并: 同类且 500ms 内
    const top = this.#undo.at(-1);
    if (top?.label === cmd.label && now - this.#lastAt < 500 && top.merge) {
      const merged = top.merge(cmd);
      if (merged) { this.#undo[this.#undo.length - 1] = merged; this.#lastAt = now; return; }
    }
    cmd.execute();
    this.#undo.push(cmd);
    if (this.#undo.length > this.#capacity) this.#undo.shift();   // 溢出丢最旧
    this.#redo = [];                                   // 新操作清 redo
    this.#lastAt = now;
  }
  undo() { const c = this.#undo.pop(); if (c) { c.undo(); this.#redo.push(c); } }
  redo() { const c = this.#redo.pop(); if (c) { c.execute(); this.#undo.push(c); } }
  get canUndo() { return this.#undo.length > 0; }
  get canRedo() { return this.#redo.length > 0; }
}
// 测试: execute→undo 后状态与初始一致; undo→redo 后状态与 execute 后一致
// merge: 输入命令连续 → 一条 (合并协议: cmd.merge(next) 返回合并结果或 null)
```

**评分点**：
- merge 协议（连续输入合并不堆撤销点——编辑器标准）
- 新操作清空 redo（git 语义）
- 溢出丢最旧 + 只存 diff（内存管理）
- 对称性 golden 断言（undo/redo 后状态一致）
