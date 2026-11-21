---
title: [H5-193] 设计一个离线笔记应用（IndexedDB + 同步冲突）
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-193：设计一个离线笔记应用（IndexedDB + 同步冲突）
**答**：
- 离线三板斧：数据本地化（IndexedDB）+ 资源本地化（Service Worker 缓存 App Shell）+ 同步策略。
- 本地优先：一切写操作先落 IDB（带 `updated_at` + `dirty` 标记），UI 即时反馈；防抖批量上送。
- 同步协议：push 本地 dirty 记录、pull 服务端变更；冲突解决三选一——**字段级合并**（标题/正文分开比）、**副本保留**（冲突版本存成两条让用户手动合并，最安全）、**CRDT**（Yjs/Automerge 字符级自动合并，协作的正解）。
- 关键字段：`base_updated_at` 记录"本地基于哪个服务端版本修改"，用于检测真冲突（服务端已前进而本地也改了）。

```javascript
// 离线笔记：IndexedDB 存储 + 同步冲突处理（以 idb 库风格演示）
async function openDB() {
  const req = indexedDB.open('notes', 1);
  req.onupgradeneeded = () => {
    const store = req.result.createObjectStore('notes', { keyPath: 'id' });
    store.createIndex('dirty', 'dirty');       // 上送队列索引
  };
  return req;
}
const dbp = openDB();

// 1) 本地优先：写操作先落 IDB（updated_at + dirty 标记），UI 即时反馈
async function saveNote(note) {
  const db = await dbp;
  const tx = db.transaction('notes', 'readwrite');
  tx.objectStore('notes').put({
    ...note, updated_at: Date.now(), dirty: true,
    base_updated_at: note.base_updated_at ?? 0,   // 本地基于的服务端版本
  });
  scheduleSync();                                 // 防抖批量上送
}

// 2) 同步：push dirty + pull 远端，冲突用 base_updated_at 检测
async function sync() {
  const db = await dbp;
  const tx = db.transaction('notes', 'readwrite');
  const dirty = [];
  const req = tx.objectStore('notes').index('dirty').openCursor();
  req.onsuccess = async (e) => {
    const cur = e.target.result;
    if (!cur) return;
    dirty.push(cur.value);
    cur.continue();
  };
  for (const local of dirty) {
    const remote = await api.getNote(local.id).catch(() => null);
    let payload = local;
    // 真冲突：服务端在本地基线之后又被别人改过
    if (remote && remote.updated_at > local.base_updated_at &&
        remote.updated_at !== local.updated_at) {
      payload = resolveConflict(local, remote);
    }
    await api.putNote(payload);
    const wtx = (await dbp).transaction('notes', 'readwrite');
    wtx.objectStore('notes').put({
      ...payload, dirty: false, base_updated_at: Date.now(),
    });
  }
}

// 3) 冲突解决三选一（产品决策，面试要讲清取舍）：
function resolveConflict(local, remote) {
  // a. 字段级合并：标题/正文分开比（多数笔记产品这么做）
  if (local.title !== remote.title) return { ...remote, title: local.title };
  // b. 副本保留：冲突版本存成两条，用户手动合并 —— 最安全
  return { ...remote,
    duplicate: { ...local, id: crypto.randomUUID() } };
}
// c. CRDT（Yjs/Automerge）：字符级自动合并，冲突不再存在 —— 协作编辑的正解
const scheduleSync = (() => { let t; return () => { clearTimeout(t); t = setTimeout(sync, 2000); }; })();
// 4) Service Worker：App Shell + 静态资源 precache，API 失败回退缓存
// self.addEventListener('fetch', (e) => {
//   e.respondWith(fetch(e.request).catch(() => caches.match(e.request)));
// });
```
