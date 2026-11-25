---
title: [ZSM-795] RSC 时代的状态架构：服务端状态与客户端 store 的边界再思考
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-795：RSC 时代的状态架构：服务端状态与客户端 store 的边界再思考

**答**：
- RSC（React Server Components）改变了状态边界：服务端组件直接读数据库/服务端缓存（不进客户端 store），客户端 store 的职责收缩为「纯交互态 + 服务端数据的客户端缓存（TanStack hydration）」。旧的「全局 store 包打天下」在 RSC 架构下大量失效——很多数据根本不需要进客户端 store。
- RSC 下的状态分层决策树：数据在服务端渲染期确定且交互中不更新 → RSC 直读（零客户端状态）；交互中要更新且只在客户端 → 客户端 store；跨请求缓存复用 → TanStack Query + hydration（ZSM-632）；需要用户输入后服务端计算 → Server Action + useOptimistic（React 19 的乐观钩子接管了乐观更新语义）。
- Server Action 与状态库的协作：action 返回结果直接更新 TanStack 缓存（或 revalidate），客户端 store 只存 UI 态——「Server Action 是新的 mutation 层」，Zustand 里不再需要手写 async action 管理请求生命周期。
- 边界的判定信号：一个状态字段问「它是渲染产物还是用户意图」——渲染产物归服务端，用户意图归客户端。RSC 架构下客户端 store 的体积普遍缩小 50%+（渲染产物被剥离）。
- 追问钩子：RSC 的「状态序列化边界」——传给客户端组件的 props 必须可序列化（无函数/类实例），store 想给 RSC 传数据只能通过 Server Action 参数或 URL——这个限制决定了「客户端 store 是 RSC 树的孤岛」，跨边界通信只能走显式协议。

```javascript
// RSC 状态分层决策
// app/products/page.tsx（RSC）：渲染产物直读，零客户端状态
export default async function Page() {
  const products = await db.products.list()        // 服务端直读：不进客户端 store
  return <ProductList products={products} />       // 传给客户端组件的 props 可序列化
}

// components/cart-button.tsx（客户端）：交互态
'use client'
function AddToCart({ productId }) {
  const [pending, startTransition] = useTransition()
  const [optimistic, addOptimistic] = useOptimistic(cartCount, (cur, delta) => cur + delta)

  function add() {
    startTransition(async () => {
      addOptimistic(1)                             // React 19 乐观钩子：接管乐观更新
      await addToCartAction(productId)             // Server Action：新的 mutation 层
      // 服务端 revalidate 或 updateQueryData 对账
    })
  }
  return <button onClick={add} disabled={pending}>加购({optimistic})</button>
}

// 分层判定树
// 渲染期确定+不更新      → RSC 直读（零状态）
// 客户端交互更新          → 客户端 store / useOptimistic
// 跨请求缓存              → TanStack + hydration
// 用户输入+服务端计算      → Server Action + optimistic
// 序列化边界：store → RSC 只能走 Action 参数或 URL（孤岛协议）
```
