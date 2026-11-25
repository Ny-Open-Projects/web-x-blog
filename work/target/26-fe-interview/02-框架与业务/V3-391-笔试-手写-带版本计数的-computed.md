---
title: [V3-391] 笔试：手写带版本计数的 computed（脏检查 + 缓存）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-391：笔试：手写带版本计数的 computed（脏检查 + 缓存）
**答**：实现 `computedEff(fn)`：返回带 `.value` 的对象；依赖变化后首次读取才重算（惰性），依赖未变化（值相同）时返回缓存，且链式依赖（computed 依赖 computed）避免级联重复计算。用 version counting 实现。

```javascript
let globalVersion = 0
function reactive(value) {
  return { get value() { track(r); return r }, set value(nv) { if (Object.is(nv, r)) return; r = nv; dep.version = ++globalVersion; notify(r) } }
  let r = value; const dep = { version: 0, subs: new Set() }
  function track(d) { if (activeEffect) d.subs.add(activeEffect) }
  function notify() { dep.subs.forEach(e => e()) }
}
function computedEff(fn) {
  const self = { version: 0 }
  let cached, hasCache = false
  const effect = () => { hasCache = false; self.version = globalVersion } // 失效：丢弃缓存
  const read = () => {
    if (hasCache && self.version === globalVersion) return cached // 版本一致，缓存有效
    activeEffect = effect
    cached = fn(); hasCache = true
    activeEffect = null
    self.version = globalVersion
    return cached
  }
  return { get value() { return read() } }
}
// a 变化触发 effect 置 version，c.value 首次读重算；b 恰好不变时后续读取直接命中缓存
```
**评分点**：
- 惰性求值：trigger 只标记版本，不立即重算。
- 缓存命中条件「hasCache && version 一致」。
- activeEffect 切换正确（读取期间收集依赖）。
- 能说清版本计数相对布尔 dirty 的优势（值未变可短路下游）。
