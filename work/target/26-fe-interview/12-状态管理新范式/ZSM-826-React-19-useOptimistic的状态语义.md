---
title: [ZSM-826] React 19 的 useOptimistic：框架级乐观更新的状态语义
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-826：React 19 的 useOptimistic：框架级乐观更新的状态语义

**答**：
- `useOptimistic(state, reducer)` 把乐观更新内建进 React：传乐观值给 action（`addOptimistic(like)`），渲染期间显示乐观态；**transition 提交完成后自动回滚到真实 state**——回滚语义由框架托管，不再手写快照还原（对比 ZSM-528 的手写对账器）。
- 关键语义：乐观值只存在于 transition 的渲染期间——**必须在 startTransition/action 内调用 addOptimistic**，事件同步回调里调用无效。回滚时机 = 关联的 async transition 完成时；成功路径的「转正」要靠 action 内 await 后的 setState（用服务端结果覆盖）。
- 与状态库的分工：组件级乐观（点赞按钮、行内编辑）用 useOptimistic 零样板；跨组件/跨路由的乐观（购物车全局角标）仍需 store 层乐观（Zustand + 对账器）——「局部乐观归框架，全局乐观归 store」。
- 与 Server Action 的组合是官方预期形态：`useOptimistic + startTransition(async () => { await serverAction() })`——服务端成功后 revalidate 或返回值 setState 转正，失败 transition 异常自动回滚乐观值。
- 追问钩子：useOptimistic 的局限——乐观值的「作用域是组件」且不能持久（刷新即失）、不支持乐观队列（多个并发乐观会合并 reducer，注意 reducer 幂等）；复杂乐观场景（部分失败选择性保留）仍要手写。

```javascript
'use client'
import { useOptimistic, useState, useTransition } from 'react'

function LikeButton({ postId, initialLikes }) {
  const [likes, setLikes] = useState(initialLikes)
  const [optimisticLikes, addOptimisticLike] = useOptimistic(
    likes,
    (cur, delta) => cur + delta,          // 乐观 reducer
  )
  const [isPending, startTransition] = useTransition()

  function like() {
    startTransition(async () => {          // 必须在 transition 内
      addOptimisticLike(1)                 // 立即显示 +1（渲染期乐观）
      const res = await likeAction(postId) // Server Action
      if (res.ok) {
        setLikes(res.likes)                // 转正：服务端结果覆盖（transition 结束前）
      }
      // 失败：不 setState → transition 结束自动回滚乐观值
    })
  }

  return <button onClick={like}>{isPending ? optimisticLikes : likes} 赞</button>
}

// 对比手写对账器（ZSM-528）：
// 框架版：回滚自动、零快照管理、作用域=组件、不能持久
// 手写版：跨组件/持久/乐观队列/选择性保留 —— 全局乐观仍需 store 层
```
