---
title: [VIZ-375] 拾取（Picking）的三种实现与取舍
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-375：拾取（Picking）的三种实现与取舍

**答**：
- CPU 射线：射线与场景几何求交（BVH 加速），精确但大数据量要建加速结构。
- GPU 拾取：渲染 pass 用 ID 颜色编码，读回 1 像素——简单但多一次渲染。
- 数学拾取：体素/网格直接坐标换算（瓦片地图），最快但要按场景定制。

```javascript
// 三种拾取
function pickByRay(scene, ray, bvh) {
  return bvhRay(bvh, ray.origin, ray.dir,
    leaves => leaves.reduce((best, it) => {
      const h = rayAABB(ray.origin, ray.dir, it.box.min, it.box.max);
      return h && (!best || h.t < best.t) ? { ...h, item: it } : best;
    }, null));
}
async function pickByGPU(gl, x, y, renderIdPass) {
  renderIdPass();                                   // ID 颜色渲染
  const px = new Uint8Array(4);
  gl.readPixels(x, y, 1, 1, gl.RGBA, gl.UNSIGNED_BYTE, px);
  return px[0] | px[1] << 8 | px[2] << 16;          // 还原实例 ID
}
```
