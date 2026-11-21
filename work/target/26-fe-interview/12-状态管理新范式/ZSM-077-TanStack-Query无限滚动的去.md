---
title: [ZSM-077] useInfiniteQuery 列表去重与列表项更新怎么做？invalidate 后 pages 会被覆盖吗？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-077：useInfiniteQuery 列表去重与列表项更新怎么做？invalidate 后 pages 会被覆盖吗？
**答**：
- 去重两层：服务端游标保证不重复（权威）；前端 flatMap 前按 id 去重兜底（服务端插入新行导致游标重叠时）。
- 单项更新：invalidate(['goods','detail',id]) 不会更新已加载的无限列表页——列表页里的该项是列表缓存的拷贝。解法：setQueryData 遍历 pages 定点改该项，或 invalidate 整个列表 key（代价：全部页重取）。
- invalidate 无限查询的 key：pages 结构会被「第一页响应」整体替换，已加载的第 2~N 页丢失（除非服务端支持按已加载游标重取）。所以编辑类操作优先 setQueryData 定点更新。
- 渲染层用 select 做合并去重，避免每帧 flatMap。

```javascript
// 定点更新无限列表里的单项
function patchPost(postId, patch) {
  qc.setQueryData(['feed'], old => old && ({
    ...old,
    pages: old.pages.map(page => ({
      ...page,
      items: page.items.map(p => p.id === postId ? { ...p, ...patch } : p),
    })),
  }))
}
```
