---
title: [H5-213] WebGL 矩阵变换 MVP 是什么
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebGL]
type: 面试题
---

## H5-213：WebGL 矩阵变换 MVP 是什么

**答**：
- MVP = Model（模型局部→世界）× View（世界→相机）× Projection（相机→裁剪空间），三个 4x4 矩阵相乘作用于顶点
- Model：物体的位置/旋转/缩放；View：相机的逆变换（相机后退=世界前进）；Projection：透视/正交投影
- 用矩阵而非逐顶点运算的原因：一个 uniform 矩阵描述全部顶点的统一变换，GPU 并行执行
- 齐次坐标（x,y,z,1）：平移才能表示成矩阵乘法；透视除法用 w 分量
- 钩子：列主序（WebGL/OpenGL）vs 行主序（DX）——传矩阵时要 transpose 或预先转置

```glsl
// gl_Position = uProjection * uView * uModel * vec4(aPos, 1.0);
// 顺序从右往左：先模型变换，再观察，最后投影
```
```javascript
// three.js 内部帮你做了 MVP；手动写原生时用 gl-matrix
import { mat4 } from 'gl-matrix';
const mvp = mat4.create();
mat4.multiply(mvp, proj, view);
mat4.multiply(mvp, mvp, model);
gl.uniformMatrix4fv(uMvpLoc, false, mvp); // false = 不转置（列主序）
```
