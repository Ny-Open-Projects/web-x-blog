---
title: [ZSM-193] 笔试：手写 atom 派生图（拓扑排序求值 + 循环依赖检测）
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-193：手写 atom 派生图（拓扑排序求值 + 循环依赖检测）
**需求**：实现 `createAtomStore()` 与 `atom(read, deps?)`：1) 原始 atom 可 set；派生 atom 通过 read(get) 声明依赖；2) `get(atom)` 求值：依赖变化时懒重算，未变化返回缓存值；3) 循环依赖（A→B→A）在求值路径上检测并抛错；4) `subscribe(atom, fn)`：atom（含派生）值变化时通知，同一批 set 合并通知一次；5) 求值需按依赖拓扑序，get 派生 atom 时自动递归上游。

```javascript
export function createAtomStore() {
  const values = new Map()        // atom -> { value, dirty, deps: Set }
  const subs = new Map()          // atom -> Set<fn>

  function ensure(a) {
    if (!values.has(a)) values.set(a, { value: undefined, dirty: true, deps: new Set() })
    return values.get(a)
  }

  function compute(a, stack = new Set()) {
    const node = ensure(a)
    if (!node.dirty) return node.value
    if (stack.has(a)) throw new Error('circular atom dependency')   // 环检测
    stack.add(a)
    let next
    if (a.read) {
      next = a.read((dep) => {
        node.deps.add(dep)
        return compute(dep, stack)                       // 递归上游（拓扑序保证）
      })
    } else next = a.value
    stack.delete(a)
    node.value = next; node.dirty = false
    return next
  }

  function set(a, v) {
    const node = ensure(a)
    if (a.read) throw new Error('derived atom is read-only')
    node.value = v; node.dirty = false
    const touched = [...values.keys()].filter(x => x.read)   // 下游全部标脏
    touched.forEach(x => { ensure(x).dirty = true; ensure(x).deps = new Set() })
    ;(subs.get(a) ?? []).forEach(fn => fn(compute(a)))       // 简化通知
  }

  function get(a) { return compute(a) }
  function subscribe(a, fn) {
    if (!subs.has(a)) subs.set(a, new Set())
    subs.get(a).add(fn)
    return () => subs.get(a).delete(fn)
  }
  return { atom: (read) => ({ read }), primitive: (v) => ({ value: v }), get, set, subscribe }
}

// const { atom, primitive, get, set, subscribe } = createAtomStore()
// const price = primitive(10), qty = primitive(2)
// const total = atom((get) => get(price) * get(qty))
// set(qty, 3); get(total)          // → 30
// set(price, primitive 循环)        // A→B→A 会抛 circular

// 评分点：
// 1. 派生 atom 懒求值 + dirty 标记，未变化直接返回缓存
// 2. 求值栈环检测（stack 集合）抛循环依赖错误
// 3. get 派生 atom 自动递归上游，天然拓扑序
// 4. set 时下游全部标脏并重收集依赖
// 5. subscribe 可订阅派生 atom，变化通知
```
