---
title: [ZSM-116] SWR 翻页时怎么避免列表闪烁？keepPreviousData 和中间 loading 的取舍是什么？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-116：SWR 翻页时怎么避免列表闪烁？keepPreviousData 和中间 loading 的取舍是什么？
**答**：
- 翻页时 key 变化，SWR 默认行为是「清空当前 data、重新 isLoading」，列表瞬间消失闪一下。`keepPreviousData: true` 让 data 在新 key 数据到达前保留上一页内容，配合 isValidating 显示顶部进度即可平滑翻页。
- 取舍：keepPreviousData 体验好但存在「展示错误页数据」的窗口期，敏感数据（账单、成绩）宁可闪也要保证所见即所得，要按业务分级。
- 配套技巧：列表区域固定高度、行元素加 key（用数据 id）避免 DOM 重建导致的图片重载；`placeholderData`（v2）可给固定占位。
- 追问钩子：TanStack Query 对应 `placeholderData: keepPreviousData`（v5 从 isPreviousData 改名），两库一致体现了业界对分页平滑的标准解法。

```javascript
import useSWR from 'swr'

function GoodsTable({ page }) {
  const { data, isLoading, isValidating } = useSWR(
    `/api/goods?page=${page}`, fetcher,
    { keepPreviousData: true }   // 新页数据到达前保留上一页
  )
  return (
    <div className={isValidating && !isLoading ? 'table refreshing' : 'table'}>
      {isLoading ? <Skeleton/> : <Table rows={data.list}/>}
      {/* 视觉上：上一页仍在展示，仅顶部细进度条提示刷新中 */}
    </div>
  )
}
```
