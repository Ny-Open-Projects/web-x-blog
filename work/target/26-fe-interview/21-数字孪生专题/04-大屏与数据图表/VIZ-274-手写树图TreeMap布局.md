---
title: [VIZ-274] 手写树图（TreeMap）布局：squarified 算法
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-274：手写树图（TreeMap）布局：squarified 算法

**答**：
- 题目：TreeMap——层级矩形填充（面积=值），squarified 算法让矩形接近正方形（可读性）。
- 思路：按值降序，逐行装填（行内矩形并排），选择「使行内矩形长宽比最优」的行断点——squarify 核心是比较两种断点方案的worst aspect ratio。
- 评分点：面积→面积映射；worst ratio 比较；递归子级布局。

```javascript
function squarify(items, rect) {                           // items 按值降序
  const total = items.reduce((s, i) => s + i.value, 0);
  const out = [];
  let rest = [...items], rx = rect.x, ry = rect.y, rw = rect.w, rh = rect.h;
  while (rest.length) {
    const area = rw * rh;
    const row = [];
    let bestRatio = Infinity, bestRow = null;
    for (let i = 0; i < rest.length; i++) {                 // 尝试行断点
      row.push(rest[i]);
      const rowArea = row.reduce((s, x) => s + x.value, 0) / total * area;
      const side = Math.min(rw, rh);
      const worst = Math.max(...row.map(x => {
        const itemArea = x.value / total * area;
        return Math.max(itemArea / side, side / itemArea);   // 长宽比
      }));
      if (worst < bestRatio) { bestRatio = worst; bestRow = row.length; }
    }
    const chosen = rest.slice(0, bestRow);
    const rowArea = chosen.reduce((s, x) => s + x.value, 0) / total * area;
    const side = Math.min(rw, rh);
    let off = 0;
    for (const item of chosen) {                            // 行内排布
      const w = item.value / total * area / side;
      out.push({ item, rect: rw >= rh
        ? { x: rx, y: ry + off, w: side, h: w }
        : { x: rx + off, y: ry, w: w, h: side } });
      off += w;
    }
    if (rw >= rh) { ry += side; rh -= side; } else { rx += side; rw -= side; }   // 缩剩余区域
    rest = rest.slice(bestRow);
  }
  return out;
}
```
