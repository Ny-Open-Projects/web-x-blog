---
title: [VIZ-394] Instanced 绘制在 shader 侧怎么写
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-394：Instanced 绘制在 shader 侧怎么写

**答**：
- WebGL2 drawArraysInstanced + gl_InstanceID；或实例属性 divisor 设置（每实例步进）。
- shader：用 instance attribute（矩阵拆 4 个 vec4 行）变换位置；CPU 侧只需更新 instance buffer。
- 性能：万级实例瓶颈在顶点数×实例数——LOD/剔除配合（每实例 AABB 视锥剔除）。

```javascript
// 实例化 shader
`#version 300 es
in vec3 aPos;
in vec4 iMat0; in vec4 iMat1; in vec4 iMat2; in vec4 iMat3;
uniform mat4 uVP;
void main() {
  mat4 model = mat4(iMat0, iMat1, iMat2, iMat3);
  gl_Position = uVP * model * vec4(aPos, 1.0);
}`
// buffer 分割：
gl.vertexAttribDivisor(1, 1);   // 每实例步进 1
gl.drawArraysInstanced(gl.TRIANGLES, 0, vertCount, instanceCount);
```
