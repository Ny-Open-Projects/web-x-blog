---
title: [ZSM-506] 笔试：手写支持动态依赖的派生 atom 引擎
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-506：手写支持动态依赖的派生 atom 引擎
**答**：实现 `createDerivedAtom(read)`（read 为 `(get, set) => value`）：1) `get(atom)` 时**按实际调用**收集依赖（条件分支不读的不算依赖）；2) 上游 set 后只失效受影响的派生（沿依赖边传播），未挂载订阅前惰性求值；3) `subscribe(atom, fn)` 支持派生 atom 订阅；4) 同一轮更新内重复读不重算（缓存版本号）。附一个条件分支派生的用例验证动态依赖。

```javascript
function createStore() {
  const values = new Map()     // atom -> { v, ver }
  const deps = new Map()       // atom -> Set<atom>（本轮读取收集）
  const subs = new Map()       // atom -> Set<fn>
  const verOf = (a) => values.get(a)?.ver ?? 0

  function ensure(a) {
    if (!values.has(a)) values.set(a, { v: a.init, ver: 0, derived: !a.read })
    const s = values.get(a)
    if (!s.derived) return s
    // 依赖版本没变就命中缓存
    const last = deps.get(a)
    if (last && [...last].every((d) => s.usedVer.get(d) === verOf(d))) return s
    // 重算：动态收集依赖
    const used = new Map()
    const get = (d) => { used.set(d, verOf(ensure(d))); return values.get(d).v }
    s.v = a.read(get)
    s.usedVer = used
    deps.set(a, new Set(used.keys()))
    return s
  }

  function set(a, value) {
    const s = ensure(a)
    s.v = typeof value === 'function' ? value(s.v) : value
    s.ver++
    propagate(a)
  }

  function propagate(a, seen = new Set()) {
    if (seen.has(a)) return
    seen.add(a)
    deps.forEach((ds, child) => {
      if (ds.has(a)) { values.get(child).ver++; propagate(child, seen) }
    })
    subs.get(a)?.forEach((fn) => fn(values.get(a).v))
  }

  return {
    get: (a) => ensure(a).v,
    set,
    subscribe(a, fn) {
      (subs.get(a) ??= new Set()).add(fn)
      return () => subs.get(a)?.delete(fn)
    },
  }
}

// 验证动态依赖
const store = createStore()
const mode = { init: 'a' }
const a = { init: 1 }, b = { init: 2 }
const pick = { read: (get) => get(mode) === 'a' ? get(a) : get(b) }
store.get(pick)                    // 1，依赖只有 mode+a
store.set(b, 99)
console.log(store.get(pick))       // 仍为 1：b 不在依赖图内，未触发重算
```
**评分点**：
- 依赖按实际 get 调用收集（条件分支不读不计入）
- 版本号缓存命中（同一轮重复读不重算）
- 失效沿依赖图向下游传播且防环（seen 集合）
- 订阅触发与失效解耦（失效先行，通知按订阅粒度）
