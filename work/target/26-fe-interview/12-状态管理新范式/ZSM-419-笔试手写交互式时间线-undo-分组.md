---
title: [ZSM-419] 笔试：手写按操作语义分组的撤销栈（拖拽/输入/删除各成组）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-419：手写按操作语义分组的撤销栈
**答**：实现 `createGroupedHistory()`：1) `begin(kind)` 开始一个操作组（如 'drag'/'input'/'delete'），组内 push 合并为一步；2) `push(patch)` 记入当前组；3) `end()` 结束组（未 end 的组自动在 begin 新组或 undo 时隐式结束）；4) `undo()/redo()` 按组粒度恢复（组内多次 patch 一次撤销）；5) 组记录 patch 列表，undo 时逆序应用逆 patch；6) 支持「原子组」（组内失败整体丢弃）。

```javascript
export function createGroupedHistory() {
  let groups = [], future = [], cur = null

  function begin(kind, { atomic = false } = {}) {
    cur = { kind, patches: [], atomic }
  }
  function push(patch) {
    if (!cur) cur = { kind: 'misc', patches: [], atomic: false }   // 隐式组
    cur.patches.push(patch)
  }
  function end() {
    if (!cur || !cur.patches.length) { cur = null; return }
    groups = [...groups.slice(-49), cur]         // 上限 50 组
    future = []                                  // 新组分叉清 redo
    cur = null
  }
  function undo(state, applyPatch) {
    if (cur) end()                               // 未结束组隐式结束
    const g = groups.pop()
    if (!g) return state
    future.push(g)
    let s = state
    for (const p of [...g.patches].reverse()) s = applyPatch(s, invert(p))   // 逆序逆放
    return s
  }
  function redo(state, applyPatch) {
    const g = future.pop()
    if (!g) return state
    groups.push(g)
    let s = state
    for (const p of g.patches) s = applyPatch(s, p)
    return s
  }
  return { begin, push, end, undo, redo,
    get canUndo() { return groups.length > 0 || !!cur },
    get canRedo() { return future.length > 0 } }
}
// invert(patch)：由 patch 类型生成逆操作（如 {op:'set',key,v} → 旧值）
```
**评分点**：
- 组粒度撤销（拖拽 N 帧一次撤销）——begin/end 显式 + 隐式兜底
- undo 逆序应用逆 patch（顺序敏感操作正确还原）
- 新组清 redo（分叉语义）；50 组上限 FIFO
- atomic 组的失败丢弃语义（attempt 失败不留垃圾组）
