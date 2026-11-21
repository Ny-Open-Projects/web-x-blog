---
title: [H5-215] WebGL 2 和 WebGL 1 的区别是什么
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebGL]
type: 面试题
---

## H5-215：WebGL 2 和 WebGL 1 的区别是什么

**答**：
- WebGL2 = OpenGL ES 3.0，主要升级：GLSL 3.0 语法、3D 纹理与 2 的幂纹理全面支持 mipmap、多种新格式（float 纹理、深度纹理）
- 渲染对象：非方形尺寸的 frame buffer（离屏渲染）不再受限；多重采样渲染缓冲内建支持
- 新绘制方式：VAO（顶点数组对象，一次绑定所有 attribute 配置）、transform feedback（GPU 输出回 GPU，粒子系统利器）、instancing 原生内建
- 实用层面：WebGL1 的诸多扩展（OES_texture_float 等）在 2 里成为核心功能，代码更干净
- 兼容策略：`getContext('webgl2') || getContext('webgl')` 降级；着色器语法要按版本分支维护

```javascript
const gl = canvas.getContext('webgl2');
if (gl) {
  const vao = gl.createVertexArray();  // WebGL2 核心 VAO
  gl.bindVertexArray(vao);             // 一次配置，帧间复用
} else {
  const gl1 = canvas.getContext('webgl'); // 降级路径
}
```
