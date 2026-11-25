---
title: [1265] 笔试手写：实现 embedding 批量合并缓存器
date: 2026-11-22
categories: [AI与Agent]
tags: [前端面试, 笔试题, RAG]
type: 笔试题
---

## 1265：笔试手写：实现 embedding 批量合并缓存器

**需求**：实现 embedBatch(texts, cache, embed)：cache 为 Map<text, vector>，embed(list) 批量向量化。规则：先查缓存命中的直接复用；未命中的去重合并（同文本只发一次）后批量调用 embed；结果回填缓存；按原 texts 顺序返回向量数组。

```js
function embedBatch(texts, cache, embed) {
  const misses = [];
  const slot = texts.map(t => {
    if (cache.has(t)) return { t, hit: true, v: cache.get(t) };
    if (!misses.includes(t)) misses.push(t); // 去重合并
    return { t, hit: false };
  });
  const fetched = misses.length ? await embed(misses) : [];
  const vec = new Map(misses.map((t, i) => [t, fetched[i]]));
  for (const [t, v] of vec) cache.set(t, v); // 回填缓存
  return slot.map(s => s.hit ? s.v : vec.get(s.t));
}
// 注：async 函数，调用 await embedBatch(...)
```

**评分点**：
- 命中/未命中分流，未命中先文本级去重再批量
- 结果按原顺序还原（slot 映射表思想）
- 回填缓存供后续复用
- 能讨论：批量上限（一次 embed 不超 64 条）需再分批
