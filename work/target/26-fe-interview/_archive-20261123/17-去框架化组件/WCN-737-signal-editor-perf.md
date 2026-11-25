---
title: [WCN-737] 富文本/画布编辑器里 Signals 高频更新如何优化性能？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-737：富文本/画布编辑器里 Signals 高频更新如何优化性能？

**答**：
- 结论：把「文档模型」与「视图状态」分离——高频的光标/拖拽坐标用独立 signal 且 rAF 节流，不进入历史栈；结构性变更（插入节点）才走事务与 undo。
- 对细粒度节点用 signal per node，只更新受影响节点；批量 DOM 写入用 batch 合并，避免中途布局抖动（layout thrashing）。
- 追问钩子：协同场景下每个字符都发 signal 更新会怎样？考察「操作变换（OT/CRDT）批处理 + 节流广播」。

```javascript
const cursor = signal({ x: 0, y: 0 });
const doc = signal({ nodes: [] });
let raf = 0;
function onPointerMove(x, y) {
  if (raf) return;
  raf = requestAnimationFrame(() => { cursor.value = { x, y }; raf = 0; }); // 节流
}
function insertNode(node) {
  batch(() => {
    doc.value = { nodes: [...doc.value.nodes, node] }; // 结构性变更走 batch
  });
}
console.log('高频坐标节流，结构变更批处理');
```
