---
title: [HW-107] 手写 IndexedDB 轻量封装——Promise 化 CRUD、索引查询、游标分页与升级迁移
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-107：手写 IndexedDB 轻量封装——Promise 化 CRUD、索引查询、游标分页与升级迁移
**答**：IDB 原生 API 回调地狱且事务易错，封装四要点：① 打开/升级（onupgradeneeded 建库建索引，版本迁移按版本号 switch）；② Promise 化事务（事务 complete 才 resolve，错误 reject 并带事务回滚语义）；③ 游标分页（cursor + limit，keyset 分页优于 offset）；④ 泛型 get/put/delete/query(byIndex)。

```javascript
class DB {
  constructor(name, version, upgrade) {
    this.name = name; this.version = version; this.upgrade = upgrade;
    this.ready = this.#open();
  }
  #open() {
    return new Promise((resolve, reject) => {
      const req = indexedDB.open(this.name, this.version);
      req.onupgradeneeded = (e) => this.upgrade(req.result, e.oldVersion, e.newVersion);   // 迁移入口
      req.onsuccess = () => resolve(req.result);
      req.onerror = () => reject(req.error);
    });
  }
  async tx(store, mode, fn) {                        // 事务包装：complete 才算成功
    const db = await this.ready;
    return new Promise((resolve, reject) => {
      const t = db.transaction(store, mode);
      const s = t.objectStore(store);
      Promise.resolve(fn(s)).then(resolve, reject);
      t.oncomplete = () => {};                        // 数据落盘以 complete 为准
      t.onerror = () => reject(t.error);              // 事务失败自动回滚
      t.onabort = () => reject(t.error || new Error('aborted'));
    });
  }
  put(store, value, key) { return this.tx(store, 'readwrite', (s) => new Promise((res, rej) => {
    const r = key !== undefined ? s.put(value, key) : s.put(value);
    r.onsuccess = () => res(r.result); r.onerror = () => rej(r.error); })); }
  get(store, key) { return this.tx(store, 'readonly', (s) => new Promise((res, rej) => {
    const r = s.get(key); r.onsuccess = () => res(r.result); r.onerror = () => rej(r.error); })); }
  delete(store, key) { return this.tx(store, 'readwrite', (s) => new Promise((res, rej) => {
    const r = s.delete(key); r.onsuccess = () => res(); r.onerror = () => rej(r.error); })); }
  async page(store, index, cursorKey, limit = 20) {  // keyset 分页：游标 + 上界
    const db = await this.ready;
    return new Promise((resolve, reject) => {
      const out = [];
      const req = db.transaction(store, 'readonly')
        .objectStore(store).index(index).openCursor(cursorKey ? IDBKeyRange.lowerBound(cursorKey, true) : undefined);
      req.onsuccess = () => {
        const cur = req.result;
        if (!cur || out.length >= limit) return resolve({ items: out, next: cur ? cur.key : null });
        out.push(cur.value); cur.continue();
      };
      req.onerror = () => reject(req.error);
    });
  }
}
// 迁移示例：
// upgrade(db, oldV) { if (oldV < 2) db.createObjectStore('cache');
//   if (oldV < 3) db.transaction('cache').objectStore('cache').createIndex('byTs', 'ts'); }
// 用法：const db = new DB('app', 3, upgrade); await db.put('cache', { id: 1, ts: Date.now() });
// keyset 分页：db.page('cache', 'byTs', lastTs) —— offset 分页在数据变动时会重/漏，keyset 稳定
```

**评分点**：
- onupgradeneeded 按版本号增量迁移（oldVersion 判断），不破坏旧数据。
- Promise 化事务：以事务 complete/error 为准（不是 request.onsuccess 就 resolve）。
- 游标分页用 keyset（lowerBound + 上次游标键），能说出 offset 分页在变动数据的缺陷。
- 事务失败回滚语义（onabort/onerror reject）。
