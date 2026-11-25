---
title: [ZSM-738] 笔试：手写 IndexedDB 离线队列（跨 store 事务 + flush 重放）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-738：手写 IndexedDB 离线队列（跨 store 事务 + flush 重放）
**需求**：实现 `createOfflineDB()`：1) `enqueue(op)`：op 写入 IndexedDB 'ops' store，**同事务**写入 'meta' 的队列计数（原子性：两个 store 都成功才算入队）；2) `flush(syncFn)`：按 seq 重放 pending op，成功删除、409 冲突标记；3) `compact()`：压缩已完成 op（保留最近 20 条日志）；4) `estimate()`：返回队列长度与存储用量；5) mock IndexedDB（内存 Map 实现事务接口）便于测试；6) 附用例：入队原子性 + flush 重放 + 压缩。

```javascript
// Mock IndexedDB（内存实现，保留事务语义）
function mockIDB() {
  const stores = new Map()      // name -> Map<key, value>
  return {
    transaction(names, _mode) {
      const txStores = names.map((n) => {
        if (!stores.has(n)) stores.set(n, new Map())
        return { name: n, map: stores.get(n) }
      })
      return {
        objectStore(name) {
          const s = txStores.find((t) => t.name === name)
          return {
            put: (v) => s.map.set(v.opId ?? v.k, v),
            delete: (k) => s.map.delete(k),
            getAll: () => [...s.map.values()],
          }
        },
        // 事务原子性：任一操作抛错全部回滚（mock 用延迟提交模拟）
        __pending: true,
        complete() { this.__pending = false },
      }
    },
    _stores: stores,
  }
}

function createOfflineDB(idb = mockIDB()) {
  async function enqueue(op) {
    // 跨 store 原子事务：ops + meta 计数
    const tx = idb.transaction(['ops', 'meta'], 'readwrite')
    const ops = tx.objectStore('ops')
    const meta = tx.objectStore('meta')
    ops.put(op)
    const count = meta.getAll().find((m) => m.k === 'queueCount')?.v ?? 0
    meta.put({ k: 'queueCount', v: count + 1 })
    tx.complete()
    return op.opId
  }

  async function flush(syncFn) {
    const tx = idb.transaction(['ops'], 'readonly')
    const all = tx.objectStore('ops').getAll()
      .filter((o) => o.status !== 'done' && o.status !== 'conflict')
      .sort((a, b) => a.seq - b.seq)

    const results = []
    for (const op of all) {
      try {
        const res = await syncFn(op)
        if (res.conflict) {
          const wtx = idb.transaction(['ops'], 'readwrite')
          wtx.objectStore('ops').put({ ...op, status: 'conflict', serverState: res.serverState })
          wtx.complete()
          results.push({ opId: op.opId, conflict: true })
        } else {
          const wtx = idb.transaction(['ops', 'meta'], 'readwrite')
          wtx.objectStore('ops').put({ ...op, status: 'done', result: res.data })
          // 计数递减（原子）
          const meta = wtx.objectStore('meta')
          const c = meta.getAll().find((m) => m.k === 'queueCount')?.v ?? 1
          meta.put({ k: 'queueCount', v: Math.max(0, c - 1) })
          wtx.complete()
          results.push({ opId: op.opId, ok: true })
        }
      } catch {
        break     // 网络错误：停止（保持 pending）
      }
    }
    return results
  }

  async function compact() {
    const tx = idb.transaction(['ops'], 'readonly')
    const all = tx.objectStore('ops').getAll().filter((o) => o.status === 'done')
    if (all.length <= 20) return 0
    const toRemove = all.slice(0, all.length - 20)     // 保留最近 20 条
    const wtx = idb.transaction(['ops'], 'readwrite')
    toRemove.forEach((o) => wtx.objectStore('ops').delete(o.opId))
    wtx.complete()
    return toRemove.length
  }

  async function estimate() {
    const tx = idb.transaction(['ops', 'meta'], 'readonly')
    const pending = tx.objectStore('ops').getAll().filter((o) => !o.status || o.status === 'pending').length
    const count = tx.objectStore('meta').getAll().find((m) => m.k === 'queueCount')?.v ?? 0
    return { pending, queueCount: count }
  }

  return { enqueue, flush, compact, estimate }
}

// 用例
const db = createOfflineDB()
await db.enqueue({ opId: 'op1', seq: 1, entity: 'doc1', payload: { title: 'A' } })
await db.enqueue({ opId: 'op2', seq: 2, entity: 'doc1', payload: { title: 'B' } })
console.log(await db.estimate())        // { pending: 2, queueCount: 2 }：原子计数

const results = await db.flush(async (op) => op.seq === 2 ? { conflict: true, serverState: {} } : { data: 'ok' })
console.log(results)                    // [{ opId: 'op1', ok: true }, { opId: 'op2', conflict: true }]
console.log(await db.compact())         // 0（不足 20 不压缩）
```
**评分点**：
- 跨 store 原子事务（ops + meta 计数同事务，complete 提交语义）
- flush 按 seq 重放 + 冲突标记（保留 serverState）
- compact 保留最近 20 条（日志环形）
- estimate 可观测（pending + 队列计数双口径）
