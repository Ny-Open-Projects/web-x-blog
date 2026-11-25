---
title: [VIZ-041] D3 布局生成器（pie/force/hierarchy）的工作原理？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-041：D3 布局生成器（pie/force/hierarchy）的工作原理？
**答**：D3 布局器**不画图**，只把数据加工成图形参数（角度/坐标/矩形），绘制仍交给 selection——这是它"计算与渲染分离"的设计。**pie**：算每个扇区的 startAngle/endAngle；**force**：物理模拟器，引力/斥力/弹簧三种力在每次 tick 迭代中更新节点坐标，直到系统收敛（alpha 衰减到 alphaMin）；**hierarchy 系列**：hierarchy 包装层级数据 + sum 聚合，treemap/partition/tree/pack 各自输出矩形/扇区/坐标。布局都是纯函数，可预计算缓存。

```javascript
// 布局生成器不画图，只把数据加工成图形参数，绘制仍交给 selection
const pie = d3.pie().value(d => d.value).sort(null); // sort(null) 保持原始顺序
const arc = d3.arc().innerRadius(60).outerRadius(100);
svg.selectAll('path').data(pie(data)).join('path').attr('d', arc);
// 力导向：simulation 每次 tick 迭代收敛，on tick 里同步图形位置
const sim = d3.forceSimulation(nodes)
  .force('link', d3.forceLink(links).id(d => d.id).distance(80)) // 弹簧力
  .force('charge', d3.forceManyBody().strength(-100))            // 电荷斥力
  .force('center', d3.forceCenter(300, 200))                     // 向心力
  .on('tick', () => {
    link.attr('x1', d => d.source.x).attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x).attr('y2', d => d.target.y);
    node.attr('transform', d => `translate(${d.x},${d.y})`);
  });
```
