---
title: [ZSM-424] 笔试：手写状态快照与 diff 补丁引擎（可逆 patch）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-424：手写状态快照与 diff 补丁引擎
**答**：实现快照/补丁引擎：1) `snapshot(state)` 生成不可变快照（structuredClone）；2) `diff(a, b)` 生成 patch 数组：`{op:'set'|'del', path, value?}`，path 为 `a.b.0.c` 形式（数组下标）；3) `apply(state, patches)` 按序应用生成新状态（不可变更新：只复制变更路径节点）；4) `invert(patches, before)` 生成逆补丁（撤销用）；5) 引用相等的子树跳过（性能）。

```javascript
export function diff(a, b, path = '', out = []) {
  if (Object.is(a, b)) return out
  if (a === null || b === null || typeof a !== 'object' || typeof b !== 'object'
      || Array.isArray(a) !== Array.isArray(b))
    return (out.push({ op: 'set', path, value: b }), out)
  const keys = new Set([...Object.keys(a), ...Object.keys(b)])
  for (const k of keys) {
    const p = path ? `${path}.${k}` : k
    if (!(k in b)) out.push({ op: 'del', path: p })
    else if (!(k in a)) out.push({ op: 'set', path: p, value: b[k] })
    else diff(a[k], b[k], p, out)
  }
  return out
}

export function apply(state, patches) {
  const root = structuredClone(state)
  for (const { op, path, value } of patches) {
    const segs = path.split('.')
    const last = segs.pop()
    let cur = root
    for (const s of segs) cur = cur[s]
    op === 'set' ? (cur[last] = value) : delete cur[last]
  }
  return root
}

export function invert(patches, before) {
  return [...patches].reverse().map(({ op, path, value }) => {
    if (op === 'set') {
      const old = getPath(before, path)
      return old === undefined ? { op: 'del', path } : { op: 'set', path, value: old }
    }
    return { op: 'set', path, value: getPath(before, path) }   // del 的逆是 set 旧值
  })
}
const getPath = (o, p) => p.split('.').reduce((c, s) => c?.[s], o)
```
**评分点**：
- diff 覆盖三类变化（set/del/类型变更），路径拼接正确（空路径首层）
- apply 不可变更新语义（clone 后应用，不污染原状态——严格版应路径级 COW，可作加分讨论）
- invert 依赖 before 快照（set 逆 = 旧值；del 逆 = set 旧值；新增 set 的逆 = del）
- 引用相等短路（性能关键）；数组下标路径的平局（splice 语义局限）可作为追问点
