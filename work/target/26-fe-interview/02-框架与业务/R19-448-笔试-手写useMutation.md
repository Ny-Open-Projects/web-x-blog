---
title: [R19-448] 笔试：手写 useMutation（提交类请求 hook）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 数据流]
type: 笔试题
---

## R19-448：笔试：手写 useMutation

**答**：实现 `useMutation(mutationFn, { onSuccess, onError, onSettled, invalidateKeys })`：① mutate(variables) 返回 Promise（调用方可 await）；② 状态：isPending/isError/data；③ 成功后自动 invalidate 相关 query（传 queryClient 引用）；④ 乐观更新集成（onMutate 钩子：返回快照用于失败回滚）；⑤ 防重复提交（pending 时 mutate 拒绝或排队选项）。写出实现。

```javascript
export function useMutation(mutationFn, {
  onSuccess, onError, onSettled, onMutate, invalidateKeys, queryClient, queue = false,
} = {}) {
  const [state, setState] = useState({ isPending: false, isError: false, data: null, error: null });

  const mutate = useCallback(async (variables) => {
    if (state.isPending && !queue) throw new Error('mutation in progress');
    let snapshot;
    setState((s) => ({ ...s, isPending: true, isError: false }));
    try {
      snapshot = await onMutate?.(variables);          // 乐观更新(返回快照)
      const data = await mutationFn(variables);
      setState({ isPending: false, isError: false, data, error: null });
      invalidateKeys?.forEach((k) => queryClient?.invalidateQueries({ queryKey: k }));
      onSuccess?.(data, variables);
      return data;
    } catch (e) {
      setState({ isPending: false, isError: true, data: null, error: e });
      if (snapshot) snapshot.restore?.();              // 失败回滚乐观更新
      onError?.(e, variables, snapshot);
      throw e;
    } finally {
      onSettled?.();
    }
  }, [mutationFn, state.isPending]);

  return { ...state, mutate };
}
// 用法
const likeMut = useMutation((postId) => api.like(postId), {
  onMutate: async (postId) => {
    const prev = queryClient.getQueryData(['post', postId]);
    queryClient.setQueryData(['post', postId], (p) => ({ ...p, likes: p.likes + 1 }));  // 乐观
    return { restore: () => queryClient.setQueryData(['post', postId], prev) };
  },
  invalidateKeys: [['post']],
  queryClient,
});
```

**评分点**：
- onMutate 快照回滚协议（乐观更新的标准模式）
- invalidate 联动（成功后失效相关查询）
- 防重复（拒绝 vs 排队选项）
- mutate 返回 Promise（调用方可续接）
