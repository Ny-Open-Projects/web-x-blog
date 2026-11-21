---
title: [H5-208] WebGL 顶点着色器和片元着色器分别干什么
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebGL]
type: 面试题
---

## H5-208：WebGL 顶点着色器和片元着色器分别干什么

**答**：
- 顶点着色器：每个顶点跑一次，输入顶点属性（位置/法线/UV），输出裁剪空间坐标 gl_Position；负责 MVP 变换
- 片元着色器：每个候选像素跑一次，输入插值后的 varying 变量，输出颜色 gl_FragColor；负责材质、光照、纹理采样
- 数据传递：顶点→片元靠 varying 插值（如顶点颜色在三角形内自动平滑过渡）
- 数量级差异：一帧可能只跑几百次顶点着色，但跑百万次片元着色——片元着色器是性能大头
- 面试钩子：uniform（全局常量，每帧更新）vs attribute（每顶点）vs varying（插值）三类变量要分清

```glsl
// 顶点着色器：位置变换 + 传颜色
attribute vec3 aPos; attribute vec3 aColor;
uniform mat4 uMVP;
varying vec3 vColor;
void main() {
  gl_Position = uMVP * vec4(aPos, 1.0);
  vColor = aColor;
}
// 片元着色器：直接用插值后的颜色
varying vec3 vColor;
void main() { gl_FragColor = vec4(vColor, 1.0); }
```
