---
title: [ZSM-042] Jotai 的异步 atom 怎么写？loading/error 状态怎么处理？怎么手动刷新？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-042：Jotai 的异步 atom 怎么写？loading/error 状态怎么处理？怎么手动刷新？
**答**：
- 异步 atom：read 函数返回 Promise（或用 async/await），`useAtomValue` 会自动 suspense——组件要么被 <Suspense> 包住，要么用 `loadable(atom)` 拿 loading/error/data 三态。
- 错误处理：Promise reject 时读取会抛出，用 ErrorBoundary 兜底；或者用 loadable/异步 atom 返回 `{ state, data, error }` 结构自己管理。
- 手动刷新：给异步 atom 传一个「刷新计数」依赖 atom，refresh 就是给计数 +1，read 函数里 `await get(refreshAtom)` 触发重新求值。
- 注意：原生异步 atom 无缓存策略（staleTime 等概念），频繁挂载会重复请求；这是选 TanStack Query 而非 Jotai 装服务端数据的关键理由。

```javascript
const refreshAtom = atom(0)
const userAtom = atom(async get => {
  await get(refreshAtom) // 依赖刷新计数
  return fetchUser()
})
const refreshUser = () => useSetAtom 之外：写法如下
// const setRefresh = useSetAtom(refreshAtom); setRefresh(c => c + 1)

function Profile() {
  const user = useAtomValue(userAtom) // 触发 Suspense
  return <Suspense fallback={<Spin/>}><Avatar user={user}/></Suspense>
}
// 或者不用 Suspense：
const st = useAtomValue(loadable(userAtom)) // st.state: 'loading' | 'hasData' | 'hasError'
```
