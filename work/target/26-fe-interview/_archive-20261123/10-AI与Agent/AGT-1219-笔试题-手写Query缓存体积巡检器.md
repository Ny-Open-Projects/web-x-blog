---
title: [1219] 笔试手写：实现缓存大条目与总量守卫
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, TanStack Query]
type: 笔试题
---

## 1219：笔试手写：实现缓存大条目与总量守卫

**需求**：实现 CachePatrol(limitPerEntry=1_000_000, limitTotal=20_000_000)：scan(entries)——entries 为 { key, jsonLen }[]；输出 { oversized: 超单条上限的 key 列表, total, overTotal, byDomain: { [key[0]]: bytes } }（按域聚合体积）。

```js
function cachePatrol(entries, limitPerEntry = 1_000_000, limitTotal = 20_000_000) {
  const oversized = [], byDomain = {};
  let total = 0;
  for (const e of entries) {
    total += e.jsonLen;
    const d = e.key[0] ?? 'unknown';
    byDomain[d] = (byDomain[d] || 0) + e.jsonLen;
    if (e.jsonLen > limitPerEntry) oversized.push(e.key);
  }
  return { oversized, total, overTotal: total > limitTotal, byDomain };
}
const entries = [
  { key: ['feed', 1], jsonLen: 2_000_000 },
  { key: ['feed', 2], jsonLen: 500_000 },
  { key: ['user', 1], jsonLen: 300_000 },
];
console.log(cachePatrol(entries));
// oversized [['feed',1]]；total 2.8M；byDomain { feed: 2.5M, user: 300k }
```

**评分点**：
- 双阈值（单条+总量）守卫
- byDomain 聚合（定位膨胀域——治理动作指向明确）
- key[0] 缺失的 unknown 兜底
- 能讨论：巡检 -> 动作联动（oversized 域 gcTime 缩短/removeQueries）、jsonLen 与真实内存的差异

