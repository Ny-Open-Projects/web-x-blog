---
title: [JS-117] 如何实现 promise 化的 IndexedDB 简易封装？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-117：如何实现 promise 化的 IndexedDB 简易封装？

**答**：
- IndexedDB 全程事件回调风格，封装思路：request 包 Promise，事务包函数。
- open 三件套：`onupgradeneeded` 建库建索引、`onsuccess` 拿 db、`onerror` 拿错误。
- 事务生命周期：事务在创建时就要声明读写模式，且离开事件循环后无法再挂请求。
- 所有异步操作统一走 `requestToPromise`，业务代码即可全部 async/await。

```javascript
function openDB(name, version, upgrade) {
  return new Promise((resolve, reject) => {
    const req = indexedDB.open(name, version);
    req.onupgradeneeded = (e) => upgrade(req.result, e); // 仅版本变化时触发
    req.onsuccess = () => resolve(req.result);
    req.onerror = () => reject(req.error);
  });
}

const toPromise = (req) => new Promise((resolve, reject) => {
  req.onsuccess = () => resolve(req.result);
  req.onerror = () => reject(req.error);
});

class IDBStore {
  constructor(db, storeName) { this.db = db; this.name = storeName; }

  _tx(mode, fn) {
    const tx = this.db.transaction(this.name, mode);
    return fn(tx.objectStore(this.name));
  }

  put(value, key)  { return toPromise(this._tx('readwrite', (s) => s.put(value, key))); }
  get(key)         { return toPromise(this._tx('readonly',  (s) => s.get(key))); }
  delete(key)      { return toPromise(this._tx('readwrite', (s) => s.delete(key))); }
  getAll()         { return toPromise(this._tx('readonly',  (s) => s.getAll())); }
}

(async () => {
  const db = await openDB('demo', 1, (db) => {
    if (!db.objectStoreNames.contains('kv')) db.createObjectStore('kv'); // 主键即 key
  });
  const users = new IDBStore(db, 'kv');
  await users.put({ name: 'tom', vip: true }, 'u-1');
  console.log(await users.get('u-1'));    // { name: 'tom', vip: true }
  console.log(await users.getAll());
  await users.delete('u-1');
})();
```
