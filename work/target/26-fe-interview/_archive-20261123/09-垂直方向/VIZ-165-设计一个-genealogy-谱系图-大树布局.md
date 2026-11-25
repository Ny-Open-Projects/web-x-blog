---
title: [VIZ-165] 设计一个 genealogy 谱系图（大树布局）。
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-165：设计一个 genealogy 谱系图（大树布局）。
**答**：① **布局**——家谱是 DAG（通婚合并），简单家谱按 tidy tree（Reingold-Tilford）横向树 + 代际泳道；万人级用横向虚拟化 + 子树聚合折叠；② **视觉**——男左女右配色、世代泳道标注、头像照片；③ **交互**——点击节点展开/收起子树（子树折叠为 + 汇总节点）、定位某人居中、双击看个人页；④ **遮挡**——远世代节点信息递减、重叠子树合并计数；⑤ **数据**——GedCOM 标准解析入图。

```javascript
// 可折叠大族谱：tidy tree + 子树聚合
const root = d3.hierarchy(familyTree, d => d.children?.length ? d.children : null);
root.descendants().forEach(d => { d._children = d.children; d.children = d.depth < 3 ? d.children : null; }); // 默认展开 3 代
function update(src) {
  const tree = d3.tree().nodeSize([36, 160])(root);
  node.join('g')
    .attr('transform', d => `translate(${d.y},${d.x})`)
    .on('click', (e, d) => {
      if (d.children) { d._children = d.children; d.children = null; }  // 收起
      else { d.children = d._children; d._children = null; }            // 展开
      update(d);
    });
  link.join('path').attr('d', d3.linkHorizontal()
    .x(d => d.y).y(d => d.x));
}
```
