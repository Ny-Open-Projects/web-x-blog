---
title: [VIZ-183] 实现 option diff 与增量 setOption。
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-183：实现 option diff 与增量 setOption。
**答**：ECharts setOption 默认 merge，但重复全量 setOption 仍触发重算。优化：① **diff**——新旧 option 深比较（data 引用与关键配置），无变化直接跳过 setOption；② **增量**——只 patch 变化的 series（seriesId 匹配），`replaceMerge: 'series'` 控制替换语义；③ lazyUpdate + silent 配合；④ React/Vue 封装层最常见反模式：props 每次新引用导致全量 setOption——封装层必须做 memo/diff。大数据追加用 appendData 或自管数据 + dataZoom 窗口。

```javascript
// 封装层：diff 后增量 setOption
const lastOption = new WeakMap();
function smartSetOption(chart, next) {
  const prev = lastOption.get(chart);
  if (prev && deepEqual(prev, next)) return;          // 无变化直接跳过
  const patch = diffOptions(prev, next);              // 只提取变化的分支
  chart.setOption(patch, {
    lazyUpdate: true,
    silent: true,
    replaceMerge: ['series'],                         // series 级替换语义
  });
  lastOption.set(chart, next);
}
// diffOptions：按 option 分支做浅/深比较，series 用 seriesId 对齐后再 diff data 引用
```
