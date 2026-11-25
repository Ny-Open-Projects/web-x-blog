---
title: [VIZ-467] 手写一个 LOD 选择器（屏幕误差 + 距离）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## VIZ-467：手写一个 LOD 选择器（屏幕误差 + 距离）

**答**：
- 需求：实现 selectLOD(object, camera)。object 为 { lods: [{ geo, err }], pos }；按屏幕投影误差选 LOD：err 的屏幕像素高度 < 2px 可用该级；相机 fov/viewport 由 camera 提供；输出 { index, screenPx }。
- 边界：距离为 0 取最细 LOD；fov 默认 45°；viewport 高度默认 1080；无匹配取最粗。
- 评分点：投影误差；遍历选择；零距离；最粗兜底

```javascript
function selectLOD(object, camera, { fov = 45, height = 1080 } = {}) {
  const d = Math.hypot(...object.pos.map((v, i) => v - camera.pos[i]));
  if (d < 1e-6) return { index: 0, screenPx: Infinity };
  const perUnit = height / (2 * Math.tan(fov * Math.PI / 360) * d);
  for (let i = 0; i < object.lods.length; i++) {
    const px = object.lods[i].err * perUnit;
    if (px < 2) return { index: i, screenPx: +px.toFixed(2) };
  }
  return { index: object.lods.length - 1,
    screenPx: +(object.lods[object.lods.length - 1].err * perUnit).toFixed(2) };
}
// 滞回防弹跳：err 接近 2px 的 ±5% 内保持当前级
```
