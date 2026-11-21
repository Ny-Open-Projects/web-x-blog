---
title: [TST-417] 笔试：实现灰度图像素 diff（阈值 + 差异统计 + mask 区域）。
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-417：笔试：实现灰度图像素 diff（阈值 + 差异统计 + mask 区域）。
**题目**：输入两幅等尺寸灰度图（二维数组）与阈值 t：逐像素 |a-b| > t 记为差异点，输出 `{ratio, diffPixels, regions}`；支持 mask 矩形区域（区域内忽略）。

```javascript
function pixelDiff(a, b, t = 10, masks = []) {
  const inMask = (y, x) => masks.some(m => y >= m.y1 && y <= m.y2 && x >= m.x1 && x <= m.x2);
  const H = a.length, W = a[0].length;
  const grid = [];
  let diff = 0;
  for (let y = 0; y < H; y++) {
    grid[y] = [];
    for (let x = 0; x < W; x++) {
      const d = inMask(y, x) ? 0 : Math.abs(a[y][x] - b[y][x]) > t ? 1 : 0;
      grid[y][x] = d; diff += d;
    }
  }
  return { diffPixels: diff, ratio: +(diff / (H * W)).toFixed(4), grid };
}

```

**评分点**：
- 逐像素阈值比较（|a-b| > t）。
- mask 区域内像素跳过。
- ratio 分母是总像素（mask 不从分母扣——或说明取舍）。
- 差异点相邻聚合成区域（简化 BFS）为加分项。
