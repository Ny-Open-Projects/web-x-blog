---
title: [ZSM-095] 场景题：IM 发消息要在 TanStack Query 里做乐观更新+排序+失败重试，怎么设计？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-095：场景题：IM 发消息要在 TanStack Query 里做乐观更新+排序+失败重试，怎么设计？
**答**：
- 缓存结构 `['messages', roomId]` 无限查询（游标）。乐观消息带本地 id（uuid）+ status: 'sending'，插入时按时间戳排序放尾部。
- onMutate：取消在途 + setQueryData 插入乐观项；onSuccess：服务端返回正式 id → setQueryData 定点替换（本地 id 映射），status 'sent'；onError：status 'failed' 保留气泡 + 手动重试按钮（mutation.reset 或再次 mutate）。
- 不在 onSettled invalidate 整个会话——全量重取会把 pages 结构打回第一页，只做定点替换；会话列表未读数单独 invalidate。
- 排序兜底：服务端补齐正式 createdAt 后再排一次，防止本地时钟偏差。

```javascript
onMutate: async (msg) => {
  await qc.cancelQueries({ queryKey: ['messages', roomId] })
  const optimistic = { ...msg, localId: crypto.randomUUID(), status: 'sending' }
  qc.setQueryData(['messages', roomId], old => insertSorted(old, optimistic))
  return { localId: optimistic.localId }
},
onSuccess: (server, _v, ctx) => {
  qc.setQueryData(['messages', roomId], old => replaceLocal(old, ctx.localId, server))
},
onError: (_e, _v, ctx) => {
  qc.setQueryData(['messages', roomId], old => markFailed(old, ctx.localId)) // UI 给重试入口
},
```
