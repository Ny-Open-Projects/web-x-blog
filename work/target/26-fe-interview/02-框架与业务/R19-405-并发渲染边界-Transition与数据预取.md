---
title: [R19-405] 并发渲染边界：Transition 与数据预取的编排
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 数据流]
type: 面试题
---

## R19-405：并发渲染边界：Transition 与数据预取的编排

**答**：
- 预取先行模式：hover/intent 时开始 fetch（数据层缓存）——点击导航时 transition 渲染直接命中缓存（无等待）
- React 19 的 prerender 探索：`experimental_prerender`（预渲染 UI + 数据到缓存）——transition 更新直接复用预渲染结果
- 数据层选择：React Query prefetchQuery + transition——「预取（独立于渲染）+ 低优渲染」的两段式
- 取消语义：transition 被打断 ≠ fetch 取消——预取请求继续完成并进缓存（下次命中）；要取消用 AbortController 在数据层管理
- 效果度量：点击到可见（transition pending 时长）——预取命中率决定该模式收益

```jsx
function NavItem({ href, prefetch }) {
  const queryClient = useQueryClient();
  const onMouseEnter = () => queryClient.prefetchQuery({ queryKey: ['page', href], queryFn: () => api.get(href) });
  const onClick = (e) => {
    e.preventDefault();
    startTransition(() => navigate(href));   // 数据已缓存 → 快速提交
  };
  return <a href={href} onMouseEnter={onMouseEnter} onClick={onClick} />;
}
```
