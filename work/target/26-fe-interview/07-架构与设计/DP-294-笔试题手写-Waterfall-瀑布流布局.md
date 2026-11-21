---
title: [DP-294] 笔试题：手写瀑布流布局（最短列放置）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-294：笔试题：手写瀑布流布局（最短列放置）？
**题目**：实现瀑布流：1) 知道每项高度（或渲染后测量），每次放入当前最短列；2) 容器宽度变化时重算列数（min-width 列）与整体重排；3) 返回每项的 { x, y, w, h }；4) 支持顺序插入（增量更新列高）。
**评分点**：
- 最短列选择正确（列高数组 min + index）。
- 响应式列数计算正确（Math.floor(width / minColWidth)）。
- 输出坐标含列间距 gap。
- 增量插入 O(cols) 而非 O(n)。
```javascript
function waterfall(items, containerWidth, { minColWidth = 240, gap = 16 } = {}) {
  const cols = Math.max(1, Math.floor((containerWidth + gap) / (minColWidth + gap)));   // 2)
  const colWidth = (containerWidth - gap * (cols - 1)) / cols;
  const heights = new Array(cols).fill(0);
  const placed = [];
  for (const item of items) {                             // 1) 最短列放置
    let minIdx = 0;
    for (let c = 1; c < cols; c++) if (heights[c] < heights[minIdx]) minIdx = c;
    const pos = { x: minIdx * (colWidth + gap), y: heights[minIdx], w: colWidth, h: item.height };
    heights[minIdx] += item.height + gap;                 // 4) 增量更新
    placed.push({ id: item.id, ...pos });
  }
  return { placed, totalHeight: Math.max(...heights, 0) };
}
// 响应式：ResizeObserver(container) → waterfall(items, newWidth) 重排（记录高度缓存，只重算坐标）
```
