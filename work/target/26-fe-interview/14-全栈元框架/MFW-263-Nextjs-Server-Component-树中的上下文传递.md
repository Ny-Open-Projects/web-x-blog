---
title: [MFW-263] Server 树中的上下文传递（不用 Context 怎么传租户/用户）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 笔试题
---

## MFW-263：Server 树上下文传递

**答**:
- RSC 不能用 React Context（服务端无实例树共享）——替代三式：①AsyncLocalStorage 请求级存储（middleware/loader 写入、任意深度 server 函数读取——真正意义的 server context）②props 显式下传（布局层取一次传 children——类型安全但层级深时冗长）③模块级缓存按请求 key（危险——并发串数据，必须 per-request 隔离）
- Next 的 cache() 方案：请求内 memoize 的异步函数（同请求同参数返回同一 Promise——自动去重 + 伪上下文），是官方推荐的「server context」形态
- 边界：cache() 只在渲染请求内有效——Action/rgetoe Handler 里用它取用户要自己传（或框架提供的其他机制）

```javascript
// server-only 请求级用户
import { cache } from 'react'
export const getUser = cache(async () => {
  const token = cookies().get('session')
  return db.user.byToken(token)                 // 同请求多次调用 → 同 Promise 去重
})
// 任意深度 RSC：const user = await getUser()   // 无需 props 层层传
```
