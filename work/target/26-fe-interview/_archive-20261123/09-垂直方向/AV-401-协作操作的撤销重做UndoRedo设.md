---
title: [AV-401] 协作操作的撤销/重做（Undo/Redo）设计
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-401：协作操作的撤销/重做（Undo/Redo）设计

**答**：
- CRDT 环境的 undo 不是简单回滚：撤销自己的操作（不影响他人改动）——记录操作逆映射。
- 实现：本地 undo 栈存"自己的操作"，undo = 应用逆向 update（Yjs UndoManager 内置）。
- 边界：他人并发编辑后的 undo 结果可能"部分失效"——语义提示。

```javascript
// Yjs UndoManager
import * as Y from 'yjs';
function setupUndo(doc, userId) {
  const undoManager = new Y.UndoManager(doc.getMap('shapes'), {
    trackedOrigins: new Set([userId]),                 // 只撤销自己
    captureTimeout: 500,                               // 500ms 合并为一步
  });
  return {
    undo: () => undoManager.undo(),
    redo: () => undoManager.redo(),
    canUndo: () => undoManager.undoStack.length > 0,
  };
}
```
