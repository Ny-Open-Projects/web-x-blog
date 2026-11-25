---
title: [VIZ-352] 深度缓冲与 z-fighting 的数学根源
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-352：深度缓冲与 z-fighting 的数学根源

**答**：
- 透视深度非线性：z_ndc 与视空间深度非线性映射，远处两个相近深度被压到同一 NDC 值。
- 解决排序：提高 near、降低 far 比、polygonOffset（法线偏移）、logarithmic depth、stencil/模板分层。
- 透明物体不写深度：排序渲染（画家算法）+ 深度只读，混合顺序错误会导致视觉 artifact。

```javascript
// 深度冲突检测辅助
function zConflictRisk(near, far, bits = 24, atZ = 100) {
  const prec = depthPrecision(atZ, near);        // 见 342
  return { precisionAt100: prec,
    risk: prec > 0.01 ? '高（增大 near 或用 log depth）' : 'ok',
    ratio: (far / near).toFixed(0) };
}
// polygonOffset 配置（WebGL）：
// gl.enable(gl.POLYGON_OFFSET_FILL);
// gl.polygonOffset(1, 1);   // 地面 vs 贴地 Decal
```
