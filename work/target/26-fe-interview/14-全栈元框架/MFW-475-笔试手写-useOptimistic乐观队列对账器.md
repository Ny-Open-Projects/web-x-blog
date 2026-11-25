---
title: [MFW-475] 笔试：手写 useOptimistic 乐观队列对账器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-475：useOptimistic 乐观队列对账器
**答**：实现 `OptimisticLedger`：1) `optimistic(item)` 立即入视图，带临时 id 与 `pending: true`；2) `confirm(tempId, real)` 服务端真值到达：替换临时项并保持位置（不重排——位置抖动是差评来源）；3) `reject(tempId)` 失败移除并触发 `onError`；4) 服务端全量刷新到达时 `reconcile(serverList)`：以服务端为准，删掉不在其中的本地乐观项（孤儿清理），顺序完全采用服务端序。

```javascript
export class OptimisticLedger {
  constructor(onError) { this.items = []; this.onError = onError; this.seq = 0 }

  optimistic(item) {
    const tempId = `tmp-${++this.seq}`
    this.items.push({ ...item, id: tempId, pending: true, at: Date.now() })
    return tempId
  }

  confirm(tempId, real) {
    const i = this.items.findIndex(x => x.id === tempId)
    if (i === -1) return
    this.items[i] = { ...real, pending: false } // 原位替换，不重排
  }

  reject(tempId, err) {
    const i = this.items.findIndex(x => x.id === tempId)
    if (i !== -1) this.items.splice(i, 1)
    this.onError?.(err, tempId)
  }

  reconcile(serverList) {
    const optimisticOnly = this.items.filter(x => x.pending)
    const serverIds = new Set(serverList.map(x => x.id))
    // 服务端已有对应真值的乐观项丢弃；孤立的乐观项保留（服务端尚未落库）
    const orphans = optimisticOnly.filter(o => !o.serverKey || !serverIds.has(o.serverKey))
    this.items = [...serverList, ...orphans.map(({ pending, ...rest }) => ({ ...rest, pending }))]
  }
}
```

**评分点**：
- 原位替换不重排（confirm 后位置稳定，避免闪烁）
- reconcile 以服务端为权威序（本地序只是临时视图）
- 孤儿乐观项判定（serverKey 匹配后丢弃、无匹配保留——双写窗口语义）
- reject 触发 onError 回调（失败必须可达用户而非静默消失）
