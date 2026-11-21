---
title: [MFW-203] RSC 边界案例：乐观更新与 RSC 重渲染的内容回跳
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-203：乐观更新与 RSC 重渲染的内容回跳

**答**:
- 边界现象：useOptimistic 点赞即时 +1，但 Server Action 触发的 RSC 重渲染带回旧数据 → UI 闪回（乐观值被旧服务端树覆盖）
- 根因：乐观状态只存在于客户端 hook 内，RSC 树重渲染把服务端旧值灌回 props——两个数据流抢同一块 UI
- 解法：Action 内先 revalidate 再返回（服务端树是最新值，重渲染带回新数据与乐观值一致）；或 UI 用客户端缓存（Query）作为唯一真相源，RSC 只管首屏
- 判定法则：交互频繁的数据不放在 RSC props 里——RSC 管静态骨架，客户端缓存管动态数据，避免双源

```javascript
// 正确：Action 内 revalidate 保证服务端树新鲜
export async function like(id) {
  'use server'
  await db.like(id)
  revalidateTag(`post-${id}`)     // 重渲染带回 like+1 → 与乐观值一致，无闪回
}
// 或者：交互数据走客户端缓存，RSC 只出壳
```
