---
title: [1125] 笔试手写：从 trace 计算链路的耗时瀑布与瓶颈
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, 多Agent, 性能]
type: 笔试题
---

## 1125：笔试手写：从 trace 计算链路的耗时瀑布与瓶颈

**答**：实现 waterfall(trace)：trace 为 { spans: [{ name, start, end, parent?: string }] }（ms 时间戳，可有父子嵌套）。输出每 span 的 { name, self: 自身耗时（扣除直接子 span 占用）, total }；找出 self 耗时最大的 span 名为瓶颈。子 span 区间可能重叠，需合并后扣除。

```js
function waterfall(trace) {
  const children = new Map();
  for (const s of trace.spans) {
    if (s.parent) {
      if (!children.has(s.parent)) children.set(s.parent, []);
      children.get(s.parent).push(s);
    }
  }
  const rows = trace.spans.map(s => {
    const subs = children.get(s) || [];
    // 子 span 区间合并（处理重叠）
    const iv = subs.map(c => [c.start, c.end]).sort((a, b) => a[0] - b[0]);
    let overlap = 0, cur = null;
    for (const [a, b] of iv) {
      if (!cur) cur = [a, b];
      else if (a <= cur[1]) cur[1] = Math.max(cur[1], b);   // 重叠合并
      else { overlap += cur[1] - cur[0]; cur = [a, b]; }
    }
    if (cur) overlap += cur[1] - cur[0];
    const total = s.end - s.start;
    return { name: s.name, total, self: total - overlap };
  });
  const bottleneck = rows.reduce((m, r) => (r.self > m.self ? r : m), rows[0]);
  return { rows, bottleneck: bottleneck.name };
}
```

**评分点**：
- self 耗时 = total - 子 span 占用，且子 span 区间需合并（重叠子 span 双扣是经典 bug）
- 嵌套层级语义：直接子级扣除即可（孙级已含在子级 total 内）
- 瓶颈按 self 而非 total 排（total 大可能只是等待子级）
- 能讨论：异步并发的父 span（子 span 并行时 self 应为 total - max(子区间) 而非减和，进阶讨论点）

