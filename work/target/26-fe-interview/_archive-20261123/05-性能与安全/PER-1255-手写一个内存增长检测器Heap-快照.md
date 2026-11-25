---
title: [PER-1255] 手写一个内存增长检测器：Heap 快照 diff 简版
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1255：手写一个内存增长检测器：Heap 快照 diff 简版

**答**：
- 需求：实现 heapDiff(snapshotA, snapshotB)。snapshots 为 { constructors: { Name: retainedBytes } }；输出 { growth: [{ ctor, delta }], leaked: [ctor], totalGrowth }：delta > 100KB 视为 leaked 候选，按 delta 降序；totalGrowth 为总和。
- 边界：B 中新增构造器 delta = 全量；A 独有（被回收）记负 delta 不进 leaked；retained 缺失按 0。
- 评分点：diff 计算；泄漏阈值；排序；负增长排除

```javascript
function heapDiff(a, b, { leakThreshold = 100 * 1024 } = {}) {
  const growth = [];
  const ctors = new Set([...Object.keys(a), ...Object.keys(b)]);
  for (const c of ctors) {
    const delta = (b[c] ?? 0) - (a[c] ?? 0);
    growth.push({ ctor: c, delta });
  }
  growth.sort((x, y) => y.delta - x.delta);
  return { growth,
    leaked: growth.filter(g => g.delta > leakThreshold)
      .map(g => g.ctor),
    totalGrowth: growth.reduce((s, g) => s + g.delta, 0) };
}
// leaked 非空 -> 检查对应组件 unmount 是否彻底（detached DOM/定时器）
```
