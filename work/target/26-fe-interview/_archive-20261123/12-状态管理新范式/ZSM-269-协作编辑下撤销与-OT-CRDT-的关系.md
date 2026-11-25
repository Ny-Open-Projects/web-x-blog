---
title: [ZSM-269] 多人协作时撤销和 OT/CRDT 是什么关系
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-269：多人协作时撤销和 OT/CRDT 是什么关系

**答**:
- 单机撤销=简单栈；协作下你的 undo 会与其他人的并发 op 交叉，必须经过变换（OT transform 或 CRDT 天然支持）
- OT 方案：undo(op) 生成逆操作并 transform 过所有后来的并发 op；ProseMirror/Yjs 都有对应实现
- CRDT 方案：删除操作是「墓碑标记」而非物理删除，undo 本质是「重新插入被删的 tombstone」，天然无冲突
- 产品语义：协作撤销只撤销「自己的操作」（undo 不该吃掉别人的修改），实现上按作者过滤 op 历史——这是面试常被追问的点

```javascript
// Yjs：undoManager 天然只撤自己
const ydoc = new Y.Doc()
const ytext = ydoc.getText('doc')
const um = new Y.UndoManager(ytext, { trackedOrigins: new Set([localOrigin]) })  // 只跟踪本地 origin
um.undo()   // 协作安全：并发远端 op 自动保留
```
