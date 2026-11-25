---
title: [VIZ-429] Shader 内的矩阵计算：何时在 CPU 预算
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-429：Shader 内的矩阵计算：何时在 CPU 预算

**答**：
- 原则：逐顶点/逐片元重复的矩阵运算预计算（CPU/顶点级）；逐实例不同才下放。
- 典型：法线矩阵每对象一次（CPU）、MVP 每对象一次（CPU），shader 只乘一次。
- 反模式：shader 里每片元重复计算常量矩阵（光源矩阵等）——提为 uniform。

```javascript
// CPU 预计算清单
function perObjectUniforms(model, view, proj) {
  return {
    mvp: mul4(mul4(proj, view), model),          // 一次乘好
    normalMat: normalMatrix(model),              // 349
    // 反模式：shader 内做 mul4(proj, mul4(view, model)) 每顶点 2 次乘
  };
}
```
