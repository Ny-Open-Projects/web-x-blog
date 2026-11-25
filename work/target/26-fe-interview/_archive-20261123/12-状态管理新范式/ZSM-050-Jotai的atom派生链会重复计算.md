---
title: [ZSM-050] Jotai 派生 atom 会重复计算吗？缓存策略和 weakMap-based memo 怎么写？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-050：Jotai 派生 atom 会重复计算吗？缓存策略和 weakMap-based memo 怎么写？
**答**：
- 同步派生 atom：依赖不变时不会重算（依赖图缓存）；但依赖对象每 set 都换引用，昂贵派生会被连带重算。
- Jotai 提供 `selectAtom(atom, fn, equalityFn)` 做切片+比较缓存；`atomWithDefault` 惰性初值；自定义缓存用 WeakMap 以「输入对象」为 key 存结果。
- WeakMap 方案：输入对象被 GC 时缓存自动释放，避免 Map 泄漏；适合按请求/按对象维度的派生。
- 极端昂贵计算（解析大文档）应放进异步派生或 worker，不要阻塞渲染主线程。

```javascript
import { selectAtom } from 'jotai/utils'

const docsAtom = atom([]) // 每次 set 新数组
// 只订阅 docs 中 opened 的那篇，引用不变不重算
const openDocAtom = selectAtom(docsAtom, docs => docs.find(d => d.opened))

// 自定义 WeakMap 缓存：同输入复用昂贵结果
const cache = new WeakMap()
const parseAtom = atom(get => {
  const doc = get(openDocAtom)
  if (!doc) return null
  if (!cache.has(doc)) cache.set(doc, expensiveParse(doc)) // doc 释放则缓存释放
  return cache.get(doc)
})
```
