---
title: [ZSM-034] Zustand 的 useStore 返回值什么时候会导致组件重渲染？列全触发与不触发的情形
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-034：Zustand 的 useStore 返回值什么时候会导致组件重渲染？列全触发与不触发的情形
**答**：
- 触发：selector 返回值与上次 `Object.is` 不相等（新对象/新数组引用、变化后的原始值）。
- 不触发：值未变（原始值相等、对象引用未变）、set 了与 selector 无关的切片、返回函数/稳定引用。
- 特殊：set 空对象或相同引用 `setState(s => s)` 不触发任何订阅。
- 推论：整 store 订阅 `useStore()` 在任何字段变化时都渲染；「订阅所有但只渲染一个字段」是常见性能事故。

```javascript
const useStore = create(set => ({ a: 1, b: { c: 2 }, list: [] }))

// 场景对照
useStore(s => s.a)              // 只有 a 变才渲染
useStore(s => s.b)              // 只有 b 引用变化才渲染（内部 c 改动但引用没换不触发——不可变更新下等价于 b 变）
useStore(s => s.list.filter(x => x.on)) // 每次任何变更都渲染（新数组引用）→ 需 useShallow
useStore()                      // 任何字段变化都渲染
```
