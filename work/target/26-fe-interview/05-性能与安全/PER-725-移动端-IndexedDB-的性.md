---
title: [PER-725] 移动端 IndexedDB 的性能特性：什么时候 IDB 会卡主线程？大批量读写的正确姿势
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-725：移动端 IndexedDB 的性能特性：什么时候 IDB 会卡主线程？大批量读写的正确姿势

**答**：
- IDB 通常是异步不卡主线程，但三类例外：**大数据 blob 写入的序列化开销**（结构化克隆在主线程做）、**游标全量遍历**（在主线程逐条回调）、**事务排队堆积**（未关闭的事务阻塞其他库操作）。
- 正确姿势：大批量写入合并到一个事务（事务创建有开销，逐条开事务是反模式）；游标遍历改为按 key 范围 getAll（一次取批量）；大 blob 考虑 OPFS（Origin Private File System）或分片。
- 移动端特性：iOS Safari 的 IDB 在后台会被冻结（事务挂起），恢复时可能报错——后台期间避免开事务；配额（用户同意后可达 GB 级）但低端机磁盘慢，写入要批量。
- 度量：事务耗时分布、单事务条数、主线程被阻塞的 clone 时间（Performance 面板看 structuredClone）。

```javascript

const idbPerf = {
  mainThreadTraps: ['大 blob 结构化克隆', '游标逐条遍历回调', '事务排队堆积'],
  dos: { batch: '大批量合并进一个事务（逐条开事务是反模式）',
    cursor: '游标 -> key 范围 getAll 批量取',
    blob: '大 blob 分片或改用 OPFS' },
  mobile: { ios: '后台冻结事务，后台期避免开事务', quota: '同意后 GB 级，低端磁盘慢需批量写' },
};
async function bulkWrite(db, store, records) {
  return new Promise((resolve, reject) => {
    const tx = db.transaction(store, 'readwrite');              // 单事务批量
    const os = tx.objectStore(store);
    for (const r of records) os.put(r);                         // 一次 clone 批量
    tx.oncomplete = resolve;
    tx.onerror = () => reject(tx.error);
  });
}
// 反模式：records.forEach(r => db.transaction(...).objectStore(store).put(r))  // N 个事务
```
