---
title: [ARC-387] 前端数据快照与撤销体系（undo/redo）架构如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-387：前端数据快照与撤销体系（undo/redo）架构如何设计？
**答**:
- 两种实现：状态快照（每次操作存全量/结构共享快照，简单但内存大）与命令模式（存操作+逆操作，内存小但要为每个操作实现 invert，ARC-054）。
- 工程选型：操作类型少且明确 → 命令模式；编辑器类操作复杂 → 快照 + 不可变结构共享（Immer/CRDT 快照），配合上限（如 100 步）控制内存。
- 快照体系要点：快照触发合并策略（连续输入 500ms 合并为一步，否则撤销会按字符退）；快照带元数据（操作者/时间/标签）；崩溃恢复用最近快照 + 草稿。
- 与协作的交叉：协作场景撤销只能撤销自己的 op（CRDT undo 是本地 op 序列回滚），不能全局回滚他人修改——这是 CRDT undo 的架构难点。
- 服务端快照：重要节点存版本（用户可见的历史版本），支持版本预览与回滚，与本地 undo 是两套体系。
```javascript
class History {
  constructor(limit = 100) { this.stack = []; this.idx = -1; this.limit = limit; }
  push(state) {
    this.stack = this.stack.slice(0, this.idx + 1);      // 丢弃 redo 分支
    this.stack.push(structuralShare(state));
    if (this.stack.length > this.limit) this.stack.shift();
    this.idx = this.stack.length - 1;
  }
  undo() { return this.idx > 0 ? this.stack[--this.idx] : null; }
  redo() { return this.idx < this.stack.length - 1 ? this.stack[++this.idx] : null; }
}
```
