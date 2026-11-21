---
title: [ALG-210] 数据导出：把 N 行导出拆成最少的接口请求（每请求上限不同）——贪心 + 证明
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

**场景**：导出 1000 行，接口支持 `limit` 参数（最大 200），但单请求还有服务端耗时约束：行数越多单请求越慢。要求**最少请求数**：贪心每次取最大 limit。证明贪心最优：交换论证（任何最优解的第一个请求若 < limit，可以扩到 limit 不增加请求数）。

**思路**：贪心 O(n/limit)，配合"剩余不足 limit 时一次拿完"的尾批处理。进阶：不同区间 limit 不同（如前 500 行免费 200/请求，之后 100/请求）时贪心仍成立（每段独立最大）。

```javascript
function minRequests(totalRows, { limit = 200, maxBytes = 1024 * 512, bytesPerRow = 3000 } = {}) {
  const requests = [];
  let offset = 0;
  while (offset < totalRows) {
    // 本请求最大行数 = min(limit, 字节预算能承载的行数)
    const byBytes = Math.max(1, Math.floor(maxBytes / bytesPerRow));
    const size = Math.min(limit, byBytes, totalRows - offset);
    requests.push({ offset, limit: size });
    offset += size;
  }
  return requests;    // 长度即最少请求数
}
minRequests(1000);
// => [{offset:0,limit:170},{offset:170,limit:170},{offset:340,limit:170},...]
// 170 = 512KB/3KB 向下取整（字节约束先于 limit 生效）
// 贪心正确性（交换论证）：最优解第一个请求 size < 可行最大值 s 时，
// 把它扩成 s 只会覆盖更多行、后续请求只会更少 —— 与最优解请求数相同或更少
// 复杂度 O(totalRows / pageSize)
```

**评分点**：
- 贪心策略正确且取约束的最小者（limit 与字节预算、剩余行数三者取 min）。
- 交换论证或等价方式说明贪心最优性（只会答"贪心"不给证明扣分）。
- 尾批/边界处理（剩余 < limit 一次拿完；bytesPerRow 过大时 max(1,·) 保底）。
- 复杂度标注 O(n/pageSize)。
