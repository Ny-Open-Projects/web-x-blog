---
title: [ZSM-055] 笔试：手写 useHydrateAtoms（SSR 初始值注入，只生效一次）
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-055：手写 useHydrateAtoms（SSR 初始值注入，只生效一次）

**题目要求**：
- 实现 `useHydrateAtoms(entries, store?)`：传入 `[[atom, value]]` 数组，在组件首次渲染时把初值写入 store。
- 语义：**只在挂载时生效一次**，后续父组件重渲染传新值不覆盖（这是与 setState 的关键区别）。
- 必须在渲染期同步写入（不能 setTimeout），保证 SSR/CSR 首帧一致。

```javascript
import { useSyncExternalStore, useRef } from 'react'

export function useHydrateAtoms(entries, store = defaultStore) {
  const hydrated = useRef(false)
  if (!hydrated.current) {          // 渲染期判断：SSR 和客户端首渲染各执行一次
    hydrated.current = true
    for (const [atom, value] of entries) {
      if (store.get(atom) === undefined) store.set(atom, value) // 不覆盖已有值
    }
  }
  // 注意：不能用 useEffect —— SSR 时不执行，会丢失首帧初值
  return null
}

// 用法
function Profile({ initialName }) {
  useHydrateAtoms([[nameAtom, initialName]])
  const name = useAtomValue(nameAtom)
  return <h1>{name}</h1>
}
```

**评分点**：
- 在渲染期（非 effect）写入，保证服务端渲染拿到初值。
- 用 ref 保证只注入一次，父组件重渲染不会覆盖用户已修改的值。
- 不覆盖 store 中已有值（get 有值则跳过），多层级 hydrate 不互相踩。
- 能说出为什么不能用 useEffect：SSR 无 effect，客户端首帧会闪默认值。
