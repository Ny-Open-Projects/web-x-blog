---
title: [ZSM-143] TanStack Query 的 isLoading、isPending、isFetching 三个状态怎么区分？v5 为什么改名？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-143：TanStack Query 的 isLoading、isPending、isFetching 三个状态怎么区分？v5 为什么改名？
**答**：
- status 三态：pending（还没有第一次成功数据）、error、success。isPending = status === 'pending'；isLoading = isPending && isFetching（首次取数中）的组合标志。
- isFetching = 该 key 正在发请求，包括有数据后的后台重取——所以「转圈到底绑谁」的答案：骨架屏绑 isLoading/isPending，静默刷新条绑 isFetching。
- v5 改名动机：v4 的 isLoading 其实是「首次加载」，与「正在请求」语义混淆，v5 把 pending 定义为严格 status、isLoading 定义为组合标志，语义分层清晰。
- mutation 同理：isPending 表示提交中；配合 mutation 的 status 迁移时注意 v4 的 isLoading 全部改叫 isPending。

```javascript
function GoodsList({ id }) {
  const { data, status, isPending, isLoading, isFetching } = useQuery({
    queryKey: ['goods', id], queryFn: () => api.goods(id),
  })
  // status: 'pending' | 'error' | 'success'
  // isPending  = status === 'pending'
  // isLoading  = isPending && isFetching   ← 首次取数中
  // isFetching = 任何正在进行的请求        ← 含后台重取

  if (isLoading) return <Skeleton/>
  if (status === 'error') return <ErrorView/>
  return <div className={isFetching ? 'refreshing' : ''}>
    <List items={data}/>              {/* 后台重取时旧数据仍在，半透明提示 */}
  </div>
}
```
