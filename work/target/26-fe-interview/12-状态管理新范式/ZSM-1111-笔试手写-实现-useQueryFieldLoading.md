---
title: [1111] 笔试手写：实现 useQueryFieldLoading
date: 2026-11-22
categories: [状态管理新范式]
tags: [前端面试, 笔试题, Hook]
type: 笔试题
---

## 1111：笔试手写：实现 useQueryFieldLoading

**答**：实现 aggregateLoading(queries)：queries 为 { key, isLoading, isError }[]。聚合策略：allOf = 任一 loading 即 loading（整体就绪才展示）；anyOf = 全部 loading 才算 loading（有一个就先展示一个）；hidePrevious = anyOf 且防抖动（某 query 从 loading→done 的一帧内不闪 loading）。返回 { allOf, anyOf, hidePrevious, failed }（failed 为已错误的 key 列表）。

```js
function aggregateLoading(queries) {
  const allOf = queries.some(q => q.isLoading);
  const anyOf = queries.every(q => q.isLoading);
  // hidePrevious：前一次就绪过（记 ready 集合）则本次 loading 不展示
  const ready = new Set();
  for (const q of queries) {
    if (!q.isLoading && !q.isError) ready.add(q.key);
    else if (q.isError) ready.delete(q.key);
  }
  const hidePrevious = queries.some(q => q.isLoading && !ready.has(q.key)) && ready.size > 0;
  const failed = queries.filter(q => q.isError).map(q => q.key);
  return { allOf, anyOf, hidePrevious, failed };
}
// 注：ready 集合在真实 Hook 里应跨渲染持久（useRef），笔试用闭包语义表达
```

**评分点**：
- allOf/anyOf 两种语义的布尔实现（some/every 别写反）
- hidePrevious 的就绪集合持久化思想（防闪烁核心）
- failed 收集供错误 UI 分流
- 能讨论：三策略对应三种页面骨架（整页骨架 / 分区渐进 / 保旧数据）
