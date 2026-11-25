---
title: [H5-361] IndexedDB 深水：事务、索引与游标的实战要点
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 存储]
type: 面试题
---

## H5-361：IndexedDB 深水：事务、索引与游标的实战要点

**答**：
- 事务模型是核心：所有读写必须在事务里，事务随回调链结束自动提交——在事务回调外做 await 异步操作会导致事务失效（InvalidStateError），IDB 操作要串在一条 promise 链里不插外部异步
- 索引设计：按查询路径建 index（如 by_status + [status, created] 复合索引），游标 openCursor 范围扫描代替全表遍历；索引也是存储成本，别滥建
- 游标分页：IDBCursor.advance 跳过已读、keyset 分页（lastKey 继续）比 offset 更高效；count 用 index.count 快速拿总数
- 版本升级：onupgradeneeded 里做 schema 迁移（建表/建索引），要考虑旧版本数据迁移耗时（大库升级会卡启动，放后台线程）
- 封装建议：promise 化 + 事务粒度收敛 + 批量操作合并事务；读多写少场景用 IDB + 内存缓存双层

```javascript
function pageByStatus(db, status, lastKey, limit = 20) {
  return new Promise((resolve, reject) => {
    const tx = db.transaction('tasks', 'readonly');
    const idx = tx.objectStore('tasks').index('by_status');
    const range = lastKey
      ? IDBKeyRange.bound([status, lastKey], [status, Infinity], true, false)
      : IDBKeyRange.bound([status, ''], [status, Infinity]);
    const out = [];
    idx.openCursor(range).onsuccess = (e) => {
      const cur = e.target.result;
      if (!cur || out.length >= limit) return resolve(out);
      out.push(cur.value); cur.continue();
    };
    tx.onerror = () => reject(tx.error);
  }); // 注意: 全程无外部 await, 事务不中断
}
```
