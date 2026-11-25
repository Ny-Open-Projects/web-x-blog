---
title: [1257] 笔试手写：实现 文档三态 diff 索引器
date: 2026-11-22
categories: [AI与Agent]
tags: [前端面试, 笔试题, RAG]
type: 笔试题
---

## 1257：笔试手写：实现 文档三态 diff 索引器

**需求**：实现 indexDiff(oldMap, newMap)：oldMap/newMap 为 { path: contentHash }。输出三态：added（新文档）、removed（消失文档）、updated（hash 变化）。更新项按依赖深度排序（路径深度浅的先重建，保证父文档先入库）；返回 { added, removed, updated, plan }，plan 为一次批量入库的顺序数组（先删后增更）。

```js
function indexDiff(oldMap, newMap) {
  const added = [], removed = [], updated = [];
  for (const p of Object.keys(newMap)) {
    if (!(p in oldMap)) added.push(p);
    else if (oldMap[p] !== newMap[p]) updated.push(p);
  }
  for (const p of Object.keys(oldMap)) if (!(p in newMap)) removed.push(p);
  const depth = p => p.split('/').length;
  const plan = [
    ...removed.sort((a, b) => depth(b) - depth(a)),   // 深的先删（子先父后）
    ...[...added, ...updated].sort((a, b) => depth(a) - depth(b)), // 浅的先建
  ];
  return { added, removed, updated, plan };
}
```

**评分点**：
- 三态判定逻辑（对 old/new 各遍历一次）
- 删除按深度降序、新增按深度升序（父子顺序约束）
- hash 不变即跳过（增量省成本的落点）
- 能讨论：updated 是否需要段落级 diff 决定重建范围
