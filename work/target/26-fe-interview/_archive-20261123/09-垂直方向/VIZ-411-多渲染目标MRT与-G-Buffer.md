---
title: [VIZ-411] 多渲染目标（MRT）与 G-Buffer 打包
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-411：多渲染目标（MRT）与 G-Buffer 打包

**答**：
- WebGL2/WebGPU 支持多 attach：一次片元写多个目标（G-Buffer）。
- 打包技巧：法线存 octahedral 编码（2×16bit）、材质参数打包 RGBA8 各 8bit。
- 对齐：attach 数量与格式受 MAX_COLOR_ATTACHMENTS 限制（WebGL2 至少 4）。

```javascript
// 法线八面体编码
function encodeOcta(n) {
  const p = [n[0], n[1]].map(v => v / (Math.abs(n[0]) + Math.abs(n[1]) + Math.abs(n[2]) + 1e-9));
  return n[2] < 0
    ? [(1 - Math.abs(p[1])) * Math.sign(p[0] || 1e-9),
       (1 - Math.abs(p[0])) * Math.sign(p[1] || 1e-9)] : p;
}
function decodeOcta(p) {
  const z = 1 - Math.abs(p[0]) - Math.abs(p[1]);
  return [p[0], p[1], z].map(v => v);   // 归一化略
}
// G-Buffer：attach0 RGBA8 albedo+flag, attach1 RG16F 法线 + BA rough/metal
```
