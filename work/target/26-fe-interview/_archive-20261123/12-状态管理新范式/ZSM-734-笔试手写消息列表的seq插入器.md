---
title: [ZSM-734] 笔试：手写消息列表的 seq 插入器（二分插入 + 缺口检测 + 撤回挂起）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-734：手写消息列表的 seq 插入器（二分插入 + 缺口检测 + 撤回挂起）
**需求**：实现 `createMessageList()`：1) `append(msg)`：按服务端 seq 升序二分插入，重复 seq 去重；2) 缺口检测：插入位置与前一条 seq 跳差 > 1 时触发 `onGap(from, to)`（上层补拉）；3) `recall(seq)`：目标已存在直接标记，未到则挂起队列，append 后自动 drain；4) `insertGapFill(list)`：补拉结果批量插入（同样二分 + 去重 + drain）；5) 附用例：乱序插入、缺口回调、撤回挂起释放。

```javascript
function createMessageList({ onGap } = {}) {
  const messages = []            // seq 升序
  const recallQueue = new Set()
  const listeners = new Set()

  function lowerBound(seq) {
    let lo = 0, hi = messages.length
    while (lo < hi) {
      const mid = (lo + hi) >> 1
      if (messages[mid].seq < seq) lo = mid + 1
      else hi = mid
    }
    return lo
  }

  function insertOne(m) {
    const i = lowerBound(m.seq)
    if (messages[i]?.seq === m.seq) return false          // 重复去重
    messages.splice(i, 0, { ...m, recalled: false })
    // 缺口检测
    const prev = messages[i - 1]
    if (prev && m.seq - prev.seq > 1) onGap?.(prev.seq, m.seq)
    return true
  }

  function append(m) {
    const inserted = insertOne(m)
    if (inserted) drainRecalls()
    return inserted
  }

  function insertGapFill(list) {
    let added = 0
    list.forEach((m) => { if (insertOne(m)) added++ })
    drainRecalls()
    return added
  }

  function drainRecalls() {
    for (const seq of [...recallQueue]) {
      const m = messages.find((x) => x.seq === seq)
      if (m) { m.recalled = true; recallQueue.delete(seq) }
    }
  }

  function recall(seq) {
    const m = messages.find((x) => x.seq === seq)
    if (m) m.recalled = true
    else recallQueue.add(seq)                              // 挂起：等目标到达
    listeners.forEach((fn) => fn(view()))
  }

  function view() {
    return messages.map(({ seq, content, recalled }) => ({ seq, content, recalled }))
  }

  return { append, insertGapFill, recall, view, subscribe: (fn) => (listeners.add(fn), () => listeners.delete(fn)) }
}

// 用例
let gaps = []
const list = createMessageList({ onGap: (a, b) => gaps.push([a, b]) })

list.append({ seq: 1, content: 'hello' })
list.append({ seq: 3, content: 'world' })     // 缺口：1→3
console.log(gaps)                              // [[1, 3]]

list.append({ seq: 3, content: 'world' })     // 重复：去重
console.log(list.view().length)                // 2

list.recall(2)                                 // seq2 未到：挂起
console.log(list.view().find((m) => m.seq === 2)?.recalled ?? 'not-yet')

list.insertGapFill([{ seq: 2, content: 'gap' }])   // 补拉插入
console.log(list.view())                       // seq 1,2(recalled),3：撤回指令释放
console.log([...list.view().filter((m) => m.seq === 2)][0].recalled)   // true
```
**评分点**：
- 二分插入保持 seq 升序 + 重复去重
- 缺口检测触发 onGap（补拉协议钩子）
- 撤回挂起队列与 drain（指令到达早于目标消息的时序防御）
- insertGapFill 批量补齐同样走去重与 drain
