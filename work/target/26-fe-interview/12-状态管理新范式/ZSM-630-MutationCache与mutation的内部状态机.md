---
title: [ZSM-630] Mutation 的内部状态机：MutationCache 与 onSuccess 链的执行时序
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-630：Mutation 的内部状态机：MutationCache 与 onSuccess 链的执行时序

**答**：
- Mutation 与 Query 的本质差异：Mutation **默认不在缓存里保留结果**（结果直接返回给调用者），只有 options（gcTime 等）在 MutationCache 登记；Observer 也不订阅 mutation——useMutation 是「命令式触发 + 局部状态」。v5 才把 mutation 状态机统一成与 Query 一致的 `{ status, fetchStatus }`（idle→pending→success/error）。
- onSuccess 链的执行时序：mutationFn resolve 后，先执行 mutation 级 `onSuccess(data, vars, ctx)`，然后依次向上执行 `useMutation` 级 → `MutationCache` 全局 `onSuccess`（通过 subscribe 或全局 config）。全局层适合做埋点/统一失效（`queryClient.invalidateQueries`），局部层做业务处理——两层职责分开。
- 上下文 ctx：onMutate 返回值作为 ctx 传入 onSuccess/onError——乐观更新的快照就靠它传递（onMutate 存 prev，onError 还原）。
- retry 与 mutation：默认 retry 0（不同于 query 的 3）——写操作重试要显式开启且必须幂等；`networkMode` 同样生效。
- 追问钩子：`scope: { id }`（v5）把同 scope 的 mutation 排队串行——同一资源并发写场景用 scope 防乱序。

```javascript
// Mutation 执行链骨架（v5 简化）
async function executeMutation(mutation, vars) {
  mutation.state = { status: 'pending', fetchStatus: 'fetching', variables: vars, submittedAt: Date.now() }
  let ctx
  try {
    ctx = await mutation.options.onMutate?.(vars)         // ① 乐观钩子
    const data = await mutation.options.mutationFn(vars)  // ② 真正执行
    // ③ 钩子链：局部 → 全局
    await mutation.options.onSuccess?.(data, vars, ctx)
    mutation.cache.config.onSuccess?.(data, vars, mutation)
    mutation.state = { ...mutation.state, status: 'success', data, fetchStatus: 'idle' }
    return data
  } catch (error) {
    // onError 同构：局部 → 全局
    await mutation.options.onError?.(error, vars, ctx)
    mutation.cache.config.onError?.(error, vars, mutation)
    mutation.state = { ...mutation.state, status: 'error', error, fetchStatus: 'idle' }
    throw error
  }
}

// useMutation 标准组合：乐观 + 失效 + 埋点
useMutation({
  mutationFn: updateTodo,
  scope: { id: `todo-${id}` },              // 同一 todo 的并发写排队
  onMutate: async (newTodo) => {
    await queryClient.cancelQueries({ queryKey: ['todo', id] })   // 停在途请求防覆盖
    const prev = queryClient.getQueryData(['todo', id])
    queryClient.setQueryData(['todo', id], newTodo)               // 乐观写
    return { prev }                                               // ctx 传递快照
  },
  onError: (_e, _v, ctx) => queryClient.setQueryData(['todo', id], ctx.prev),  // 回滚
  onSettled: () => queryClient.invalidateQueries({ queryKey: ['todo', id] }),  // 终局对账
})
```
