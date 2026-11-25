---
title: [VIZ-341] 视图矩阵（LookAt）的推导
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-341：视图矩阵（LookAt）的推导

**答**：
- LookAt = 平移的逆 × 旋转：相机坐标系的三个基向量（forward/right/up）构成旋转矩阵。
- forward = normalize(eye - target)（相机看 -z），right = normalize(cross(up, forward))，up = cross(forward, right)。
- up 退化：forward 与 worldUp 平行时 cross 为 0——需要 fallback up（如改用 x 轴）。

```javascript
// LookAt 矩阵
function lookAt(eye, target, worldUp = [0, 1, 0]) {
  const sub = (a, b) => a.map((v, i) => v - b[i]);
  const norm = v => { const l = Math.hypot(...v) || 1; return v.map(x => x/l); };
  const cross3 = (a, b) => [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]];
  let f = norm(sub(eye, target));            // forward
  let r = norm(cross3(worldUp, f));
  if (!isFinite(r[0])) {                     // 退化：平行
    r = norm(cross3([1, 0, 0], f));
  }
  const u = cross3(f, r);
  return [r[0], u[0], f[0], 0,
          r[1], u[1], f[1], 0,
          r[2], u[2], f[2], 0,
          -r.reduce((s, v, i) => s + v*eye[i], 0),
          -u.reduce((s, v, i) => s + v*eye[i], 0),
          -f.reduce((s, v, i) => s + v*eye[i], 0), 1];
}
```
