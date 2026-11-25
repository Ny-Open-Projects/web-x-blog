---
title: [VIZ-265] 手写桑基图（Sankey）布局：节点分层与连线带宽
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-265：手写桑基图（Sankey）布局：节点分层与连线带宽

**答**：
- 题目：实现桑基图布局——节点按依赖分层（最长路径分层），节点高度 = 流量值，连线带宽 = 流量占比。错峰排列防节点重叠。
- 思路：① 拓扑分层；② 层内垂直排布（节点高度 = value × scale，重叠时错开）；③ link 带宽 = value × scale，贝塞尔连线。
- 评分点：拓扑分层；流量→高度映射；层内防重叠错峰。

```javascript
function sankeyLayout(nodes, links, { height = 600, gap = 20 } = {}) {
  const levels = topoLevels(nodes, links);                 // 拓扑分层
  const maxFlow = Math.max(...links.map(l => l.value));
  const scale = (height - (Math.max(...levels.map(l => l.length)) - 1) * gap)
    / Math.max(...levels.map(l => l.reduce((s, n) => s + n.value, 0)));   // 全局流量比例尺
  const positions = new Map();
  for (const [li, level] of levels.entries()) {
    let y = 0;
    for (const node of level) {
      const h = node.value * scale;
      positions.set(node.id, { x: li * COL_W, y, h });      // 层内顺序排布
      y += h + gap;
    }
  }
  return { positions, links: links.map(l => ({ ...l, width: l.value * scale })) };
}
// 连线渲染：三次贝塞尔（水平控制点）——同一节点出边按目标 y 排序防交叉
```
