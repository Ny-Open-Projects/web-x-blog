---
title: [ZSM-002] Zustand 的 selector 如何实现细粒度订阅？浅比较和严格相等有什么区别？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-002：Zustand 的 selector 如何实现细粒度订阅？浅比较和严格相等有什么区别？
**答**：
- `useStore(store, selector)`：每次 store 变化都会执行 selector，把返回值与上次做比较（默认 `Object.is` 严格相等），相等就不触发重渲染。
- 所以 selector 返回**新引用**（如 `s => s.items.filter(...)`、`s => ({ a: s.a, b: s.b })`）时，哪怕内容没变，每次都会重渲染。
- 解法：用 `useShallow`（或旧版 shallow 参数）做浅比较，只比较第一层 key/value；深层嵌套仍需 selector 本身返回稳定引用。
- 最佳实践：把「一个大 selector 返回对象」拆成多个小 selector，每个订阅一个原子切片，多数场景不需要 useShallow。
- 追问钩子：这是 selector 模式的核心，也是「Zustand 隐形 bug」高频来源。

```javascript
import { create } from 'zustand'
import { useShallow } from 'zustand/react/shallow'

const useUser = create(set => ({
  first: 'Li', last: 'Lei', age: 18,
}))

// 差：age 任何变化……不，这里返回新对象，first/last 引用每次都新 → 每次都重渲染
const bad = useUser(s => ({ first: s.first, last: s.last }))

// 好：浅比较，age 变化时 first/last 没变 → 不重渲染
const good = useUser(useShallow(s => ({ first: s.first, last: s.last })))

// 更好：拆成两个 selector，各自独立比较，无需 shallow
const first = useUser(s => s.first)
const last = useUser(s => s.last)
```
