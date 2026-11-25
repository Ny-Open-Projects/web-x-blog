---
title: [906] TanStack Query 的分页与无限滚动在大型应用的缓存架构
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, TanStack Query, 分页]
type: 面试题
---

## 906：TanStack Query 的分页与无限滚动在大型应用的缓存架构

**答**：
- 分页模式：常规分页用 placeholderData（切页保留旧数据防跳变）；无限滚动用 useInfiniteQuery（pageParam 链），maxPages 限制内存（长列表缓存 N 页足够）。
- 大列表缓存重量：无限列表缓存 50 页 x100 条 = 5000 条对象在缓存里——大列表用「缓存分页元数据 + 视口内取数」混合架构，或 maxPages + 定向失效。
- 列表项更新一致性：列表里改一条（点赞）——用 setQueryData 做「精确 patch」（按 id 找到 item 更新），比整列表 invalidate 便宜且不闪烁；配合乐观更新模板。
- 追问钩子：为什么切页要 keepPreviousData？——没有它每次切页渲染骨架屏页面跳变；placeholderData 让旧数据占位直到新页到达，UI 稳定但要有视觉提示。

```ts
const inf = useInfiniteQuery({
  queryKey: ['feed', filter],
  queryFn: ({ pageParam = 0 }) => fetchFeed({ cursor: pageParam, filter }),
  initialPageParam: 0,
  getNextPageParam: last => last.nextCursor,
  maxPages: 10,                                  // 内存护栏
});
// 精确 patch 更新列表项
qc.setQueryData(['feed', filter], old => ({ ...old,
  pages: old.pages.map(p => ({ ...p,
    items: p.items.map(it => it.id === id ? { ...it, liked: true } : it) })),
}));
```

