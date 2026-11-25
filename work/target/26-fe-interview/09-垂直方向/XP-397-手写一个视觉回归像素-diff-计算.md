---
title: [XP-397] 手写一个视觉回归像素 diff 计算器
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## XP-397：手写一个视觉回归像素 diff 计算器

**答**：
- 需求：implement pixelDiff(imgA, imgB, { threshold = 10 })。imgA/B 为 { w, h, data } RGBA；逐像素比较 RGB 差值超 threshold 记差异；输出 { diffPixels, pct, bbox }（差异包围盒）；尺寸不一致报错。
- 边界：alpha 忽略；pct 保留 2 位；bbox 为最小覆盖矩形（无差异 null）；大图抽样（步长 2）可配。
- 评分点：逐像素比较；阈值；包围盒；抽样

```javascript
function pixelDiff(a, b, { threshold = 10, step = 1 } = {}) {
  if (a.w !== b.w || a.h !== b.h) throw new Error('尺寸不一致');
  let diff = 0, total = 0;
  let x0 = a.w, x1 = 0, y0 = a.h, y1 = 0;
  for (let y = 0; y < a.h; y += step)
    for (let x = 0; x < a.w; x += step) {
      const i = (y * a.w + x) * 4;
      total++;
      const d = Math.abs(a.data[i] - b.data[i]) +
        Math.abs(a.data[i+1] - b.data[i+1]) +
        Math.abs(a.data[i+2] - b.data[i+2]);
      if (d > threshold * 3) {
        diff++;
        x0 = Math.min(x0, x); x1 = Math.max(x1, x);
        y0 = Math.min(y0, y); y1 = Math.max(y1, y);
      }
    }
  return { diffPixels: diff, pct: +(diff / total * 100).toFixed(2),
    bbox: diff ? { x0, y0, x1, y1 } : null };
}
```
