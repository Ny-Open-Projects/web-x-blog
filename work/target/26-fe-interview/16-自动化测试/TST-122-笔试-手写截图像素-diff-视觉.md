---
title: [TST-122] 笔试：手写截图像素 diff（阈值 + diff mask + 输出差异图）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-122：笔试：手写截图像素 diff（阈值 + diff mask + 输出差异图）
**答**：
- 需求：实现 `pixelDiff(baseline, current, { maxDiffRatio, threshold, mask })`——比较两张同尺寸 RGBA 截图，返回 `{ ratio, diffImage }`；`mask` 区域忽略；超阈值抛错并输出差异可视化图（红框标出差异像素）。
- 核心：逐像素比较 RGB 通道，任一通道差值超过 threshold（0~255）记为差异像素；差异像素写进 diffImage（白色底 + 红色点）；mask 用坐标矩形提前置为相等。
- 边界：尺寸不一致直接抛错（不可比）；空图/全等图 ratio=0 不生成 diff；ratio 计算用「差异像素 / 总像素」。

```javascript
function pixelDiff(base, curr, { maxDiffRatio = 0.01, threshold = 10, mask = [] } = {}) {
  const { width: w, height: h, data: a } = base;
  const { width: w2, height: h2, data: b } = curr;
  if (w !== w2 || h !== h2) {
    throw new Error(`size mismatch: ${w}x${h} vs ${w2}x${h2}`); // 尺寸不可比
  }
  const inMask = (x, y) => mask.some((m) => x >= m.x && x < m.x + m.w && y >= m.y && y < m.y + m.h);

  const diff = new Uint8ClampedArray(a.length); // 白底
  diff.fill(255);
  let diffPixels = 0;
  for (let i = 0; i < a.length; i += 4) {
    const idx = i / 4, x = idx % w, y = (idx / w) | 0;
    if (inMask(x, y)) continue;                        // mask 忽略
    const d = Math.max(Math.abs(a[i] - b[i]), Math.abs(a[i + 1] - b[i + 1]), Math.abs(a[i + 2] - b[i + 2]));
    if (d > threshold) {
      diffPixels++;
      diff[i] = 255; diff[i + 1] = 0; diff[i + 2] = 0; diff[i + 3] = 255; // 红色标差异
    }
  }
  const ratio = diffPixels / (w * h);
  if (ratio > maxDiffRatio) {
    const err = new Error(`visual diff ${ratio.toFixed(4)} > ${maxDiffRatio}`);
    err.diffImage = { width: w, height: h, data: diff }; // 供报告展示
    throw err;
  }
  return { ratio, diffImage: { width: w, height: h, data: diff } };
}

// base/curr 为 {width,height,data:Uint8ClampedArray(RGBA)}
// 用法：mask 掉时间戳区域，阈值 1%
// pixelDiff(base, curr, { mask: [{ x: 0, y: 0, w: 200, h: 24 }], maxDiffRatio: 0.01 });
```

**评分点**：
1. 尺寸不一致是否显式抛错而非逐像素越界比较。
2. mask 判定是否在比较前短路（性能）且含边界（x < m.x + m.w）。
3. 阈值语义清晰：通道差值 vs 像素级 ratio 两层阈值。
4. 是否输出可视化 diff 图（面试官关注工程化思维）。
