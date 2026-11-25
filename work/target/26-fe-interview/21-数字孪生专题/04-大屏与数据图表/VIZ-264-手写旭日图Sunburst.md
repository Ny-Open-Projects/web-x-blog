---
title: [VIZ-264] 手写旭日图（Sunburst）：层级环形布局与交互下钻
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-264：手写旭日图（Sunburst）：层级环形布局与交互下钻

**答**：
- 题目：实现旭日图布局——层级数据递归分配角度（子节点角度 = 父角度 × 占比），渲染为同心环；点击下钻（聚焦子树）。
- 思路：递归角度分配：节点角度 = 父角度 × (child.value / parent.sum)；半径按深度递增；下钻 = 重设根并重算。
- 评分点：递归角度分配；占比守恒（子角度和=父角度）；下钻重根。

```javascript
function sunburstLayout(root, { startAngle = 0, endAngle = 2 * Math.PI, innerR = 0 } = {}) {
  const nodes = [];
  function walk(node, a0, a1, depth) {
    nodes.push({ id: node.id, depth, a0, a1, value: node.value });   // 角度区间
    const r0 = innerR + depth * RING_WIDTH;
    const total = node.children?.reduce((s, c) => s + c.value, 0) ?? 0;
    let angle = a0;
    for (const c of node.children ?? []) {
      const span = (a1 - a0) * (c.value / total);          // 子角度 = 父 × 占比
      walk(c, angle, angle + span, depth + 1);
      angle += span;
    }
  }
  walk(root, startAngle, endAngle, 0);
  return nodes;
}
function drillDown(nodes, id) {                            // 下钻：重设根
  const target = nodes.find(n => n.id === id);
  return sunburstLayout(findSubtree(id), { startAngle: 0, endAngle: 2 * Math.PI });   // 重算
}
```
