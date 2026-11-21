---
title: [R19-239] 给出 Action + useOptimistic + useTransition 的点赞按钮完整样板
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-239：给出 Action + useOptimistic + useTransition 的点赞按钮完整样板
**答**：
- 结构：serverState 来自 props（服务端组件传入）、useOptimistic 叠加乐观值、startTransition 包 action 调用、失败 toast。
- 代码即样板：这是大厂高频手写题的标准形态。
```javascript
'use client'
function LikeButton({ postId, likes, likeAction }) {
  const [optimisticLikes, addOptimistic] = useOptimistic(
    likes,
    (cur, delta) => Math.max(0, cur + delta)
  )
  const [, startTransition] = useTransition()
  function onClick() {
    startTransition(async () => {
      addOptimistic(1)
      const res = await likeAction(postId)   // server action
      if (!res.ok) toast('点赞失败，已恢复')  // React 自动回滚乐观值
    })
  }
  return <button onClick={onClick} className={optimisticLikes > likes ? 'active' : ''}>
    👍 {optimisticLikes}
  </button>
}
```
- 要点：addOptimistic 必须在 transition/action 上下文内调用；回滚由 React 自动完成。
