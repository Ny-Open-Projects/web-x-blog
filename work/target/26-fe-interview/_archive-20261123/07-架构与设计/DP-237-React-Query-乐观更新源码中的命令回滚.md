---
title: [DP-237] 源码识别：React Query 乐观更新源码中的命令与回滚？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-237：源码识别：React Query 乐观更新源码中的命令与回滚？
**答**:
- 命令+备忘录：onMutate 先做快照（previous = getQueryData）并写入乐观值——快照即备忘录，setMutationFn 的请求即命令。
- 回滚：onError 用快照 setQueryData 恢复；onSuccess invalidateQueries 触发重新拉取对账（ARC-058 全链路）。
- 观察者协调：乐观写入触发所有 observer 更新 UI；服务端结果回来 invalidate → 广播第二次——UI 中间态就是"乐观快照 → 真值"的状态过渡。
- 识别要点：能说清"乐观值与服务器值冲突的合并策略"（以服务器为准 + 提示）是设计决策点，不是框架细节。

```typescript
useMutation({
  mutationFn: updateTodo,
  onMutate: async (newTodo) => {
    await queryClient.cancelQueries(['todo', newTodo.id]);      // 停在途请求防覆盖
    const previous = queryClient.getQueryData(['todo', newTodo.id]);  // 备忘录快照
    queryClient.setQueryData(['todo', newTodo.id], newTodo);    // 乐观写（触发 observers）
    return { previous };                                        // 上下文传给 onError
  },
  onError: (err, vars, ctx) =>
    queryClient.setQueryData(['todo', vars.id], ctx.previous),  // 回滚
  onSuccess: () =>
    queryClient.invalidateQueries({ queryKey: ['todo'] }),      // 服务端对账
});
// 两个广播：乐观写一次、invalidate 拉新后一次 —— UI 无感切换靠引用 diff
```
