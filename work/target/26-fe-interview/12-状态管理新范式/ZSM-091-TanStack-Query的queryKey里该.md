---
title: [ZSM-091] 场景题：商品列表有搜索词、分类、排序、页码，queryKey 怎么组织？切换筛选时旧请求怎么防竞态？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-091：场景题：商品列表有搜索词、分类、排序、页码，queryKey 怎么组织？切换筛选时旧请求怎么防竞态？
**答**：
- key：`['goods', { kw, category, sort, page }]`——对象形式一个 key 表达全部维度，失效时可按前缀（['goods']）或维度（Query 无法按值前缀失效，需设计 key 层级如 ['goods', category, ...]）。
- 防竞态天然成立：不同 key 是不同缓存条目，旧请求返回只写旧 key 的缓存，不会污染新 key；切回旧筛选还能秒显旧缓存。
- 若担心慢请求堆积：切换时可 cancelQueries(['goods']) 取消在途；或给 keyword 做 debounce + placeholderData(keepPreviousData) 平滑过渡。
- gcTime 默认 5 分钟足够筛选往返；高频筛选配 structuralSharing + placeholderData 避免闪 loading。

```javascript
useQuery({
  queryKey: ['goods', category, { kw, sort, page }],
  queryFn: () => api.goods({ kw, category, sort, page }),
  placeholderData: keepPreviousData, // 切筛选时展示旧数据平滑过渡
})
// 激进防竞态：切换时取消旧请求
useEffect(() => () => qc.cancelQueries({ queryKey: ['goods', category] }), [category])
```
