---
title: [VIZ-282] 手写瀑布图（Waterfall）：增减累计与连接线
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-282：手写瀑布图（Waterfall）：增减累计与连接线

**答**：
- 题目：瀑布图——各分类增减值按序累计（收入→支出→结余），柱体从「上一累计」到「新累计」，连接虚线串联。
- 思路：累计计算 running = Σ 前序；柱体 y 范围 = [prevRunning, curRunning]；正负色（增绿减红）；连接线 = 前柱顶到本柱起。
- 评分点：累计语义（分类值 vs 存量值）；柱体范围方向处理（负值）；连接虚线。

```javascript
function waterfallLayout(items) {                         // items: [{name, delta}]
  let running = 0;
  return items.map(item => {
    const prev = running;
    running += item.delta;
    return { name: item.name, delta: item.delta,
      y0: Math.min(prev, running), y1: Math.max(prev, running),   // 柱体范围
      positive: item.delta >= 0,                           // 增减色
      connector: { from: prev, to: running },              // 连接虚线（渲染层画）
      running };
  });
}
// 渲染映射：y0/y1 → 像素（比例尺含 0 基线）；connector 画前柱右上到本柱左上虚线
// 例：营收 100 → 成本 -60 → 利润 40（末项 total 型柱体从 0 起）
```
