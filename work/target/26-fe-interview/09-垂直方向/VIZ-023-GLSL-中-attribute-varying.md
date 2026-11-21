---
title: [VIZ-023] GLSL 中 attribute、varying、uniform 的区别？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-023：GLSL 中 attribute、varying、uniform 的区别？
**答**：**attribute**：逐顶点输入，只在顶点着色器可用（WebGL2 里叫 in），如坐标、法线、UV；**varying**：顶点着色器写入、经光栅化**插值**后传给片元着色器读取（WebGL2 里 out/in 配对），如逐像素的颜色/UV；**uniform**：全局常量，一次 draw 内所有顶点与片元共享同一值，由 JS 上传，如变换矩阵、时间、颜色。三者组合出"每顶点不同、每像素插值、整体统一"三个粒度。

```javascript
const vs = `
attribute vec2 aPos;          // attribute：每个顶点不同的输入
uniform float uPointSize;     // uniform：本次 draw 全局统一
varying float vAlpha;         // varying：写入后经光栅化插值传给片元
void main() {
  gl_Position = vec4(aPos, 0.0, 1.0);
  gl_PointSize = uPointSize;
  vAlpha = 0.5 + aPos.y * 0.5;
}`;
const fs = `
precision mediump float;
uniform vec3 uColor;
varying float vAlpha;         // FS 中读到的 vAlpha 已按像素位置插值
void main() { gl_FragColor = vec4(uColor, vAlpha); }`;
// 记忆：attribute 逐顶点、varying 逐像素插值、uniform 每次 draw 一份
```
