---
title: [HW-335] 手写一个 IndexedDB ORM 引擎：模型映射与索引查询
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-335：手写一个 IndexedDB ORM 引擎：模型映射与索引查询

**答**：
- 需求：实现 MiniORM：define(name, {schema, indexes}) 建 store（含索引）；insert/update/remove/get；where(index, op, value) 索引查询（IDBCursor 遍历，支持 gt/lt/in）；all() 与 count()；事务封装（批量操作单事务）。
- 边界：schema 版本升级（onupgradeneeded 建/重建索引）；查询游标分页（limit）；批量插入单事务原子（任一失败全回滚）。
- 评分点：版本升级；游标分页；事务原子性。

```javascript
class MiniORM {
  constructor(dbName, version = 1) { this.dbName = dbName; this.version = version; this.models = new Map(); }
  define(name, { schema, indexes = [] }) { this.models.set(name, { schema, indexes }); return this; }
  async open() {
    return new Promise((res, rej) => {
      const req = indexedDB.open(this.dbName, this.version);
      req.onupgradeneeded = e => {                           // 版本升级建索引
        const db = e.target.result;
        for (const [name, m] of this.models) {
          const store = db.objectStoreNames.contains(name)
            ? e.target.transaction.objectStore(name)
            : db.createObjectStore(name, { keyPath: m.schema.key ?? 'id' });
          m.indexes.forEach(ix => { if (!store.indexNames.contains(ix)) store.createIndex(ix, ix); });
        }
      };
      req.onsuccess = () => res(req.result);
      req.onerror = () => rej(req.error);
    });
  }
  async tx(name, mode, fn) {                                 // 事务封装
    const db = await this.open();
    return new Promise((res, rej) => {
      const t = db.transaction(name, mode);
      const store = t.objectStore(name);
      const out = fn(store);
      t.oncomplete = () => res(out.__result);
      t.onerror = () => rej(t.error);                        // 原子回滚
    });
  }
  async insert(name, items) {                                // 批量单事务
    return this.tx(name, 'readwrite', store => {
      items.forEach(it => store.add(it));
    });
  }
  async where(name, index, op, value, { limit = 100 } = {}) {
    const db = await this.open();
    return new Promise((res, rej) => {
      const out = [];
      const req = db.transaction(name).objectStore(name).index(index).openCursor();
      req.onsuccess = e => {
        const c = e.target.result;
        if (!c || out.length >= limit) return res(out);
        const v = c.value[index];
        if (op === 'gt' && v > value || op === 'lt' && v < value
          || op === 'eq' && v === value || op === 'in' && value.includes(v))
          out.push(c.value);
        c.continue();                                        // 游标分页
      };
      req.onerror = () => rej(req.error);
    });
  }
}
```
