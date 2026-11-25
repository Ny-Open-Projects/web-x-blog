---
title: [PER-726] 手写一个 IDB 批量写入器：单事务合并、分片限流（防大事务超时）与失败重试
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-726：手写一个 IDB 批量写入器：单事务合并、分片限流（防大事务超时）与失败重试

**答**：
- 平衡点：事务太大（几万条）会长时间占库且超时风险高——按 500 条分片，每片一个事务，片间让出主线程（await nextTick）；失败分片记录断点续写。
- 要点：分片间 await requestAnimationFrame/setTimeout(0) 让 UI 喘息；断点续写（记录已完成游标 key，重试从断点开始）；写入进度上报（大导入场景 UI 需要进度条）。
- 边界：分片大小按设备档调整（低端 200）；写入过程页面隐藏（iOS 冻结事务）要暂停并在恢复后继续。
- 评分点：断点续写与后台暂停。

```javascript

class BulkIdbWriter {
  constructor(db, store, { chunk = 500 } = {}) {
    this.db = db; this.store = store; this.chunk = window.__deviceTier === 'low' ? 200 : chunk;
  }
  async writeAll(records, { onProgress } = {}) {
    let cursor = 0;
    const resumeKey = localStorage.getItem(`idb-cursor:${this.store}`);   // 断点
    if (resumeKey) cursor = records.findIndex(r => r.key >= resumeKey);
    while (cursor < records.length) {
      if (document.hidden) await waitVisible();                 // iOS 后台冻结保护
      const slice = records.slice(cursor, cursor + this.chunk);
      const startKey = slice[0].key;
      try {
        await this.writeChunk(slice);
        cursor += slice.length;
        localStorage.setItem(`idb-cursor:${this.store}`, String(slice.at(-1).key));
        onProgress?.(cursor / records.length);
        await new Promise(r => (window.requestIdleCallback ?? setTimeout)(r)); // 让出主线程
      } catch (e) {
        await sleep(500);                                       // 失败重试当前分片（断点不前移）
      }
    }
    localStorage.removeItem(`idb-cursor:${this.store}`);
  }
  writeChunk(slice) {
    return new Promise((resolve, reject) => {
      const tx = this.db.transaction(this.store, 'readwrite');  // 单事务一批
      const os = tx.objectStore(this.store);
      slice.forEach(r => os.put(r));
      tx.oncomplete = resolve;
      tx.onerror = () => reject(tx.error);
      tx.onabort = () => reject(tx.error);
    });
  }
}
function waitVisible() {
  return new Promise(r => {
    if (!document.hidden) return r();
    document.addEventListener('visibilitychange', () => !document.hidden && r(), { once: true });
  });
}
```
