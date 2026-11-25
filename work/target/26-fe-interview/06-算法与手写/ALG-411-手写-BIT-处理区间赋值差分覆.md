---
title: [ALG-411] 手写 BIT 处理区间赋值（差分+覆盖标记）：批量开关
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-411：手写 BIT 处理区间赋值（差分+覆盖标记）：批量开关

**答**：
- 题目：配置开关序列，操作「区间 [l,r] 全部设为 on/off」与「单点查」。BIT 不直接支持赋值——用「染色段计数」技巧：维护「最后一次赋值区间」集合，查询时看是否被最近赋值覆盖。
- 思路：工程务实解——若赋值操作远多于查询：维护有序段（珂朵莉树思想，ALG-374）；若查询多：每段赋值改写 BIT 逐点（区间长度可控时 O(len log n)）。讲清 BIT 不适合赋值的本质（不可减）。
- 评分点：BIT 不支持赋值的本质（max/assign 不可减）；改写逐点的适用条件；果断换珂朵莉/线段树。

```javascript
class AssignSegments {                                     // 赋值场景的正确选型
  constructor(n) { this.segments = new Map([[1, { end: n, on: false }]]); }
  assign(l, r, on) {                                        // 区间赋值：段覆盖
    for (const [s, seg] of [...this.segments])
      if (s >= l && seg.end <= r) this.segments.delete(s);
    for (const [s, seg] of this.segments)
      if (s < l && seg.end >= l) { const oe = seg.end; seg.end = l - 1;
        if (oe >= r) this.segments.set(r + 1, { end: oe, on: seg.on }); }   // 跨界截断
    for (const [s, seg] of this.segments)
      if (s <= r && seg.end > r) { this.segments.set(r + 1, { end: seg.end, on: seg.on }); seg.end = r; }
    this.segments.set(l, { end: r, on });
  }
  get(i) { for (const [s, seg] of this.segments)
    if (s <= i && i <= seg.end) return seg.on; return false; }
}
```
