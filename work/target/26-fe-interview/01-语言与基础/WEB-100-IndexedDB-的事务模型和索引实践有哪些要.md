---
title: [WEB-100] IndexedDB 的事务模型和索引实践有哪些要点？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-100：IndexedDB 的事务模型和索引实践有哪些要点？
**答**：
- 一切读写都在事务里，事务有三种模式 readonly/readwrite/versionchange；事务生命周期到微任务队列清空即失效，回调里再异步操作会自动提交报错。
- 性能铁律：批量写合并进同一个事务（一次 fsync 级成本），逐条开事务会慢一个数量级。
- 只有 createIndex 建过索引的字段才能按非主键高效查询；复合索引解决"先按 A 再按 B 排序"的组合查询。
- 游标（cursor）遍历代替全量 getAll，大数据集下控制内存。

```javascript
const db = await new Promise((ok, err) => {
  const req = indexedDB.open('chat', 1);
  req.onupgradeneeded = () => {
    const d = req.result;
    const store = d.createObjectStore('messages', { keyPath: 'id' });
    store.createIndex('byRoom', 'roomId');                // 单字段索引
    store.createIndex('roomAndTime', ['roomId', 'time']); // 复合索引支持组合查询
  };
  req.onsuccess = () => ok(req.result);
  req.onerror = () => err(req.error);
});

// 要点一：批量写放同一事务
function saveMessages(list) {
  return new Promise((ok, err) => {
    const tx = db.transaction('messages', 'readwrite');
    const store = tx.objectStore('messages');
    list.forEach((m) => store.put(m));                    // 同一事务内多次 put
    tx.oncomplete = ok;
    tx.onerror = () => err(tx.error);                     // 任一失败整事务回滚
  });
}

// 要点二：用复合索引做范围查询，用游标控制内存
function pageByRoom(roomId, pageSize = 20) {
  return new Promise((ok) => {
    const out = [];
    const idx = db.transaction('messages').objectStore('messages')
      .index('roomAndTime');
    const range = IDBKeyRange.bound([roomId, 0], [roomId, Infinity]);
    idx.openCursor(range, 'prev').onsuccess = (e) => {    // 倒序取最新
      const cur = e.target.result;
      if (!cur || out.length >= pageSize) return ok(out);
      out.push(cur.value);
      cur.continue();
    };
  });
}
```
