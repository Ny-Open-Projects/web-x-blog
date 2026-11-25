---
title: [ZSM-730] 离线状态第二轮：IndexedDB 同步架构与存储配额治理
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-730：离线状态第二轮：IndexedDB 同步架构与存储配额治理

**答**：
- 离线架构的完整分层：**业务层**（store 乐观生效）→ **队列层**（op 持久化 IndexedDB，ZSM-588）→ **存储层**（IndexedDB 事务 + 版本 schema）→ **同步层**（联网 flush + 冲突处理）。第二轮补充两个实战面：存储配额与多实体事务编排。
- 配额治理：`navigator.storage.estimate()` 查询用量/配额（Chrome 一般给磁盘的一定比例）；策略：1) 用量 > 80% 时收缩（删最旧缓存、压缩 op 日志）；2) `persisted` 权限申请（`navigator.storage.persist()`——重要数据不被浏览器自动清理）；3) 超配额写入失败的降级（op 内存队列 + 提示用户空间不足）。
- 多实体事务：一次业务操作涉及多张 objectStore（订单 + 库存 + 日志）——IndexedDB 支持跨 store 事务，`db.transaction(['orders', 'logs'], 'readwrite')` 全成功或全回滚；Web 端「本地事务原子性」就靠它，别用两个独立事务拼。
- 结构升级：objectStore 的 schema 变更走 `onupgradeneeded`（按 version 迁移），与 persist buster（ZSM-638）同一思想——IndexedDB 版本号自增 + 迁移函数链。
- 追问钩子：IndexedDB 的坑清单——Safari 私密模式不可用（降级内存 Map）、事务中不能 await 普通 Promise（会话提前提交）、大 blob 存储性能、主线程阻塞（大数据用 worker 读写）。

```javascript
// IndexedDB 封装：跨 store 事务 + 配额治理 + 版本迁移
const DB_NAME = 'app-state'
const DB_VERSION = 3

function openDB() {
  return new Promise((resolve, reject) => {
    const req = indexedDB.open(DB_NAME, DB_VERSION)
    req.onupgradeneeded = (e) => {
      const db = e.target.result
      const oldV = e.oldVersion
      if (oldV < 1) {
        db.createObjectStore('ops', { keyPath: 'opId' })
        db.createObjectStore('snapshots', { keyPath: 'key' })
      }
      if (oldV < 2) db.createObjectStore('meta', { keyPath: 'k' })       // v2: 加元数据表
      if (oldV < 3) {
        // v3: ops 表加 index（按实体查询压缩）
        const ops = req.transaction.objectStore('ops')
        ops.createIndex('byEntity', 'entity')
      }
    }
    req.onsuccess = () => resolve(req.result)
    req.onerror = () => reject(req.error)
  })
}

// 跨 store 原子事务
async function commitOperation(db, op, snapshotPatch) {
  return new Promise((resolve, reject) => {
    const tx = db.transaction(['ops', 'snapshots'], 'readwrite')
    tx.objectStore('ops').put(op)
    tx.objectStore('snapshots').put(snapshotPatch)
    tx.oncomplete = () => resolve()
    tx.onerror = () => reject(tx.error)    // 全回滚：op 与快照要么都成功
  })
}

// 配额治理
async function checkQuota(db) {
  const { usage, quota } = await navigator.storage.estimate()
  if (usage / quota > 0.8) {
    // 收缩：删最旧缓存 + 压缩已完成 op
    await compact(db)
    if (usage / quota > 0.9) toast.warn('存储空间不足，部分离线数据可能丢失')
  }
  await navigator.storage.persist()        // 申请持久化：防浏览器自动清理
}
```
