---
title: [H5-207] WebGL 入门第一课：上下文-shader-缓冲区最小闭环
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebGL]
type: 面试题
---

## H5-207：WebGL 入门第一课：上下文-shader-缓冲区最小闭环

**答**：
- WebGL 流程闭环五步：取上下文 → 编译着色器 → 建缓冲区灌顶点数据 → 关联 attribute → drawArrays
- 着色器是 GPU 上运行的程序：顶点着色器算出每个点的位置，片元着色器算出每个像素的颜色
- 与 Canvas 2D 的本质区别：Canvas 2D 是「命令式画」，WebGL 是「数据驱动渲染」，CPU 只准备数据，绘制由 GPU 并行完成
- 最小代码量证明理解：能默写 20 行画出一个三角形，说明入门了

```javascript
const gl = canvas.getContext('webgl');
const vs = `attribute vec2 p; void main(){ gl_Position = vec4(p, 0., 1.); }`;
const fs = `void main(){ gl_FragColor = vec4(1., .5, 0., 1.); }`;
function shader(type, src) {
  const s = gl.createShader(type);
  gl.shaderSource(s, src); gl.compileShader(s);
  return s;
}
const prog = gl.createProgram();
gl.attachShader(prog, shader(gl.VERTEX_SHADER, vs));
gl.attachShader(prog, shader(gl.FRAGMENT_SHADER, fs));
gl.linkProgram(prog); gl.useProgram(prog);
const buf = gl.createBuffer();
gl.bindBuffer(gl.ARRAY_BUFFER, buf);
gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([0,.5, -.5,-.5, .5,-.5]), gl.STATIC_DRAW);
const loc = gl.getAttribLocation(prog, 'p');
gl.enableVertexAttribArray(loc);
gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
gl.drawArrays(gl.TRIANGLES, 0, 3);
```
