---
title: [ZSM-540] 笔试：手写 IM 未读数的多端已读游标同步
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-540：手写 IM 未读数的多端已读游标同步
**答**：实现 `createUnreadTracker()`：1) 消息带单调递增 `seq`；本端 `markRead(seq)` 更新本端游标（只进不退）；2) 收到其他端同步的游标（`syncRemote(deviceId, seq)`）时，未读数取**所有端游标最小值**的差值口径：`unread = maxSeq - min(allReadSeqs, maxSeq)`；3) `addMessage(seq)` 收新消息推进 maxSeq 并累计未读；4) 多端游标上报去抖（500ms 合并）；5) 游标持久化接口可注入。附用例验证「小游标端拖后腿」与去抖合并。

```javascript
function createUnreadTracker({ storage, debounceMs = 500 } = {}) {
  const readSeqs = new Map()   // deviceId -> 已读游标（本端 device0 默认 0）
  let maxSeq = 0
  let minSeq = 0
  let pendingReport = null

  function unread() {
    return Math.max(0, maxSeq - Math.min(minSeq, maxSeq))
  }

  function emit() { storage?.save({ readSeqs: [...readSeqs], maxSeq }) }

  function recomputeMin() {
    minSeq = readSeqs.size ? Math.min(...readSeqs.values()) : 0
  }

  function addMessage(seq) {
    if (seq <= maxSeq) return            // 乱序/重复消息忽略
    maxSeq = seq
    recomputeMin()
    emit()
  }

  function markRead(seq) {
    readSeqs.set('self', Math.max(readSeqs.get('self') ?? 0, seq))  // 只进不退
    recomputeMin()
    scheduleReport()
    emit()
  }

  function syncRemote(deviceId, seq) {
    const prev = readSeqs.get(deviceId) ?? 0
    if (seq <= prev) return              // 过期同步包丢弃
    readSeqs.set(deviceId, seq)
    recomputeMin()
    emit()
  }

  // 上报去抖：500ms 窗口只发最后一次
  function scheduleReport() {
    clearTimeout(pendingReport)
    pendingReport = setTimeout(() => {
      api.reportRead(readSeqs.get('self') ?? 0)
    }, debounceMs)
  }

  // 恢复持久化
  function hydrate(saved) {
    saved?.readSeqs?.forEach(([d, s]) => readSeqs.set(d, s))
    maxSeq = saved?.maxSeq ?? 0
    recomputeMin()
  }

  return { addMessage, markRead, syncRemote, hydrate, unread }
}

// 用例
const t = createUnreadTracker()
t.addMessage(1); t.addMessage(2); t.addMessage(3)
console.log(t.unread())        // 3
t.markRead(2)                  // 本端读到 2
console.log(t.unread())        // 1
t.syncRemote('pad', 1)         // 平板只读到 1
console.log(t.unread())        // 2：取各端最小游标 1 → 3-1=2
t.syncRemote('pad', 0)         // 过期包丢弃
console.log(t.unread())        // 2
t.syncRemote('pad', 3)
console.log(t.unread())        // 0：两端都到 3
```
**评分点**：
- 多端取最小游标的未读口径（任何端没读都算未读）
- 游标只进不退 + 过期同步包丢弃（乱序防御）
- 上报去抖合并（500ms 窗口）
- maxSeq 与 minSeq 分离维护，unread 派生计算（O(1)）
