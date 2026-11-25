---
title: [VIZ-025] MVP（模型/视图/投影）矩阵分别做什么？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-025：MVP（模型/视图/投影）矩阵分别做什么？
**答**：裁剪空间坐标 = **P × V × M × 顶点**。**M（模型矩阵）**：物体局部坐标 → 世界坐标（物体的位移/旋转/缩放）；**V（视图矩阵）**：世界 → 相机空间（等价于相机的逆变换，lookAt）；**P（投影矩阵）**：相机空间 → 裁剪空间（透视投影带除 w，正交投影不带）。工程上通常在 JS 端把三者预乘成一个 mvp 矩阵，用一个 uniform 传入顶点着色器，省三次矩阵乘法。注意 WebGL 矩阵是列主序，传 `uniformMatrix4fv` 时不要转置。

```javascript
// gl-matrix：clip = P * V * M * pos，列主序 Float32Array
import { mat4 } from 'gl-matrix';
const model = mat4.create();                 // 模型：物体局部 -> 世界
mat4.rotateY(model, model, Math.PI / 4);
const view = mat4.create();                  // 视图：世界 -> 相机
mat4.lookAt(view, [0, 0, 5], [0, 0, 0], [0, 1, 0]);
const proj = mat4.create();                  // 投影：相机 -> 裁剪空间
mat4.perspective(proj, Math.PI / 4, canvas.width / canvas.height, 0.1, 100);
const mvp = mat4.create();
mat4.multiply(mvp, proj, view);
mat4.multiply(mvp, mvp, model);              // 预乘成一个矩阵，VS 里只乘一次
gl.uniformMatrix4fv(uMvpLoc, false, mvp);    // false：不转置，WebGL 用列主序
```
