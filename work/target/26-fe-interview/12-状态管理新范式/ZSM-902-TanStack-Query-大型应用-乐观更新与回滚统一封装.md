---
title: [902] TanStack Query 的乐观更新在大型应用里怎么统一封装
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, TanStack Query, 乐观更新]
type: 面试题
---

## 902：TanStack Query 的乐观更新在大型应用里怎么统一封装

**答**：
- 统一封装 mutation hook：useOptimMutation(fn, { listKey, updateFn })——把「缓存快照 -> 乐观写入 -> 失败回滚 -> 成功失效」四步模板化，业务层只传 updateFn，避免每个业务各写一套 onMutate（十几个 mutation 各写一遍必然出 bug）。
- 回滚的关键：onMutate 里 cancelQueries（防旧请求覆盖乐观值）+ 保存 previous 快照 + context 传递给 onError 回滚；onSettled 里 invalidate（成功后以服务端为准校准）。
- 并发乐观更新：同一列表两个乐观 mutation 并发时快照互相覆盖——大型应用用「patch 队列」（每次记录 patch 而非快照，回滚只撤销自己的 patch）。
- 追问钩子：乐观更新成功后还要 invalidate 吗？——要：乐观值是客户端推演，服务端可能有服务端逻辑（默认值/触发器），invalidate 校准是最终一致性的兜底。

```ts
function useOptimMutation<T, V>(fn: (v: V) => Promise<T>, opt: {
  key: QueryKey; apply: (old: T[], v: V) => T[];
}) {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: fn,
    onMutate: async (v: V) => {
      await qc.cancelQueries({ queryKey: opt.key });
      const prev = qc.getQueryData<T[]>(opt.key);
      qc.setQueryData<T[]>(opt.key, old => opt.apply(old ?? [], v));
      return { prev };                              // 快照入 context
    },
    onError: (_e, _v, ctx) => ctx?.prev && qc.setQueryData(opt.key, ctx.prev),
    onSettled: () => qc.invalidateQueries({ queryKey: opt.key }),
  });
}
```

