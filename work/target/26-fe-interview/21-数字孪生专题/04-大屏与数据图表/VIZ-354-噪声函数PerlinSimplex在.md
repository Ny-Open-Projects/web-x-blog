---
title: [VIZ-354] 噪声函数（Perlin/Simplex）在图形中的应用与实现要点
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-354：噪声函数（Perlin/Simplex）在图形中的应用与实现要点

**答**：
- 用途：程序化纹理、地形高度、粒子扰动、屏幕空间噪声（抖动/溶解）。
- Perlin：网格梯度 + 插值，梯度随机化避免网格伪影；Simplex 计算更快、各向同性更好。
- FBM（分形布朗运动）：多倍频叠加（octaves 4~6，lacunarity 2，gain 0.5）产生自然细节。

```javascript
// 值噪声 + FBM（简化版，够用于动效）
function hash2(x, y) {
  const s = Math.sin(x * 127.1 + y * 311.7) * 43758.5453;
  return s - Math.floor(s);
}
function smooth(t) { return t * t * (3 - 2 * t); }
function valueNoise(x, y) {
  const xi = Math.floor(x), yi = Math.floor(y);
  const xf = smooth(x - xi), yf = smooth(y - yi);
  const a = hash2(xi, yi), b = hash2(xi+1, yi);
  const c = hash2(xi, yi+1), d = hash2(xi+1, yi+1);
  const u = a + (b-a)*xf, v = c + (d-c)*xf;
  return u + (v-u)*yf;
}
function fbm(x, y, octaves = 5) {
  let sum = 0, amp = 0.5, freq = 1;
  for (let o = 0; o < octaves; o++) {
    sum += amp * valueNoise(x*freq, y*freq);
    amp *= 0.5; freq *= 2;
  }
  return sum;
}
```
