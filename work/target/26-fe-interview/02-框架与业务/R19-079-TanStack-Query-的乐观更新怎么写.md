---
title: [R19-079] TanStack Query 的乐观更新怎么写？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-079：TanStack Query 的乐观更新怎么写？
**答**：
- onMutate 阶段先 cancelQueries 防止在途请求覆盖乐观值，再用 setQueryData 手动改缓存。
- 返回的 previous 通过 context 传给 onError，失败时精确回滚。
- onSettled 里 invalidateQueries 让服务端数据最终一致。
- 与 useOptimistic 的分工：TanStack Query 管服务端状态的乐观，React 19 的 useOptimistic 管 Action 场景的乐观。

```jsx
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';

function TodoList() {
  const qc = useQueryClient();
  const { data: todos } = useQuery({ queryKey: ['todos'], queryFn: fetchTodos });

  const mutation = useMutation({
    mutationFn: toggleTodo,
    onMutate: async (todo) => {
      await qc.cancelQueries({ queryKey: ['todos'] });   // 防止在途请求覆盖乐观值
      const previous = qc.getQueryData(['todos']);
      qc.setQueryData(['todos'], old =>
        old.map(t => (t.id === todo.id ? { ...t, done: !t.done } : t)),
      );
      return { previous };                                // 传给 onError 回滚
    },
    onError: (err, todo, ctx) => qc.setQueryData(['todos'], ctx.previous),
    onSettled: () => qc.invalidateQueries({ queryKey: ['todos'] }),
  });

  return todos?.map(t => (
    <TodoItem key={t.id} todo={t} onToggle={() => mutation.mutate(t)} />
  ));
}
```
