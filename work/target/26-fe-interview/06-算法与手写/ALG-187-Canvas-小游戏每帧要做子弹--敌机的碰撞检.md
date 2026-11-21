---
title: [ALG-187] Canvas 小游戏每帧要做子弹 × 敌机的碰撞检测，200 子弹 × 100 敌机全量两两比较是 2 万次。如何优化？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-187：Canvas 小游戏每帧要做子弹 × 敌机的碰撞检测，200 子弹 × 100 敌机全量两两比较是 2 万次。如何优化？
**答**：AABB（轴对齐包围盒）判定：两矩形在 x、y 两个方向投影都重叠才算碰撞（`a.x < b.x + b.w && a.x + a.w > b.x && ...`），O(1) 每对。批量优化用"排序 + 扫描"粗筛：子弹按 y 排序，敌机按 y 排序后双指针——y 区间不重叠的直接跳过，把均摊复杂度从 O(n×m) 降到 O(n log n + m log m + k)（k 为实际重叠对数）。更高频场景可上四叉树空间划分。

```javascript
function aabbHit(a, b) { // AABB：x 与 y 两个方向投影都重叠才算碰撞
  return a.x < b.x + b.w && a.x + a.w > b.x &&
         a.y < b.y + b.h && a.y + a.h > b.y;
}
function batchHit(bullets, enemies) {
  const hits = [];
  const bs = [...bullets].sort((a, b) => a.y - b.y);
  const es = [...enemies].sort((a, b) => a.y - b.y);
  let j = 0;
  for (const b of bs) {
    // 指针推进：跳过 y 区间整体在子弹上方的敌机（粗筛）
    while (j < es.length && es[j].y + es[j].h < b.y) j++;
    for (let k = j; k < es.length; k++) {
      if (es[k].y > b.y + b.h) break;   // 敌机已在子弹下方：后续更远，剪枝
      if (aabbHit(b, es[k])) hits.push([b, es[k]]);
    }
  }
  return hits;
}
```
