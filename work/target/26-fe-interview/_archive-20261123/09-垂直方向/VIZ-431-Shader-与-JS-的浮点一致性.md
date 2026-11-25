---
title: [VIZ-431] Shader 与 JS 的浮点一致性：为什么 CPU 算的和 GPU 不一样
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-431：Shader 与 JS 的浮点一致性：为什么 CPU 算的和 GPU 不一样

**答**：
- GPU float32 + 编译器重排/融合乘加（FMA）与 JS double 精度结果有微小差异。
- 影响：CPU 预计算的物理结果与 GPU 渲染判定（拾取/碰撞）不一致——浮点误差累积。
- 对策：关键判定结果由 GPU 输出（readback）而非 CPU 复算；或 CPU 用 float32 模拟（Math.fround）。

```javascript
// float32 对齐
function f32mul(a, b) { return Math.fround(Math.fround(a) * Math.fround(b)); }
// 验证一致性：
function consistencyCheck(cpuVal, gpuReadback, eps = 1e-3) {
  return Math.abs(Math.fround(cpuVal) - gpuReadback) < eps;
}
// 大数坐标：世界坐标 > 10000 时精度抖动——用相机相对坐标（浮点原点）
```
