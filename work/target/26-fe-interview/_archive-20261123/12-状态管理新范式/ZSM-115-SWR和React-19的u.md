---
title: [ZSM-115] React 19 时代的 SWR 有什么新玩法？useOptimistic、Action 与 SWR 怎么配合？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-115：React 19 时代的 SWR 有什么新玩法？useOptimistic、Action 与 SWR 怎么配合？
**答**：
- 分工：React 19 的 useOptimistic 管「提交期间的瞬时乐观视图」，SWR 管「服务端数据缓存」；表单 Action 提交成功后调用 mutate 失效缓存，三者各司其职。
- useOptimistic 的乐观值只在 transition 期间存在、提交结束即消失，所以「长期保留的乐观数据」（如已发送消息）仍要在成功后写入 SWR 缓存，两者不是替代关系。
- `useTransition` 包裹 mutate 可避免失效重取时把整个列表标记为 loading 造成闪烁。
- 面试表达：不要说「React 19 内置取数所以 SWR 过时了」——真正的取数缓存方案（use cache / RSC）在服务端，客户端交互缓存 SWR 仍是主力。

```javascript
'use client'
import useSWR from 'swr'
import { useOptimistic, useRef, useTransition } from 'react'

function Comments({ postId }) {
  const { data: comments, mutate } = useSWR(`/api/posts/${postId}/comments`, fetcher)
  const [pending, startTransition] = useTransition()
  const [optimistic, addOptimistic] = useOptimistic(
    comments ?? [], (list, text) => [...list, { id: 'tmp', text, pending: true }])
  const textRef = useRef()

  function submit(e) {
    e.preventDefault()
    const text = textRef.current.value
    startTransition(async () => {
      addOptimistic(text)                    // 提交期瞬时乐观视图
      const created = await api.addComment(postId, text)
      await mutate(list => [...(list ?? []), created])  // 成功后写入持久缓存
    })
  }
  return <Comments list={optimistic} onSubmit={submit} pending={pending}/>
}
```
