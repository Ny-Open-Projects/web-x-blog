---
title: [1241] 笔试手写：实现并发 span 的 self 时间计算（并行感知）
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, 多Agent]
type: 笔试题
---

## 1241：笔试手写：实现并发 span 的 self 时间计算（并行感知）

**答**：实现 waterfall(trace)：trace.spans 为 { name, start, end, parent? }[]。对每个 span 计算 self：单子级时 total - dur(子)；多子级且并行（子区间重叠）时 total - max(子区间)；串行子级时 total - sum。判定并行：子区间存在重叠。输出 { rows: [{ name, total, self, mode: 'serial'|'parallel'|'leaf' }] }。

```js
function waterfall(trace) {
  const children = new Map();
  for (const s of trace.spans) {
    if (s.parent) (children.get(s.parent) ?? children.set(s.parent, []).get(s.parent)).push(s);
  }
  return trace.spans.map(s => {
    const subs = children.get(s) || [];
    if (!subs.length) return { name: s.name, total: s.end - s.start,
      self: s.end - s.start, mode: 'leaf' };
    const iv = subs.map(c => [c.start, c.end]).sort((a, b) => a[0] - b[0]);
    let overlap = 0, cur = iv[0], parallel = false;
    for (let i = 1; i < iv.length; i++) {
      if (iv[i][0] < cur[1]) { parallel = true; cur[1] = Math.max(cur[1], iv[i][1]); }
      else { overlap += cur[1] - cur[0]; cur = iv[i]; }
    }
    overlap += cur[1] - cur[0];
    const total = s.end - s.start;
    const sub = parallel ? Math.max(...subs.map(c => c.end - c.start))
      : overlap;                                     // 并行扣 max，串行扣 sum
    return { name: s.name, total, self: total - sub,
      mode: parallel ? 'parallel' : 'serial' };
  });
}
```

**评分点**：
- 并行/串行的区分语义（并行扣 max、串行扣 sum——纯串行版会高估 self 消耗）
- 重叠检测（区间合并后判定）
- leaf 的 self = total
- 能讨论：真实分布式 trace 的 span 语义（宽度优先聚合）、async 边界的进阶（span 状态机）

