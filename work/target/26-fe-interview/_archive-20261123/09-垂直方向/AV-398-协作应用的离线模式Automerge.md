---
title: [AV-398] 协作应用的离线模式（Automerge/Yjs + IndexedDB）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-398：协作应用的离线模式（Automerge/Yjs + IndexedDB）

**答**：
- 持久化：每次 update 追加 IndexedDB（防丢），启动时重放恢复。
- 冲突：离线多端编辑天然并发——CRDT 合并，语义层校验合并结果。
- 同步指示：UI 显示"离线，N 条未同步"，恢复后自动 flush。

```javascript
// 离线持久化
async function offlinePersist(doc) {
  const updates = [];
  doc.on('update', u => updates.push(u));
  setInterval(async () => {                            // 批量落盘
    if (!updates.length) return;
    await idbAppend('offline-ops', updates.splice(0));
  }, 5000);
}
async function restoreFromLocal() {
  const saved = await idbAll('offline-ops');
  const doc = new Y.Doc();
  for (const batch of saved) for (const u of batch) Y.applyUpdate(doc, u);
  return doc;
}
```
