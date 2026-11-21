---
title: [HW-209] 手写 Blob 引用计数存储——IDB 存大 Blob + 引用表（多记录共享同一 Blob，删除最后引用才清 Blob）
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-209：手写 Blob 引用计数存储——多记录共享同一 Blob，删除最后引用才释放

**答**：聊天场景多消息引用同一图片：Blob 存 refs 表（blobKey→{count}）+ blobs 表存数据，消息记录只存 blobKey 引用——删除消息只减 count，count=0 才删 Blob（重复图片只存一份，存储省 90%+）。count 递减与 Blob 删除在事务内（原子）；gcOrphans 定期对账修正计数漂移。

```javascript
async function putBlob(blobKey, blob) {
  const tx = db.transaction(['blobs', 'refs'], 'readwrite');
  const existing = await tx.objectStore('refs').get(blobKey);
  if (existing) {
    await tx.objectStore('refs').put({ blobKey, count: existing.count + 1 });   // 已存在：只加计数
  } else {
    await tx.objectStore('blobs').put({ blobKey, blob });                        // 首次：存 Blob
    await tx.objectStore('refs').put({ blobKey, count: 1 });
  }
  await txComplete(tx);                                   // refs 与 blobs 同事务（原子，PER-324）
}
async function releaseBlob(blobKey) {                     // 删除引用：count-1，0 才删 Blob
  const tx = db.transaction(['blobs', 'refs'], 'readwrite');
  const ref = await tx.objectStore('refs').get(blobKey);
  if (ref) {
    if (ref.count <= 1) {
      await tx.objectStore('refs').delete(blobKey);
      await tx.objectStore('blobs').delete(blobKey);      // 最后引用：Blob 释放（配额回收）
    } else {
      await tx.objectStore('refs').put({ blobKey, count: ref.count - 1 });
    }
  }
  await txComplete(tx);
}
async function gcOrphans() {                              // 孤儿清理：对账修正计数漂移
  const referenced = new Set(await allMessageBlobKeys()); // 扫全部消息的 blobKey 引用
  for (const { blobKey } of await db.getAll('refs'))
    if (!referenced.has(blobKey)) await releaseBlob(blobKey);   // 无引用却 count>0：释放
}
// 收益：100 条消息引用同一截图 → 1 份 Blob + count=100（vs 100 份全存 = 99% 节省）
// 原子性：refs 计数与 blobs 数据同事务——崩溃窗口不会出现"计数在 Blob 不在"的不一致
// gcOrphans 兜底：计数漂移（崩溃/漏 release）定期修正——引用计数系统的标准配套
// 读取：getBlob(blobKey) → blobs.get → createObjectURL（用后 revoke，PER-280）
```

**评分点**：
- 引用计数模型（refs count 表 + count=0 才删 Blob）——本题核心。
- 同事务原子性（计数与 Blob 生命周期一致，PER-324）。
- gcOrphans 对账兜底（计数漂移修复）。
- 场景收益量化（重复图片只存一份）与读取 revoke 配套。
