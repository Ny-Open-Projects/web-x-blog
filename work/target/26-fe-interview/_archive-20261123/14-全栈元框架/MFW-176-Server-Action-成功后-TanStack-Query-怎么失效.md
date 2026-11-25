---
title: [MFW-176] Server Action 写成功后，TanStack Query 缓存怎么失效？
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-176：Server Action 写成功后，TanStack Query 缓存怎么失效？
**答**：
- 核心矛盾：Server Action 生活在 RSC 世界（服务端），TanStack Query 缓存生活在客户端，Action 成功后客户端缓存不会自动知道，需要显式桥接。
- 推荐分层：**服务端事实归 RSC 管**——Action 里 `revalidateTag` 让服务端组件拿到新数据；**客户端视图归 Query 管**——在调用 Action 的客户端回调里 `queryClient.invalidateQueries({ queryKey })`。
- 更优雅的方案：把 Action 包成客户端函数封装层（mutate hook），内部统一「调用 Action → 按 tag 映射 invalidate 对应 queryKey → router.refresh()（如需刷新 RSC 段）」。
- 乐观更新组合拳：`useOptimistic` 做即时 UI，Action 失败时回滚 + invalidate 拉真实数据，成功时用返回值 `setQueryData` 精准更新省一次请求。
- 注意别两套都刷导致闪烁：如果页面数据完全由 Query 提供，只 invalidate Query 即可；如果列表是 RSC 渲染的，只能靠 revalidate + refresh。

```javascript
'use client';
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { createOrderAction } from './actions';

export function useCreateOrder() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: (input) => createOrderAction(input), // Server Action
    onSuccess: (order) => {
      qc.invalidateQueries({ queryKey: ['orders'] }); // 客户端列表刷新
      qc.setQueryData(['order', order.id], order);    // 精准写回，省一次详情请求
    },
  });
}
```
