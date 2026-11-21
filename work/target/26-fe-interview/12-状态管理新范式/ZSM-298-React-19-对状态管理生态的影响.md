---
title: [ZSM-298] React 19 的变化对状态管理生态意味着什么
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-298：React 19 的变化对状态管理生态意味着什么

**答**:
- Actions/useActionState 承接「表单提交态」：pending/error 以前要自己管的状态被框架收编，表单库的提交态职责减少
- use() + Suspense 让「Promise 即状态」：异步数据可作为可 suspension 的值传递，原子库异步 atom 与之竞争但提供缓存/失效语义
- useOptimistic 收编乐观更新基础件，但「缓存失效/回滚/冲突合并」仍属 Query 层——框架给原语，生态管生命周期
- React Compiler（自动 memo）降低「引用陷阱」痛苦但不改变语义；forwardRef/ref-as-prop、useSyncExternalStore 仍是外部 store 正统接入点

```javascript
// React 19：提交态框架化
const [state, formAction, pending] = useActionState(createOrder, null)
const [optimistic, addOptimistic] = useOptimistic(state, (cur, item) => ({ ...cur, items: [...cur.items, item] }))
<form action={formAction}>…</form>   // pending 不再自己 useState
```
