---
title: [WEB-160] 如何设计一个 IndexedDB 的 Promise 化封装库？版本迁移怎么做？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-160：如何设计一个 IndexedDB 的 Promise 化封装库？版本迁移怎么做？
**答**：
- 核心：把 onsuccess/onerror 包成 Promise，事务粒度封装 get/put/delete/getAll；连接做单例缓存。
- 版本迁移：open(name, version) 的 onupgradeneeded 里按 oldVersion 逐级执行迁移函数，旧迁移逻辑永不删除。
- 迁移只做"结构变更"（建表/建索引/搬数据），业务数据变更尽量放应用层代码。
- 细节：事务在 await 之后可能已关闭，所有请求必须在事务创建的同步栈里发起；版本变更被其他标签页阻塞时给 onblocked 提示。

```javascript
// 极简 IDB 封装：Promise 化 + 迁移注册表
const MIGRATIONS = {
  1: (db) => db.createObjectStore('notes', { keyPath: 'id' }),
  2: (db, tx) => tx.objectStore('notes').createIndex('byUpdated', 'updatedAt'), // 版本 2 补索引
};
function openDB(name, version) {
  return new Promise((resolve, reject) => {
    const req = indexedDB.open(name, version);
    req.onupgradeneeded = (e) => {
      for (let v = e.oldVersion + 1; v <= version; v++) MIGRATIONS[v]?.(req.result, req.transaction); // 逐版本推进
    };
    req.onsuccess = () => resolve(req.result);
    req.onblocked = () => console.warn('请关闭其他标签页以完成升级');
    req.onerror = () => reject(req.error);
  });
}
async function put(db, store, value) {
  return new Promise((resolve, reject) => {
    const tx = db.transaction(store, 'readwrite');   // 事务内同步发起请求
    tx.objectStore(store).put(value);
    tx.oncomplete = resolve;
    tx.onerror = () => reject(tx.error);
  });
}
```
