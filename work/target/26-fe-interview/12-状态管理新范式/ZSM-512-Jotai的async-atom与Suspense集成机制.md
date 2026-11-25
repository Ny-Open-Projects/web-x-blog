---
title: [ZSM-512] Jotai 的异步 atom 是如何与 Suspense 集成的
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-512：Jotai 的异步 atom 是如何与 Suspense 集成的

**答**：
- 异步 atom 的 `read` 是 async 函数，Jotai 内部处理返回 promise：第一次读取时把 promise 存进 atomState，组件里 `useAtomValue` 抛出该 promise（throw），外层 `<Suspense>` fallback 兜住——这就是「抛 promise」的 Suspense 集成。
- promise 完成后 Jotai 把结果写入 atomState 并通知订阅，React 重试渲染，不再抛出。
- 依赖链上的异步会向上冒泡：派生 atom 里 `get(asyncAtom)` 拿到的是「等待中的原子」，其派生也会抛同一个 promise，Suspense 只需包住顶层。
- 非严格模式可关 Suspense 集成：`useAtomValue` 配合 `queryAtom`/手动 loading 状态，或 `atomWithQuery` 的 `suspense: false`，改为返回 `{ loading, data }` 形状。
- 追问钩子：write-only atom 的 set 里做异步不抛 promise（写侧不进 Suspense），刷新用 `refresh`（依赖失效）而非重新 set，避免 React 重挂载。

```javascript
import { atom, useAtomValue } from 'jotai'

// 异步 atom：读时抛 promise 给 Suspense
const userIdAtom = atom(1)
const userAtom = atom(async (get) => {
  const id = get(userIdAtom)
  const res = await fetch(`/api/users/${id}`)
  return res.json()
})
// 派生异步 atom：冒泡上游的 promise
const greetingAtom = atom(async (get) => `hi, ${get(userAtom).name}`)

function Profile() {
  const greeting = useAtomValue(greetingAtom) // 挂起期间向上抛 promise
  return <h1>{greeting}</h1>
}

function App() {
  return (
    <Suspense fallback={<Spinner />}>
      <Profile />
    </Suspense>
  )
}
// userIdAtom 变更 → userAtom 依赖版本失效 → 重新抛新 promise → Suspense 再挂起
```
