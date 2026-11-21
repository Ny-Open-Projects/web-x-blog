---
title: [ZSM-071] TanStack Query 的乐观更新怎么做？onMutate 快照与回滚的完整流程是什么？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-071：TanStack Query 的乐观更新怎么做？onMutate 快照与回滚的完整流程是什么？
**答**：
- onMutate：取消相关在途请求（防旧响应覆盖乐观值）→ 读旧缓存做快照 → setQueryData 写入乐观结果 → 返回快照。
- onError：用 context 里快照 setQueryData 回滚；onSettled：invalidateQueries 让服务端权威数据兜底对齐。
- 乐观更新只该改「本次操作直接相关」的缓存切片；列表排序/分页等复杂推导不要乐观，容易与服务端结果打架。
- 场景：点赞、收藏、拖拽排序这类低风险高频操作乐观；支付、删除账户这类高危操作悲观（等响应）。

```javascript
const like = useMutation({
  mutationFn: api.like,
  onMutate: async (postId) => {
    await qc.cancelQueries({ queryKey: ['posts'] })        // 1. 取消在途
    const prev = qc.getQueryData(['posts'])               // 2. 快照
    qc.setQueryData(['posts'], old =>                     // 3. 乐观写
      old.map(p => p.id === postId ? { ...p, liked: true, likes: p.likes + 1 } : p))
    return { prev }                                       // 4. 快照入 context
  },
  onError: (_e, _v, ctx) => qc.setQueryData(['posts'], ctx.prev), // 回滚
  onSettled: () => qc.invalidateQueries({ queryKey: ['posts'] }), // 权威对齐
})
```
