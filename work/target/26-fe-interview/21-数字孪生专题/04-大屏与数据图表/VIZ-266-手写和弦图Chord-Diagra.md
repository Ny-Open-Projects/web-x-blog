---
title: [VIZ-266] 手写和弦图（Chord Diagram）：环形关系流量
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-266：手写和弦图（Chord Diagram）：环形关系流量

**答**：
- 题目：和弦图——环形节点 + 弧形连线（宽度=流量）。布局：节点弧段按值分配角度，连线两端对齐各自节点弧段内子区间。
- 思路：节点弧段 = 环上角度区间；每个 link 在源节点弧段内按流出顺序占用子区间；连线 = 二次贝塞尔（两端宽度一致）。
- 评分点：弧段角度分配；link 子区间不重叠；贝塞尔控制点在圆心。

```javascript
function chordLayout(nodes, links, { radius = 200 } = {}) {
  const total = nodes.reduce((s, n) => s + n.value, 0);
  let angle = -Math.PI / 2;                                // 从顶部开始
  const nodeArcs = nodes.map(n => {
    const span = n.value / total * 2 * Math.PI;
    const arc = { id: n.id, a0: angle, a1: angle + span, used: 0 };
    angle += span + GAP;
    return arc;
  });
  const arcMap = new Map(nodeArcs.map(a => [a.id, a]));
  const chords = links.map(l => {
    const src = arcMap.get(l.source), dst = arcMap.get(l.target);
    const srcSpan = l.value / total * 2 * Math.PI;
    const s0 = src.a0 + src.used; src.used += srcSpan;      // 子区间占用
    const dstSpan = l.value / total * 2 * Math.PI;
    const d0 = dst.a0 + dst.used; dst.used += dstSpan;
    return { s0, s1: s0 + srcSpan, d0, d1: d0 + dstSpan, width: srcSpan * radius };   // 贝塞尔端点
  });
  return { nodeArcs, chords };
}
```
