---
title: [OPT-141] 大对象 localStorage 同步读写阻塞主线程，替代方案怎么做？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-141：大对象 localStorage 同步读写阻塞主线程，替代方案怎么做？

**答**：
- localStorage 是同步 API：5MB 大对象序列化 + 写盘在主线程一次跑完，低端机可感知卡顿（尤其连续保存草稿场景）。
- 首选替代 IndexedDB：异步、容量大、结构化存储（可存 Blob），配合 idb 库或原生 promise 包装。
- 迁移策略：小数据（< 64KB、低频）仍可用 localStorage；大的走 IndexedDB；需要跨 tab 同步的加 BroadcastChannel 通知。
- 进一步优化：写入去抖 + 分片存储（按 key 前缀拆记录），避免"改一个字段重写 5MB"。

```javascript
// 一一对应：IndexedDB 异步存储封装（替代 localStorage 的大对象读写）
const DB_NAME = 'app-store';
function openDB() {
  return new Promise((resolve, reject) => {
    const req = indexedDB.open(DB_NAME, 1);
    req.onupgradeneeded = () => req.result.createObjectStore('kv');
    req.onsuccess = () => resolve(req.result);
    req.onerror = () => reject(req.error);
  });
}
let dbp = openDB();

export async function idbSet(key, value) {   // 异步：不阻塞主线程
  const db = await dbp;
  return new Promise((resolve, reject) => {
    const tx = db.transaction('kv', 'readwrite');
    tx.objectStore('kv').put(value, key);    // 结构化存储，无需 JSON.stringify
    tx.oncomplete = resolve; tx.onerror = () => reject(tx.error);
  });
}
export async function idbGet(key) {
  const db = await dbp;
  return new Promise((resolve, reject) => {
    const req = db.transaction('kv').objectStore('kv').get(key);
    req.onsuccess = () => resolve(req.result); req.onerror = () => reject(req.error);
  });
}

// 草稿保存场景：去抖 + 分 key，避免高频全量写
let draftTimer;
function saveDraft(docId, doc) {
  clearTimeout(draftTimer);
  draftTimer = setTimeout(() => idbSet(`draft:${docId}`, doc), 800);
}

// 跨 tab 同步（localStorage 原生有 storage 事件，IDB 没有）
const bc = new BroadcastChannel('draft-sync');
bc.onmessage = e => renderDraft(e.data);
```
