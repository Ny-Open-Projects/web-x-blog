---
title: [VIZ-453] 渲染数据结构的 SoA vs AoS（buffer 布局）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-453：渲染数据结构的 SoA vs AoS（buffer 布局）

**答**：
- SoA（结构数组）：position[3N]/normal[3N] 分离存储——GPU 顶点抓取带宽友好（按需读 attribute）。
- AoS：交错（x,y,z,nx,ny,nz...）单 buffer 一次抓取；CPU 更新友好。
- 选择：高频更新的动态几何用 AoS 单次上传；静态几何 SoA 分 attribute buffer。

```javascript
// 布局对比
function interleave(positions, normals, uvs) {       // AoS
  const n = positions.length / 3;
  const out = new Float32Array(n * 8);
  for (let i = 0; i < n; i++) {
    out.set(positions.slice(i*3, i*3+3), i*8);
    out.set(normals.slice(i*3, i*3+3), i*8+3);
    out.set(uvs.slice(i*2, i*2+2), i*8+6);
  }
  return out;   // stride 32B，一次绑定
}
```
