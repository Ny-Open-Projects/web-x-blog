---
title: [VIZ-096] 实现大数据 tooltip 的聚合显示。
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-096：实现大数据 tooltip 的聚合显示。
**答**：百万级散点/密集折线的 tooltip 不能逐点显示，策略：① 命中改**分桶索引**——hover 位置 O(1) 定位到像素桶；② 内容**聚合**——取该桶及邻域统计（计数/均值/分位数），展示"该区域 3,842 个点，均值 52.3"；③ 高频更新 rAF 节流；④ 需要明细时提供"点击下钻"逐点查看。核心思想与 VIZ-080 的分桶渲染共用同一套桶结构，一份数据两处使用。

```javascript
// 大数据 tooltip：复用分桶结构，O(1) 命中 + 邻域聚合成统计文案
function aggregateTooltip(bins, cols, cell, px, py) {
  const cx = Math.floor(px / cell), cy = Math.floor(py / cell);
  let sum = 0, count = 0;
  for (let dy = -2; dy <= 2; dy++) {            // 5x5 邻域统计
    for (let dx = -2; dx <= 2; dx++) {
      const v = bins[(cy + dy) * cols + (cx + dx)];
      if (v != null) { sum += v; count++; }
    }
  }
  return count
    ? `该区域平均 ${Math.round(sum / count)} 点/格，密度 ${sum}`
    : '该区域无数据';
}
// 链路：mousemove -> rAF 节流 -> 桶索引命中 -> 聚合文案 -> tooltip 渲染
// 需要明细时提示"点击查看该区域明细"，点击后取桶内原始数据逐点展示
```
