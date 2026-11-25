---
title: [VIZ-211] WebGPU 视锥剔除与遮挡剔除：大数据场景裁剪
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-211：WebGPU 视锥剔除与遮挡剔除：大数据场景裁剪

**答**：
- 视锥剔除：CPU 侧按相机视锥体（6 平面）剔除包围盒外对象——drawCount 决定帧耗时，剔除 80% 即省 80%。
- 遮挡剔除：深度 pre-pass（先渲染深度）或 Hi-Z（Mip 链深度查询）——被挡住的跳过（WebGPU 无硬件 query，需 CPU 近似）。
- 工程落地：空间网格/八叉树加速「查询视锥内对象」。

```javascript
function frustumCull(objects, camera) {
  const planes = extractFrustumPlanes(camera.matrixVP);   // 6 平面方程
  return objects.filter(obj => {
    const box = obj.boundingBoxWorld();
    return planes.every(p => boxIntersectsPlaneSide(box, p));   // 任一平面外即剔除
  });
}
function extractFrustumPlanes(m) {                       // m 为列主序 VP 矩阵
  // Gribb-Hartmann 方法：从矩阵行组合提取 6 平面
  return [
    [m[3] + m[0], m[7] + m[4], m[11] + m[8], m[15] + m[12]],   // left
    [m[3] - m[0], m[7] - m[4], m[11] - m[8], m[15] - m[12]],   // right
    // top/bottom/near/far 同理
  ];
}
// 遮挡剔除近似：把视锥剔除后的对象按深度排序，前景先画 → 深度测试自动丢弃被挡片元（GPU 级）
```
