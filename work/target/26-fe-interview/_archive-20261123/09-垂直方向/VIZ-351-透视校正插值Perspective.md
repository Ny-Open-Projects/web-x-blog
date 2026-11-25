---
title: [VIZ-351] 透视校正插值（Perspective Correct）为什么必要
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-351：透视校正插值（Perspective Correct）为什么必要

**答**：
- 屏幕空间线性插值深度/UV 在透视下错误——近处像素"占用"更多世界空间。
- 正确做法：插值 1/w（或属性/w），再除以插值后的 1/w 还原；GPU 硬件已做，软件光栅/WebGL2 变量插值注意。
- 可视化验证：贴图在斜面上呈"梯形拉伸"错误即是线性插值症状。

```javascript
// 透视校正插值
function perspCorrect(attrs, ws, screenT) {
  // attrs/w 先线性插值再除回
  const interp = attrs.map((a, i) => a / ws[i]);
  const lerp = (x, y, t) => x + (y - x) * t;
  const v = attrs.map((_, i) => lerp(interp[i], interp[i], screenT));
  const w = lerp(1 / ws[0], 1 / ws[1], screenT);
  return v.map(x => x / w);
}
// 简化验证：深度 z0=1 z1=10，屏幕中点线性得 5.5，
// 校正后接近 2（近处像素多）——即"近大远小"的数值表现。
```
