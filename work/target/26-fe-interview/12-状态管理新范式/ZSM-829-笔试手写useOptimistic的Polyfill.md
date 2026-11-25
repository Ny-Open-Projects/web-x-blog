---
title: [ZSM-829] 笔试：手写 useOptimistic 的 Polyfill（React 18 兼容实现）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-829：手写 useOptimistic 的 Polyfill（React 18 兼容实现）
**答**：React 18 项目要用 useOptimistic——实现 polyfill：1) `useOptimisticImpl(state, setState, reducer)` 返回 `[displayValue, addOptimistic]`；2) 乐观值只在该次 transition 渲染期间生效：`addOptimistic(payload)` 先算乐观值并强制本次渲染使用；transition 完成后自动丢弃乐观值回滚真实 state；3) 并发乐观合并（多次 addOptimistic 按 reducer 叠加）；4) 附用例：乐观显示 → 完成回滚 → 失败回滚。

```javascript
import { useState, useRef, useCallback } from 'react'

function useOptimisticImpl(state, setState, reducer) {
  const optimisticRef = useRef(null)     // 当前乐观链（pending payloads）
  const [, force] = useState(0)          // 强制重渲

  // 渲染期间计算显示值：真实 state + 未完成乐观叠加
  const display = optimisticRef.current
    ? optimisticRef.current.reduce((acc, p) => reducer(acc, p), state)
    : state

  const addOptimistic = useCallback((payload) => {
    optimisticRef.current ??= []
    optimisticRef.current.push(payload)   // 并发乐观叠加
    force((n) => n + 1)                   // 触发乐观渲染
  }, [reducer])

  // transition 完成后回滚：由调用方（startTransition 包装层）触发
  const commitOrRollback = useCallback(() => {
    optimisticRef.current = null          // 丢弃乐观链：显示值回到真实 state
    force((n) => n + 1)
  }, [])

  return [display, addOptimistic, commitOrRollback]
}

// 包装：自动管理 transition 生命周期
function useOptimisticAction(state, setState, reducer) {
  const [display, addOptimistic, settle] = useOptimisticImpl(state, setState, reducer)

  function runAction(actionFn) {
    return new Promise((resolve) => {
      // React 18：手动模拟 transition 的乐观生命周期
      import('react').then(({ startTransition }) => {
        startTransition(async () => {
          try {
            await actionFn({ addOptimistic, setState })
          } finally {
            settle()                       // 完成/失败统一回滚乐观值
          }
          resolve()
        })
      })
    })
  }

  return { display, runAction }
}

// 用例
function Demo() {
  const [likes, setLikes] = useState(10)
  const { display, runAction } = useOptimisticAction(likes, setLikes, (cur, d) => cur + d)

  function like() {
    runAction(async ({ addOptimistic, setState }) => {
      addOptimistic(1)                     // UI 立即 11（乐观）
      const res = await api.like()         // 真实请求
      if (res.ok) setState(res.likes)      // 转正 42
      // 失败：不 setState → settle 回滚到 10
    })
  }
  // display === likes && 乐观链叠加
  return <button>{display}</button>
}
```
**评分点**：
- 乐观链叠加（pending 数组 + reducer 折叠，并发乐观合并）
- settle 统一回滚（完成/失败 finally 丢弃乐观链）
- 转正语义（action 内 setState 覆盖真实值）
- 渲染期计算（display = state + 乐观折叠，不污染真实 state）
