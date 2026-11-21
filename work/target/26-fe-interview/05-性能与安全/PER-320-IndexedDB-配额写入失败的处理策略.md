---
title: [PER-320] IndexedDB 写满（QuotaExceededError）怎么办？分层降级策略怎么设计？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-320：IndexedDB 写满（QuotaExceededError）怎么办？分层降级策略怎么设计？

**答**：
- 错误识别：IDB 事务报 `QuotaExceededError`（或 EventTarget 的 error event，name 因浏览器差异叫 QuotaExceededError/DOMException）——必须在事务 error 回调里接住并降级，不能让 Promise 链裸抛。
- 降级阶梯：① 清理——按 LRU 删最老的记录/最旧的 objectStore 分区（如离线包按版本淘汰）；② 压缩——大 Blob 压缩存储、文本去格式化；③ 申请持久化——`navigator.storage.persist()`（避免被整源淘汰，但不增加配额）；④ 缩域——把非关键数据降到 localStorage 小字段或内存缓存；⑤ 用户交互——磁盘真满时引导用户清理/降画质。
- 预防设计：写入前预估用量（记录自账）、给缓存类 objectStore 设 TTL 与容量上限、大文件（视频/离线包）单独分库便于整体淘汰。
- 验收：构造写入直到 QuotaExceeded，验证降级链按序触发且业务不崩、核心数据（用户草稿）有保护标记不被清理。

```javascript
async function safePut(db, store, key, value, { protect = false } = {}) {
  try {
    await put(db, store, key, value);
  } catch (e) {
    if (e.name !== 'QuotaExceededError' && e.name !== 'DOMException') throw e;
    // 降级阶梯
    await evictLRU(db, { skipProtected: protect });          // 1. 清非保护 LRU
    try { await put(db, store, key, value); return 'ok-after-evict'; } catch {}
    const compressed = await compress(value);                 // 2. 压缩
    try { await put(db, store, key, compressed); return 'ok-compressed'; } catch {}
    try { await navigator.storage.persist(); await put(db, store, key, value); return 'ok-persisted'; } catch {}
    return 'failed';                                          // 3. 走内存/localStorage 兜底由调用方决定
  }
}
// evictLRU：遍历 store 里带 lastAccess 的记录，按访问时间升序删，跳过 protect 标记
```
