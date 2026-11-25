---
title: [VIZ-470] 手写一个 overdraw 热点定位器
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## VIZ-470：手写一个 overdraw 热点定位器

**答**：
- 需求：implement hotspots(grid, threshold)。grid 为渲染计数二维数组（w*h）；输出热点区块（聚合相邻超阈值像素为 { x0, y0, w, h, avg }），按 avg 降序；聚合用 flood fill（4 邻域）。
- 边界：threshold 默认 3；grid 空返回空；聚合最小面积 4 像素否则丢弃；坐标为像素索引。
- 评分点：flood fill 聚合；阈值过滤；包围盒；最小面积

```javascript
function hotspots(grid, threshold = 3) {
  const { w, h, data } = grid;
  const visited = new Uint8Array(w * h);
  const out = [];
  const stack = [];
  for (let i = 0; i < data.length; i++) {
    if (data[i] <= threshold || visited[i]) continue;
    stack.length = 0; stack.push(i);
    visited[i] = 1;
    let sum = 0, count = 0, x0 = i % w, x1 = x0, y0 = (i / w) | 0, y1 = y0;
    while (stack.length) {
      const idx = stack.pop();
      const x = idx % w, y = (idx / w) | 0;
      sum += data[idx]; count++;
      x0 = Math.min(x0, x); x1 = Math.max(x1, x);
      y0 = Math.min(y0, y); y1 = Math.max(y1, y);
      for (const [dx, dy] of [[1,0],[-1,0],[0,1],[0,-1]]) {
        const nx = x + dx, ny = y + dy;
        if (nx < 0 || ny < 0 || nx >= w || ny >= h) continue;
        const ni = ny * w + nx;
        if (!visited[ni] && data[ni] > threshold) {
          visited[ni] = 1; stack.push(ni);
        }
      }
    }
    if (count >= 4)
      out.push({ x0, y0, w: x1 - x0 + 1, h: y1 - y0 + 1,
        avg: +(sum / count).toFixed(2) });
  }
  return out.sort((a, b) => b.avg - a.avg);
}
```
