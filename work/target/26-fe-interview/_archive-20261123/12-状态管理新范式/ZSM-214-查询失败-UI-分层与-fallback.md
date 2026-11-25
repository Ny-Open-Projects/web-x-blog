---
title: [ZSM-214] 查询失败后的 UI 分层怎么做错误兜底与降级
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-214：查询失败后的 UI 分层怎么做错误兜底与降级

**答**：
- 三层兜底：首次无数据失败 → 错误页/错误态；有过成功数据后失败（isError && data 存在）→ 展示旧数据 + 局部提示「刷新失败」；非关键模块 → 降级占位不阻塞页面
- `data` 在失败后仍保留（缓存还在），判断 `query.isError && !query.data` 才是致命错误，不要 isError 就整页报错
- 重试 UI 用 `query.refetch` 手动重试或 `refetchOnWindowFocus` 自动补拉
- 结构上用 ErrorBoundary 接住 render 抛错（配合 useSuspenseQuery），普通 useQuery 的 error 走局部条件渲染

```javascript
const q = useQuery({ queryKey: ['sku', id], queryFn: fetchSku })

if (q.isError && !q.data) return <FullError onRetry={q.refetch} />   // 致命
if (q.isPending) return <Skeleton />
return (
  <>
    <Sku sku={q.data} />
    {q.isError && <InlineError onRetry={q.refetch} />}                // 有旧数据：局部提示
  </>
)
```
