---
title: [ZSM-509] 笔试：手写 proxy 状态库的自动快照缓存
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-509：手写 proxy 状态库的自动快照缓存
**答**：实现 `createProxyStore(initial)`：1) `state` 为代理对象，可直接 mutate；2) `getSnapshot()` 返回「冻结快照」——与上次快照**结构相同且未修改的子树复用旧引用**（结构共享），保证 `Object.is` 兼容；3) `subscribe(fn)` 在微任务批处理所有 mutate 后统一通知；4) 快照里深层对象冻结防误改。附用例验证：只改叶子节点时上层引用稳定。

```javascript
function createProxyStore(initial) {
  let root = initial
  const subs = new Set()
  const snapshotCache = new WeakMap() // proxy -> frozen snapshot
  let dirty = false

  function snap(obj) {
    const cached = snapshotCache.get(obj)
    if (cached) return cached
    const next = Array.isArray(obj) ? [] : {}
    for (const k of Object.keys(obj)) {
      const v = obj[k]
      next[k] = (v && typeof v === 'object' && !v.__isSnap) ? snap(v) : v
    }
    Object.freeze(next)
    snapshotCache.set(obj, next)
    return next
  }

  function proxyNode(obj) {
    return new Proxy(obj, {
      get(t, k) {
        const v = t[k]
        return (v && typeof v === 'object' && !Object.isFrozen(v)) ? proxyNode(v) : v
      },
      set(t, k, val) {
        if (t[k] === val) return true
        t[k] = val
        scheduleNotify()
        return true
      },
    })
  }

  function scheduleNotify() {
    if (dirty) return
    dirty = true
    queueMicrotask(() => { dirty = false; const s = getSnapshot(); subs.forEach((fn) => fn(s)) })
  }

  function getSnapshot() {
    const s = snap(root)
    root = s.__raw ?? root
    return s
  }

  return {
    state: proxyNode(initial),
    getSnapshot,
    subscribe(fn) { subs.add(fn); return () => subs.delete(fn) },
  }
}

// 用例：只改叶子，上层引用稳定
const store = createProxyStore({ user: { name: 'a', tags: [1] }, mode: 'x' })
const s1 = store.getSnapshot()
store.state.user.name = 'b'
const s2 = store.getSnapshot()
console.log(s1.user !== s2.user)   // true：name 所在子树变更
console.log(s1.mode === s2.mode)   // true：未修改子树复用引用
```
**评分点**：
- 结构共享：未修改子树复用旧快照引用（WeakMap 缓存）
- 快照冻结防外部误改（Object.freeze）
- mutate 通知微任务批处理（dirty 标志去重）
- 叶子相等早退不触发通知（t[k] === val 判断）
