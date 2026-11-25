---
title: [VIZ-361] LOD（细节层次）的切换判定与平滑过渡
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-361：LOD（细节层次）的切换判定与平滑过渡

**答**：
- 切换依据：屏幕投影误差——物体在屏幕上的像素高度 / lod 距离阈值；距离 + 屏幕占比双条件更稳。
- 平滑：几何 morph（两 LOD 顶点插值）或透明度渐变；硬切换的"弹跳"在相机移动时明显。
- 生成：离线工具（meshoptimizer simplifier）按比例 100%/50%/25% 生成，运行时按屏幕误差选择。

```javascript
// LOD 选择
function pickLOD(dist, screenH, sizes, { pixelErr = 4 } = {}) {
  // sizes: 各 LOD 的近似几何误差（世界单位）
  const proj = (err, d) => err * (screenH / (2 * Math.tan(30 * Math.PI/180) * d));
  for (let i = 0; i < sizes.length; i++) {
    if (proj(sizes[i], dist) < pixelErr) return i;   // 误差低于阈值即够
  }
  return sizes.length - 1;                            // 最粗 LOD
}
// 硬切换防弹跳：dist 落入 [th*0.95, th*1.05] 滞回带不切换
```
