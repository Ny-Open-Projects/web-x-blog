---
title: [VIZ-366] 视差贴图（Parallax/Normal Map）的数学差异
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-366：视差贴图（Parallax/Normal Map）的数学差异

**答**：
- Normal Map：只改光照法线不改几何——视角变化时轮廓不变（"假凸起"）。
- Parallax Occlusion：沿视线在高度图上采样位移 UV，产生真实视差；代价是多次采样循环。
- 选型：静态展示 Normal Map 够用；第一人称/特写用 Parallax；开销敏感移动端降级 Normal。

```javascript
// Parallax UV 偏移
function parallaxUV(uv, viewDirTS, heightMap, { scale = 0.05, steps = 8 } = {}) {
  let depth = 0;
  const stepD = 1 / steps;
  const [vx, vy] = viewDirTS;
  for (let i = 0; i < steps; i++) {
    const h = heightMap(uv[0], uv[1]);      // 当前高度
    depth += stepD;
    if (h <= 1 - depth) break;
    uv = [uv[0] + vx * scale * stepD, uv[1] + vy * scale * stepD];
  }
  return uv;
}
// Normal map 只影响光照：
// N = normalize(2.0 * texture(normalMap, uv).rgb - 1.0)
```
