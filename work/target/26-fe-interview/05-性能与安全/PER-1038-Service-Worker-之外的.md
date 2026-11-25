---
title: [PER-1038] Service Worker 之外的离线方案：IndexedDB 缓存与同步协议
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1038：Service Worker 之外的离线方案：IndexedDB 缓存与同步协议

**答**：
- IndexedDB 适合结构化离线数据（草稿/列表缓存）；容量远超 localStorage（可达数百 MB）。
- 同步协议：离线队列记录操作日志（op-based），恢复连接后按序重放；冲突用 LWW 或版本向量处理。
- 关键设计：请求幂等键、队列持久化（SW 存储兜底）、失败进死信队列人工介入。
- 场景：表单草稿、审批待办、移动巡检——弱网刚需。

```javascript
// 离线同步队列
const DB = 'ops'; let db;
function open() { return new Promise(res => {
  const r = indexedDB.open(DB, 1);
  r.onupgradeneeded = () => r.result.createObjectStore('q', { keyPath: 'id' });
  r.onsuccess = () => res(db = r.result);
}); }
async function enqueue(op) {                    // op: { id, type, payload }
  const tx = db.transaction('q', 'readwrite');
  tx.objectStore('q').add({ ...op, ts: Date.now() });
}
async function flush() {
  const tx = db.transaction('q', 'readonly');
  const req = tx.objectStore('q').getAll();
  req.onsuccess = async () => {
    for (const op of req.result) {
      const r = await fetch('/sync', { method: 'POST',
        body: JSON.stringify(op) }).catch(() => null);
      if (r?.ok) {
        const dtx = db.transaction('q', 'readwrite');
        dtx.objectStore('q').delete(op.id);     // 成功才出队
      } // 失败留在队列，下次重试
    }
  };
}
addEventListener('online', flush);
```
