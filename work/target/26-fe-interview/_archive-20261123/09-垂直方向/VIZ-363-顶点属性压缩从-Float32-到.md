---
title: [VIZ-363] 顶点属性压缩：从 Float32 到 Int16/归一化
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-363：顶点属性压缩：从 Float32 到 Int16/归一化

**答**：
- 位置：Float32 → 精度不足时用相对原点（实例局部坐标）+ Int16 归一化；法线可用 SNORM8（符号化 8bit）。
- UV：0-1 范围用 UNORM16 足够；顶点色用 UNORM8×4。
- 收益：显存带宽减半/减半再减半，顶点抓取是移动端瓶颈时收益直接体现在帧时间。

```javascript
// 顶点压缩示例
function packNormal(nx, ny, nz) {         // SNORM8 风格
  const q = (v) => Math.round((Math.max(-1, Math.min(1, v)) * 127) + 128);
  return [q(nx), q(ny), q(nz)];
}
function packUV(u, v) {                   // UNORM16
  return [Math.round(u * 65535), Math.round(v * 65535)];
}
// 解包（shader）：
// vec3 n = unpackSnorm3x8(packedNormal) / 127.0
// 顶点缓冲 32B/顶点 -> 12B/顶点，带宽 -62%
```
