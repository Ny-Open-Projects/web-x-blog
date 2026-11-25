---
title: [AV-387] Yjs 的核心概念：YDoc/YMap/YArray/Update
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-387：Yjs 的核心概念：YDoc/YMap/YArray/Update

**答**：
- YDoc：CRDT 根文档；YMap/YArray/YText 等结构化类型；本地修改产生 Update（二进制）广播。
- 同步：update 广播给 peers，合并自动收敛；离线时本地累积，恢复后同步 update 序列。
- 快照与历史：Y.encodeStateAsUpdate 全量快照、Y.snapshot 任意时点恢复。

```javascript
// Yjs 最小示例
import * as Y from 'yjs';
const doc = new Y.Doc();
const shapes = doc.getMap('shapes');
doc.on('update', (update, origin) => {
  if (origin !== 'remote') wsSend(update);          // 本地变更广播
});
function applyRemote(update) {
  Y.applyUpdate(doc, update, 'remote');
}
function snapshot() {
  return Y.encodeStateAsUpdate(doc);                 // 全量快照（新加入者）
}
shapes.set('rect1', { x: 10, y: 20, type: 'rect' });
```
