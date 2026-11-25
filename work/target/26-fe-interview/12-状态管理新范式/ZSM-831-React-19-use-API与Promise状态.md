---
title: [ZSM-831] React 19 的 use(Promise)：Promise 直读对状态库意味着什么
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-831：React 19 的 use(Promise)：Promise 直读对状态库意味着什么

**答**：
- `use(promise)` 在组件里直接消费 Promise（挂起/恢复由 Suspense 语义接管）——数据获取的形态从「hook 订阅」变成「Promise 直读」。对状态库的意义：**TanStack 的 `useSuspenseQuery` 内部就是 use(promise) 的消费者**——查询缓存的 promise 直接喂给 use。
- use(Promise) 的缓存要求：**同一 Promise 引用重复读取不重复挂起**——React 要求 Promise 是「稳定引用」（组件外/缓存层持有），在渲染期间 new Promise 是反模式（每次渲染新 promise = 永远挂起）。这与 getSnapshot 引用稳定（ZSM-615）是同一条纪律的 Promise 版。
- 与状态库的分工变化：轻量「一次性请求」可以直接 `use(fetchPromise)`（缓存 promise 用 useMemo 模块级），无需引入 Query 库；需要缓存语义（staleTime/失效/去重）仍用 Query——「use 降低了裸 promise 的门槛，但缓存语义的复杂度没变」。
- use(Context) 也统一了：条件 use context（hook 规则外的动态读取）——对状态库的意义：`use(Context)` 可在条件分支读取，状态分层（ZSM-796）的判定更灵活。
- 追问钩子：use(Promise) 与 ErrorBoundary 的组合——promise reject 会被最近的 ErrorBoundary 接（不进 try/catch），错误处理路径与 useSuspenseQuery 一致（ZSM-648）。

```javascript
// use(Promise) 的三种姿势
// 1) 配合缓存层（TanStack Query 的内部形态）
function TodoList() {
  const data = use(todoQuery.promise)   // 查询缓存的稳定 Promise → use 挂起/恢复
  return <ul>{data.map((t) => <li key={t.id}>{t.title}</li>)}</ul>
}

// 2) 轻量一次性请求（模块级 promise 缓存）
const userPromise = fetchUser(1)          // 组件外：稳定引用
function Profile() {
  const user = use(userPromise)           // 挂起 → Suspense → 恢复
  return <div>{user.name}</div>
}

// 3) 反模式：渲染期 new Promise（永远挂起）
function Bad() {
  const data = use(new Promise((r) => setTimeout(() => r(fetchData()), 0)))  // ✗ 每次渲染新引用
  return null
}
// ✓ 正确：useMemo 化或提到组件外

// 与状态库的分工判断
const DECISION = {
  一次性请求: 'use(promise) 直接读，缓存用 useMemo/模块级',
  缓存语义(失效/去重/失效传播): 'TanStack Query——复杂度没消失只是被库封装',
  中间态: 'useSuspenseQuery = Query 缓存 promise + use 的官方组合（648）',
}
```
