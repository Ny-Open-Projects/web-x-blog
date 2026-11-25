---
title: [ZSM-109] SWR 的 isLoading 和 isValidating 有什么区别？怎么据此设计加载 UI？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-109：SWR 的 isLoading 和 isValidating 有什么区别？怎么据此设计加载 UI？
**答**：
- isLoading = 没有任何可展示数据且正在请求（首次进入或 key 变化后缓存为空）；isValidating = 只要正在验证就为 true，包括有旧数据时的后台重取。
- UI 设计结论：骨架屏绑 isLoading，顶部细进度条/半透明遮罩绑 isValidating——两者混用是「列表页每次焦点重取都闪骨架屏」的根因。
- 还有 `data === undefined && error === undefined` 的手工判断历史写法，v2 之后直接用 isLoading，面试要能说清 v1→v2 的语义升级。
- key 变化时（如翻页）data 会保留上一个 key 的值直到新数据到达（默认行为），需要显式清场时用 `keepPreviousData: false` 配合判断 `data?.page !== page`。

```javascript
function SearchList({ keyword, page }) {
  const { data, error, isLoading, isValidating } = useSWR(
    `/api/search?kw=${keyword}&page=${page}`, fetcher
  )
  return (
    <div style={{ opacity: isValidating && data ? 0.7 : 1 }}>
      {isLoading && <Skeleton rows={10}/>}          {/* 首次：骨架屏 */}
      {!isLoading && error && <ErrorView/>}
      {data && <List items={data.list}/>}
      {isValidating && data && <TopProgressBar/>}   {/* 后台重取：细进度条 */}
    </div>
  )
}
```
