---
title: [ZSM-520] Zustand 的 selector 每次返回新引用时的四种解法对比
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-520：Zustand 的 selector 每次返回新引用时的四种解法对比

**答**：
- 问题根源：selector 返回字面量对象/数组时，store 里任何字段变化都会重新执行 selector，产出新引用，`useSyncExternalStore` 用 `Object.is` 比对判定「变了」，触发本可避免的重渲（或死循环级别的渲染风暴）。
- 解法一 `useShallow(selector)`：浅比较新旧对象/数组的键值，推荐默认解法，覆盖绝大多数「解构多字段」场景。
- 解法二 selector 内记忆化：缓存上次输入输出，依赖没变返回旧引用，适合返回深层结构的派生（列表过滤+排序）。
- 解法三 selector 粒度拆分：一个 selector 拆成 N 个标量 selector，分别订阅——比浅比较更省（未变的字段根本不触发比对）。
- 解法四 custom equalityFn：`useStore(store, selector, shallow)` 第三参自定义比较函数，适合特殊语义（如忽略字段顺序、忽略时间戳）。
- 选型口径：优先拆分（性能最优）；结构性派生用 useShallow；深层派生用 memo+shallow 双保险。

```javascript
import { useShallow } from 'zustand/react/shallow'
import { useStore } from 'zustand'
import { useMemo } from 'react'

// 解法一：useShallow（对象返回）
const { name, count } = useUserStore(useShallow((s) => ({ name: s.name, count: s.count })))

// 解法二：selector 内记忆化（深层派生）
const useFilteredTodos = () => {
  const filter = useUserStore((s) => s.filter)
  const todos = useUserStore((s) => s.todos)
  return useMemo(() => todos.filter((t) => t.status === filter),
    [todos, filter])   // 输入引用没变就不产新数组
}

// 解法三：拆分（标量订阅）
const name = useUserStore((s) => s.name)
const count = useUserStore((s) => s.count)

// 解法四：自定义比较
const items = useStore(useUserStoreApi, (s) => s.items, (a, b) =>
  a.length === b.length && a.every((v, i) => v.id === b[i].id))
```
