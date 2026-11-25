---
title: [ZSM-588] 离线优先的状态队列：IndexedDB 暂存、重放与冲突标记
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-588：离线优先的状态队列：IndexedDB 暂存、重放与冲突标记

**答**：
- 离线优先三层：**本地写**（操作立即写 IndexedDB + 状态乐观生效）、**队列**（待同步 op 持久化到 IndexedDB，浏览器崩溃也不丢）、**重放**（联网后按序发给服务端，处理返回结果）。
- 队列设计要点：op 带本地 `opId + baseVersion`（操作基于哪个版本的数据）；重放时服务端校验 baseVersion——版本不符返回 409，客户端标记「冲突」：策略可选服务端胜（丢弃本地 op，回滚展示）或提示用户手动解决（文档编辑类）。
- 顺序与合并：同一实体的多个 op 重放要保序；可合并的 op 先压缩（连续「改标题」合并为最后一次），减少重放次数；不同实体的 op 可并行重放提高吞吐。
- 持久化细节：IndexedDB 写入是事务性的——「op 入队」和「本地状态生效」要放同一个事务里（或至少保证 op 先入队），防止「状态变了队列没存」的半完成态。
- 追问钩子：重放是「幂等友好」的——服务端用 opId 去重（重试可能重复发送），已处理的 opId 直接返回上次结果。

```javascript
// 离线队列核心
class OfflineQueue {
  constructor(db) { this.db = db }

  async enqueue(op) {
    // 事务：op 入队（持久化）成功后才算提交
    const tx = this.db.transaction('ops', 'readwrite')
    const store = tx.objectStore('ops')
    store.put({ ...op, opId: op.opId, baseVersion: op.baseVersion, status: 'pending' })
    await done(tx)
  }

  async flush() {
    const ops = (await getAll(this.db, 'ops')).filter((o) => o.status === 'pending')
    for (const op of ops) {
      try {
        const res = await api.replay(op)   // 服务端按 opId 幂等 + baseVersion 校验
        if (res.status === 409) {
          await markConflict(this.db, op, res.serverState)   // 冲突标记
          continue
        }
        await markDone(this.db, op.opId, res.data)
      } catch (e) {
        break    // 网络错误：停止 flush，剩余 op 保持 pending 下次重试
      }
    }
  }

  async compress() {
    // 同实体连续同类 op 合并（改标题取最后一次）
    const ops = await getAll(this.db, 'ops')
    const byEntity = new Map()
    for (const op of ops) {
      const key = `${op.entity}:${op.type}`
      byEntity.set(key, op)   // 后者覆盖前者
    }
    return [...byEntity.values()]
  }
}

// 冲突标记 UI 状态
// { conflictOps: [{ opId, entity, serverState, localOp }] }
// 用户选择「保留服务端」→ 回滚本地 + 删 op；「保留本地」→ 强制提交（服务端 force 合并）
```
