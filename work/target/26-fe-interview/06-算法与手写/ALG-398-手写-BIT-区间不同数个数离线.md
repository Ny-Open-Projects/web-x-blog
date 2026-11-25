---
title: [ALG-398] 手写 BIT 区间不同数个数（离线）：去重统计
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-398：手写 BIT 区间不同数个数（离线）：去重统计

**答**：
- 题目：数组多组查询「区间 [l, r] 内不同值的个数」。离线经典：按右端点排序 + BIT 维护每个值「上次出现位置」。
- 思路：扫到位置 i 的值 v：若 v 出现过，先在旧位置 -1；在 i 处 +1。查询 [l, r] 的答案 = sum(r) - sum(l-1)（每个值只在「最右出现位置」计 1）。
- 评分点：离线按 r 排序；同值只计最右；删除旧位置的 -1。

```javascript
function distinctCount(arr, queries) {                     // queries: [{l, r, id}]
  const sorted = [...queries].sort((a, b) => a.r - b.r);
  const bit = new BIT(arr.length);
  const last = new Map();                                   // 值 → 上次出现位置
  const ans = new Array(queries.length);
  let ptr = 1;                                              // 1-based 扫描
  for (const q of sorted) {
    while (ptr <= q.r) {
      const v = arr[ptr - 1];
      if (last.has(v)) bit.add(last.get(v), -1);            // 旧位置删除
      bit.add(ptr, 1);                                      // 新位置计入
      last.set(v, ptr);
      ptr++;
    }
    ans[q.id] = bit.sum(q.r) - bit.sum(q.l - 1);            // 不同值个数
  }
  return ans;
}
```
